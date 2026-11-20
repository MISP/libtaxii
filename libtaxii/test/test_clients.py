from __future__ import unicode_literals

from email.message import Message
import ssl

import pytest
import six
from six.moves import http_client, urllib

from libtaxii import get_message_from_http_response
from libtaxii.clients import LibtaxiiHTTPSHandler, VerifiableHTTPSConnection
from libtaxii.constants import ST_FAILURE, VID_TAXII_XML_11


@pytest.mark.parametrize('verify_server', [False, True])
def test_connection(verify_server):
    conn = VerifiableHTTPSConnection('example.org', verify_server=verify_server)

    assert conn.context.protocol == ssl.PROTOCOL_TLS_CLIENT
    assert conn.context.check_hostname == verify_server
    assert conn.context.verify_mode == (ssl.CERT_REQUIRED if verify_server else ssl.CERT_NONE)


def test_https_handler_preserves_timeout():
    conn = LibtaxiiHTTPSHandler().get_connection('example.org', timeout=3)

    assert conn.timeout == 3


@pytest.mark.parametrize('response_type', ['http', 'url', 'error'])
def test_response_charset(response_type):
    status_xml = (
        '<taxii:Status_Message xmlns:taxii="http://taxii.mitre.org/messages/taxii_xml_binding-1.1"'
        ' message_id="1" in_response_to="0" status_type="FAILURE">'
        '<taxii:Message>caf\u00e9</taxii:Message></taxii:Status_Message>'
    )
    headers = Message()
    headers['Content-Type'] = 'application/xml; charset="iso-8859-1"'
    headers['X-TAXII-Content-Type'] = VID_TAXII_XML_11
    body = status_xml.encode('iso-8859-1')

    if response_type == 'http':
        class ResponseSocket(object):
            def makefile(self, mode):
                return six.BytesIO(b'HTTP/1.1 200 OK\r\n' + headers.as_string().encode('ascii') + b'\r\n' + body)

        response = http_client.HTTPResponse(ResponseSocket())
        response.begin()
    elif response_type == 'url':
        response = urllib.response.addinfourl(six.BytesIO(body), headers, 'http://example.org/')
    else:
        response = urllib.error.HTTPError('http://example.org/', 400, 'Failure', headers, six.BytesIO(body))

    message = get_message_from_http_response(response, '0')

    assert message.status_type == ST_FAILURE
    assert message.message == 'caf\u00e9'


def test_response_without_content_type():
    response = urllib.response.addinfourl(six.BytesIO(b'details'), Message(), 'http://example.org/')

    message = get_message_from_http_response(response, '123')

    assert message.status_type == ST_FAILURE
    assert message.in_response_to == '123'
    assert message.message.endswith('details')

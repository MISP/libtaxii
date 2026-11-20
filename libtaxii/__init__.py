# Copyright (c) 2017, The MITRE Corporation
# For license information, see the LICENSE.txt file

"""
The main libtaxii module
"""

from email.message import Message

import six
from six.moves import urllib

import libtaxii.messages_10 as tm10
import libtaxii.messages_11 as tm11
import libtaxii.clients as tc
from .constants import *

from .version import __version__  # noqa


def _get_response_encoding(content_type):
    headers = Message()
    if content_type:
        headers['Content-Type'] = content_type
    return headers.get_content_charset('utf-8')


def get_message_from_http_response(http_response, in_response_to):
    """Create a TAXII message from an HTTPResponse object.

    This function parses the :py:class:`httplib.HTTPResponse` by reading the
    X-TAXII-Content-Type HTTP header to determine if the message binding is
    supported. If the X-TAXII-Content-Type header is present and the value
    indicates a supported Message Binding, this function will attempt to parse
    the HTTP Response body.

    If the X-TAXII-Content-Type header is not present, this function will
    attempt to build a Failure Status Message per the HTTP Binding 1.0
    specification.

    If the X-TAXII-Content-Type header is present and indicates an unsupported
    Message Binding, this function will raise a ValueError.

    Args:
        http_response (httplib.HTTPResponse): the HTTP response to
            parse
        in_response_to (str): the default value for in_response_to
    """
    if isinstance(http_response, six.moves.http_client.HTTPResponse):
        return get_message_from_httplib_http_response(http_response, in_response_to)
    elif isinstance(http_response, urllib.error.HTTPError):
        return get_message_from_urllib2_httperror(http_response, in_response_to)
    elif isinstance(http_response, urllib.response.addinfourl):
        return get_message_from_urllib_addinfourl(http_response, in_response_to)
    else:
        raise ValueError('Unsupported response type: %s.' % http_response.__class__.__name__)


def get_message_from_urllib2_httperror(http_response, in_response_to):
    """ This function should not be called by libtaxii users directly. """
    info = http_response.info()

    get_header = info.getheader if hasattr(info, 'getheader') else info.get
    taxii_content_type = get_header('X-TAXII-Content-Type')
    encoding = _get_response_encoding(get_header('Content-Type'))
    response_message = http_response.read()

    if taxii_content_type is None:
        body = six.ensure_text(response_message, encoding=encoding, errors='replace')
        m = str(http_response) + '\r\n' + str(info) + '\r\n' + body
        return tm11.StatusMessage(message_id='0', in_response_to=in_response_to, status_type=ST_FAILURE, message=m)
    elif taxii_content_type == VID_TAXII_XML_10:  # It's a TAXII XML 1.0 message
        return tm10.get_message_from_xml(response_message, encoding)
    elif taxii_content_type == VID_TAXII_XML_11:  # It's a TAXII XML 1.1 message
        return tm11.get_message_from_xml(response_message, encoding)
    elif taxii_content_type == VID_CERT_EU_JSON_10:
        return tm10.get_message_from_json(response_message, encoding)
    else:
        raise ValueError('Unsupported X-TAXII-Content-Type: %s' % taxii_content_type)


def get_message_from_urllib_addinfourl(http_response, in_response_to):
    """ This function should not be called by libtaxii users directly. """
    info = http_response.info()

    get_header = info.getheader if hasattr(info, 'getheader') else info.get
    taxii_content_type = get_header('X-TAXII-Content-Type')
    encoding = _get_response_encoding(get_header('Content-Type'))
    response_message = http_response.read()

    if taxii_content_type is None:  # Treat it as a Failure Status Message, per the spec

        message = []
        for k, v in info.items():
            message.append(k + ': ' + v + '\r\n')
        message.append('\r\n')
        message.append(six.ensure_text(response_message, encoding=encoding, errors='replace'))

        m = ''.join(message)

        return tm11.StatusMessage(message_id='0', in_response_to=in_response_to, status_type=ST_FAILURE, message=m)

    elif taxii_content_type == VID_TAXII_XML_10:  # It's a TAXII XML 1.0 message
        return tm10.get_message_from_xml(response_message, encoding)
    elif taxii_content_type == VID_TAXII_XML_11:  # It's a TAXII XML 1.1 message
        return tm11.get_message_from_xml(response_message, encoding)
    elif taxii_content_type == VID_CERT_EU_JSON_10:
        return tm10.get_message_from_json(response_message, encoding)
    else:
        raise ValueError('Unsupported X-TAXII-Content-Type: %s' % taxii_content_type)


def get_message_from_httplib_http_response(http_response, in_response_to):
    """ This function should not be called by libtaxii users directly. """
    get_header = http_response.getheader if hasattr(http_response, 'getheader') else http_response.get
    taxii_content_type = get_header('X-TAXII-Content-Type')
    encoding = _get_response_encoding(get_header('Content-Type'))
    response_message = http_response.read()

    if taxii_content_type is None:  # Treat it as a Failure Status Message, per the spec

        message = []
        header_tuples = http_response.getheaders()
        for k, v in header_tuples:
            message.append(k + ': ' + v + '\r\n')
        message.append('\r\n')
        message.append(six.ensure_text(response_message, encoding=encoding, errors='replace'))

        m = ''.join(message)

        return tm11.StatusMessage(message_id='0', in_response_to=in_response_to, status_type=ST_FAILURE, message=m)

    elif taxii_content_type == VID_TAXII_XML_10:  # It's a TAXII XML 1.0 message
        return tm10.get_message_from_xml(response_message, encoding)
    elif taxii_content_type == VID_TAXII_XML_11:  # It's a TAXII XML 1.1 message
        return tm11.get_message_from_xml(response_message, encoding)
    else:
        raise ValueError('Unsupported X-TAXII-Content-Type: %s' % taxii_content_type)

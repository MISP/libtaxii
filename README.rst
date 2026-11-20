libtaxii
========

A Python library for handling `Trusted Automated eXchange of Indicator Information (TAXII™) <https://taxiiproject.github.io/>`_ v1.x Messages and invoking TAXII Services.

:Source: https://github.com/TAXIIProject/libtaxii/
:Documentation: https://libtaxii.readthedocs.io/
:Information: https://taxiiproject.github.io/
:Download: https://pypi.python.org/pypi/libtaxii/

|version badge| |downloads badge|

.. |version badge| image:: https://img.shields.io/pypi/v/libtaxii.svg?maxAge=3600
   :target: https://pypi.python.org/pypi/libtaxii/
.. |downloads badge| image:: https://img.shields.io/pypi/dm/libtaxii.svg?maxAge=3600
   :target: https://pypi.python.org/pypi/libtaxii/

Overview
--------

A primary goal of libtaxii is to remain faithful to both the TAXII
specifications and to customary Python practices. libtaxii is designed to be
intuitive both to Python developers and XML developers.


Installation
------------

The test suite runs on Python 3.10 through 3.14. Use
`uv <https://docs.astral.sh/uv/getting-started/installation/>`_ to create a
virtual environment and install this checkout from the repository root.

.. code-block:: bash

    uv venv --python 3.14
    source .venv/bin/activate
    uv pip install -e .
    python -c "import libtaxii; print(libtaxii.__version__)"
    discovery_client --help

On Windows PowerShell, activate the environment with
``.venv\Scripts\Activate.ps1``. For a published release, use
``uv pip install libtaxii`` or ``python -m pip install libtaxii``.

To install the development tools and run the tests from the checkout:

.. code-block:: bash

    uv pip install -r requirements.txt
    python -m pytest libtaxii

See the `installation guide
<https://libtaxii.readthedocs.io/en/latest/installation.html>`_ for more examples.


Getting Started
---------------

Read the `Getting Started guide
<http://libtaxii.readthedocs.org/en/latest/getting_started.html>`_.


Layout
------

The libtaxii repository has the following layout:

* ``docs/`` - Used to build the `documentation
  <http://libtaxii.readthedocs.org>`_.
* ``libtaxii/`` - The main libtaxii source.
* ``libtaxii/test/`` - libtaxii tests.
* ``libtaxii/xsd/`` - TAXII XML schemas used for validation.


Versioning
----------

Releases of libtaxii are given ``major.minor.revision`` version numbers, where
``major`` and ``minor`` correspond to the TAXII version being supported.  The
``revision`` number is used to indicate new versions of libtaxii.


Feedback
--------

Please provide feedback and/or comments on open issues to taxii@mitre.org.

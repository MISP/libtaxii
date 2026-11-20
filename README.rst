libtaxii
========

A Python library for handling `Trusted Automated eXchange of Indicator Information (TAXII™) <https://taxiiproject.github.io/>`_ v1.x Messages and invoking TAXII Services.

:Source: https://github.com/MISP/libtaxii/
:Upstream: https://github.com/TAXIIProject/libtaxii/
:Documentation: https://misp.github.io/libtaxii/
:Information: https://taxiiproject.github.io/
:Download: https://pypi.org/project/misp-libtaxii/

|version badge| |downloads badge|

.. |version badge| image:: https://img.shields.io/pypi/v/misp-libtaxii.svg?maxAge=3600
   :target: https://pypi.org/project/misp-libtaxii/
.. |downloads badge| image:: https://img.shields.io/pypi/dm/misp-libtaxii.svg?maxAge=3600
   :target: https://pypi.org/project/misp-libtaxii/

Overview
--------

The MISP Project maintains this fork of libtaxii. The MITRE Corporation
developed the original library. See the `MISP Project website
<https://www.misp-project.org/>`_.

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
``uv pip install misp-libtaxii`` or ``python -m pip install misp-libtaxii``.
Python code continues to use ``import libtaxii``.

To install the development tools and run the tests from the checkout:

.. code-block:: bash

    uv pip install -r requirements.txt
    python -m pytest libtaxii

See the `installation guide
<https://misp.github.io/libtaxii/installation.html>`_ for more examples.

Publishing to PyPI
------------------

Before the first release, register a GitHub pending publisher for
``misp-libtaxii`` with owner ``MISP``, repository ``libtaxii``, workflow
``publish.yml`` and environment ``pypi`` in the
`PyPI publishing settings <https://pypi.org/manage/account/publishing/>`_.
Publish a GitHub Release whose tag matches the version in
``libtaxii/version.py``. The workflow builds and uploads the wheel and source
distribution using Trusted Publishing.


Getting Started
---------------

Read the `Getting Started guide
<https://misp.github.io/libtaxii/getting_started.html>`_.


Layout
------

The libtaxii repository has the following layout:

* ``docs/`` - Quarto book and Python API reference.
* ``libtaxii/`` - The main libtaxii source.
* ``libtaxii/test/`` - libtaxii tests.
* ``libtaxii/xsd/`` - TAXII XML schemas used for validation.

Building the documentation
--------------------------

Install `Quarto <https://quarto.org/docs/get-started/>`_ and activate the
development environment described above. Run these commands from the
repository root.

.. code-block:: bash

    python docs/render_api.py
    quarto render docs

The first command generates Quarto chapters from the Python docstrings and
Sphinx API sources. The second builds the book into ``docs/_book/``. Use
``quarto preview docs`` to preview changes locally and ``tox -e docs`` to
check the API examples.

The layout and color palette follow the `MISP Book
<https://github.com/MISP/misp-book/>`_. The documentation workflow builds pull
requests and publishes from ``master`` when the repository's Pages source is
set to **GitHub Actions** under **Settings → Pages**.


Versioning
----------

Releases of libtaxii are given ``major.minor.revision`` version numbers, where
``major`` and ``minor`` correspond to the TAXII version being supported.  The
``revision`` number is used to indicate new versions of libtaxii.


Feedback
--------

Report bugs and share feedback through the `MISP/libtaxii issue tracker
<https://github.com/MISP/libtaxii/issues>`_.

==================
sphinxnotes-strike
==================

.. image:: https://img.shields.io/github/stars/sphinx-notes/strike.svg?style=social&label=Star&maxAge=2592000
  :target: https://github.com/sphinx-notes/strike

:version: |version|
:copyright: Copyright ©2022 by Shengyu Zhang.
:license: BSD, see LICENSE for details.

Sphinx extension for :del:`strikethrough text support`.

.. contents::
   :local:
   :backlinks: none

Installation
============

Download it from official Python Package Index:

.. code-block:: console

   $ pip install sphinxnotes-strike

Add extension to :file:`conf.py` in your sphinx project:

.. code-block:: python

    extensions = [
              # …
              'sphinxnotes.strike',
              # …
              ]

Functionalities
===============

Use role ``strike`` to add text with a strikethrough:

==================== ================
``:strike:`Sphinx``` :strike:`Sphinx`
==================== ================

Role ``del`` also works:

================= =============
``:del:`Sphinx``` :del:`Sphinx`
================= =============

Change Log
==========

2022-08-25 1.2
--------------

- Fallback to text for unsupported builder
- Use inline HTML stylesheet

2022-04-13 1.1
--------------

- Add support for LaTeX builder (#1)

2021-02-11 1.0
--------------

Release 1.0 stable.

2021-02-12 1.0a0
----------------

The alpha version is out, enjoy~

==================
sphinxnotes-strike
==================

----------------------------------------------------
Sphinx extension for HTML strikethrough text support
----------------------------------------------------

.. image:: https://img.shields.io/github/stars/sphinx-notes/strike.svg?style=social&label=Star&maxAge=2592000
   :target: https://github.com/sphinx-notes/strike

:version: |version|
:copyright: Copyright ©2021 by Shengyu Zhang.
:license: BSD, see LICENSE for details.

The extension provides a domain named "any", allows user creates directive
and roles to descibe and reference arbitrary object by writing restructedText
template.

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

Role ``s`` is shortcut of ``strike``:

=============== ==========
``:s:`Sphinx``` :s:`Sphinx`
=============== ==========

Change Log
==========

2021-02-12 1.0a0
----------------

.. sectionauthor:: Shengyu Zhang

The alpha version is out, enjoy~

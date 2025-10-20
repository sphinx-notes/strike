.. This file is generated from sphinx-notes/cookiecutter.
   You need to consider modifying the TEMPLATE or modifying THIS FILE.

==================
sphinxnotes-strike
==================

.. |docs| image:: https://img.shields.io/github/deployments/sphinx-notes/strike/github-pages?label=docs
   :target: https://sphinx.silverrainz.me/strike
   :alt: Documentation Status
.. |license| image:: https://img.shields.io/github/license/sphinx-notes/strike
   :target: https://github.com/sphinx-notes/strike/blob/master/LICENSE
   :alt: Open Source License
.. |pypi| image:: https://img.shields.io/pypi/v/sphinxnotes-strike.svg
   :target: https://pypistats.org/packages/sphinxnotes-strike
   :alt: PyPI Package
.. |download| image:: https://img.shields.io/pypi/dm/sphinxnotes-strike
   :target: https://pypi.python.org/pypi/sphinxnotes-strike
   :alt: PyPI Package Downloads
.. |github| image:: https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white/
   :target: https://github.com/sphinx-notes/strike
   :alt: GitHub Repository

|docs| |license| |pypi| |download| |github|

Introduction
============

.. INTRODUCTION START

An extension that adds :del:`strikethrough text` support to Sphinx.

.. INTRODUCTION END

Getting Started
===============

.. note::

   We assume you already have a Sphinx documentation,
   if not, see `Getting Started with Sphinx`_.


First, downloading extension from PyPI:

.. code-block:: console

   $ pip install sphinxnotes-strike


Then, add the extension name to ``extensions`` configuration item in your
:parsed_literal:`conf.py_`:

.. code-block:: python

   extensions = [
             # …
             'sphinxnotes.strike',
             # …
             ]

.. _Getting Started with Sphinx: https://www.sphinx-doc.org/en/master/usage/quickstart.html
.. _conf.py: https://www.sphinx-doc.org/en/master/usage/configuration.html

.. ADDITIONAL CONTENT START

Use role ``strike`` to add text with a strikethrough:

==================== ================
``:strike:`Sphinx``` :strike:`Sphinx`
==================== ================

Role ``del`` also works:

================= =============
``:del:`Sphinx``` :del:`Sphinx`
================= =============

.. ADDITIONAL CONTENT END

Contents
========

.. toctree::
   :caption: Contents

   changelog

The Sphinx Notes Project
========================

The project is developed by `Shengyu Zhang`__,
as part of **The Sphinx Notes Project**.

.. toctree::
   :caption: The Sphinx Notes Project

   Home <https://sphinx.silverrainz.me/>
   Blog <https://silverrainz.me/blog/category/sphinx.html>
   PyPI <https://pypi.org/search/?q=sphinxnotes>

__ https://github.com/SilverRainZ

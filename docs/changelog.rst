.. This file is generated from sphinx-notes/cookiecutter.
   You need to consider modifying the TEMPLATE or modifying THIS FILE.

==========
Change Log
==========

.. hint:: You may want to learn about our `Release Strategy`__

   __ https://sphinx.silverrainz.me/release.html

.. Example:

   1.0
   ===

   .. version:: _
      :date: yyyy-mm-dd

   Change log here.

2.x
===

.. version:: 2.0

   - fix: Fix typo in warning subtype for unsupported builder (:pull:`16`)
   - BREAKING: Drop all logic about supported builder (:pull:`17`)

1.x
===

.. version:: 1.5
   :date: 2025-11-15

   - fix: :version:`1.4` breaks linkcheck builder and likely other builders
     (:issue:`14`)

.. version:: 1.4
   :date: 2025-11-14

   - fix: Avoid an error which occurred when another extension has already added
     LaTeX packages (:pull:`10`, :pull:`11`)
   - refactor: Builder that supports strike_node does not need to insert
     itself into ``SUPPORTED_BUILDERS`` now (:issue:`12`)

.. version:: 1.3
   :date: 2025-09-26

   - Export a ``SUPPORTED_BUILDERS`` list (:issue:`7`)
   - Add :file:`py.typed` file to ship type hints (:pull:`6`)

.. version:: 1.2
   :date: 2022-08-25 

   - Fallback to text for unsupported builder (:issue:`2`)
   - Use inline HTML stylesheet

.. version:: 1.1
   :date: 2022-04-13 

   - Add support for LaTeX builder (:issue:`1`)

.. version:: 1.0
   :date: 2022-08-25 

   Release 1.0 stable.


.. version:: 1.0a0
   :date: 2021-02-12  

   The alpha version is out, enjoy~

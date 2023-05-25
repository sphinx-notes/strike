.. list-table::
   :align: left

   * - Date
     - :ref:`📅{{ date }} <any-version.date>`
   * - Assets
     - :octicon:`github` Source__, :octicon:`package` Wheel__

__ https://github.com/sphinx-notes/strike/releases/tag/{{ title }}
__ https://pypi.python.org/pypi/sphinxnotes-strike/{{ title }}/#files


{% for line in content %}
{{ line }}
{% endfor %}


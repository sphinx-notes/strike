
{% if style is not defined or style == 'tab' %}
.. tab-set::

   .. tab-item:: Result

      {% for line in content %}{{ line }}
      {% endfor %}

   .. tab-item:: reStructuredText

      .. code:: rst

         {% for line in content %}{{ line }}
         {% endfor %}
{% elif style == 'grid'  %}
.. grid:: 2

   .. grid-item-card::  reStructuredText

      .. code:: rst

         {% for line in content %}{{ line }}
         {% endfor %}

   .. grid-item-card:: Result

      {% for line in content %}{{ line }}
      {% endfor %}
{% endif %}


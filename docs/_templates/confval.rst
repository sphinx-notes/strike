
:Type: :py:class:`{{ type }}`
:Default: ``{{ default }}``
{% if choice %}:Choices: {% for c in choice %}``{{ c }}`` {% endfor %}{% endif %}
{% if versionadded %}:Version added: :version:`{{ versionadded }}`{% endif %}
{% if versionchanged %}:Version changed:{% for i in range(0, versionchanged|count -1, 2)  %}
   :version:`{{ versionchanged[i] }}`
      {{ versionchanged[i+1] }}{% endfor %}{% endif %}

{{ content }}


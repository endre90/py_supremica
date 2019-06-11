{% for item in commands %}
bool got_{{ item }}
{%- endfor %}
{% for item in states %}
bool {{ item }}
{%- endfor %}


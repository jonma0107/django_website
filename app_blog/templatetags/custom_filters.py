from django import template

register = template.Library()

@register.filter(name='format_content')
def format_content(value):
    # Cuenta los saltos de línea y decide el formato
    if value.count('\n') > 2:  # Ajusta este número según tus necesidades
        return f'<pre>{value}</pre>'
    else:
        return f'<p>{value}</p>'

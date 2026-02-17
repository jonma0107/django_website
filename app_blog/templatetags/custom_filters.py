from django import template

register = template.Library()

@register.filter(name='format_content')
def format_content(value):
    if not value:
        return ""
    # Dividimos por saltos de línea dobles para crear párrafos
    paragraphs = value.split('\n\n')
    formatted = ""
    for p in paragraphs:
        content = p.replace("\n", "<br>")
        formatted += f'<p class="blog-paragraph">{content}</p>'
    return formatted

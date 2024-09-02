from django import template

register = template.Library()

@register.filter
def format_number(value):
    if value >= 1000000000:
        return f"{value / 1000000000:.2f}B"
    elif value >= 1000000:
        return f"{value / 1000000:.2f}M"
    elif value >= 1000:
        return f"{value / 1000:.2f}K"
    else:
        return f"{value:.2f}"
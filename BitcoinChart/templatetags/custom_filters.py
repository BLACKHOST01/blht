from django import template

register = template.Library()

@register.filter(name='format_number')
def format_number(value):
    try:
        value = float(value)
        if value >= 1_000_000_000:
            return f'{value/1_000_000_000:.2f}B'
        elif value >= 1_000_000:
            return f'{value/1_000_000:.2f}M'
        elif value >= 1_000:
            return f'{value/1_000:.2f}K'
        else:
            return f'{value:.2f}'
    except (ValueError, TypeError):
        return value  # Return the original value if conversion fails
@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def subtract(value, arg):
    return value - arg

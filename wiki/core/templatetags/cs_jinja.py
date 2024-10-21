from django import template

register = template.Library()

@register.filter
def format_time(arg):
    return str(arg).split(" ")[0]

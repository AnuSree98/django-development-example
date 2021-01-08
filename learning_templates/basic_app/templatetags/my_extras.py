from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,args):
    """
    this cuts all values of 'arg' from the string!

    """
    return value.replace(args," ")

#Custom template filter
from django import template

register = template.Library()

@register.filter(name='cut')
def cuts(value, arg):
    # This cuts out all values of "arg" from the string!

    return value.replace(arg,'')
#First is name for template tag, second is function name
#register.filter('cut',cuts) same as line 6


def lower_1(value):
    return value.lower() + "1"

register.filter('lower_1', lower_1)

def down_2(value, arg):
    return value - arg

register.filter('down_2', down_2)

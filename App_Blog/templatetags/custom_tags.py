# custom_tags.py
from django import template

register = template.Library()



def letter_range(value):
    return value[0:500]+ '...'

register.filter('range_filter',letter_range)
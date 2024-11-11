from django.template.base import Library
from django.template.defaultfilters import timesince_filter
from django.utils import translation

register = Library()

@register.filter
def timesince_it(value, arg=None):
    with translation.override('منـذ'):
        time_since = timesince_filter(value, arg)
    return time_since
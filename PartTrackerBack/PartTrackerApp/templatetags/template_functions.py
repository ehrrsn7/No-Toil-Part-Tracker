from django.utils.safestring import mark_safe
from django import template
import json
register = template.Library()

_status_enum = [ "stamp", "spray", "check", "oil", "bag", ]

@register.filter
def index(indexable, i):
    try:
        return indexable[i]
    except IndexError as e:
        print(e)
        return -1

@register.filter
def key(dictionary, key):
    return dictionary.get(key)

@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))

@register.filter(is_safe=True)
def status_enum(status_int):
    try:
        return _status_enum[status_int].capitalize()
    except IndexError as e:
        print(e)
        return "unknown"

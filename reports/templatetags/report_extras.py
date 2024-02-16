from django import template

register = template.Library()


@register.filter(name="lookup")
def lookup(dict, key):
    print("key:", type(key))
    print("dict:", dict)
    if key in dict:
        return dict[key]
    else: 
        return 0
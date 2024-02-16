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


@register.filter(name="get_total")
def get_total(dict):
    total = sum(dict.values())
    if total >= 0:
        return total
    else:
        return 0
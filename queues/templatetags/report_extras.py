from django import template


register = template.Library()


@register.filter(name="has_reports")
def has_reports(dict):
    return len(dict) != 0


@register.filter(name="lookup")
def lookup(dict, key):
    if key in dict:
        return dict[key]
    else:
        return 0
    
    
@register.filter(name="is_exist")
def is_exist(dict, key):
    if key in dict:
        return True
    else:
        return False
    
    
@register.filter(name="get_total")
def get_total(dict):
    total = sum(dict.values())
    if total >= 0:
        return total
    else:
        return 0
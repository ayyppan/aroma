from django import template

register = template.Library()


@register.filter(name="cut")
def cut(value,arg):
    """
        This will cut the arg from the string given
    """
    return value.replace(arg,'')
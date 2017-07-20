from django import template

register = template.Library()

def beautify(value):
    value = value.replace('-', '/').replace('_', ' ')

    return value

def highlight(value, tags):
    for tag in tags:
        value = value.replace(tag, "<strong>{0}</strong>".format(tag))

    return value

register.filter('beautify', beautify)
register.filter('highlight', highlight)

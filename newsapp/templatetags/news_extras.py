from django import template

register = template.Library()

@register.filter(name='parseDate')
def parseDate(date):
    return date[0:10]
from django import template


register = template.Library()


@register.filter(name='censor')
def censor(value):
    censor_words = ['охуеть', 'блядь', 'наитию']
    for word in censor_words:
        if word[3] == value:
            value = '*****'
        else:
            return value

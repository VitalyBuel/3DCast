from django import template


register = template.Library()


@register.filter()
def censor(value):
    dirty = [
        "лох",
        "TOEFL",
    ]

    for word in dirty:
        value = value.replace(word, '****')
    return value

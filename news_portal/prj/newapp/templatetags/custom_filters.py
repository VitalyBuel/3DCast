from django import template


register = template.Library()


@register.filter(name='censor')
def censor(self):
    stop_list = ['наитию']
    text = self
    for word in stop_list:
        if word in text:
            raise ValueError('Вы позволили себе немного лишнего! Одумайтесь и исправьте текст!')
    return text


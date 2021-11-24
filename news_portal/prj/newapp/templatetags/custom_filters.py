from django import template


register = template.Library()


@register.filter(name='censor')
def censor(value):
    censor_words = ['охуеть', 'блядь', 'наитию']
    fragments = []
    # Проходимся по всем словам.
    for word in censor_words:
        # Разбиваем слово на части, и проходимся по ним.
        for part in range(len(value)):
            fragments.append(part)
    for word in censor_words:
    # Проходимся по всем фрагментам.
        for fragment in fragments:
        # Сравниваем фрагмент и искомое слово
            if word == fragment:
            # Если они равны, выводим надпись о их нахождении.
                return "****"
            else:
                return word

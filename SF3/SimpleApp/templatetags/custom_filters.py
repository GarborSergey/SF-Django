from django import template

register = template.Library()

CURRENCIES_SYMBOLS = {
    'rub': '!',
    'usd': '$',
}

@register.filter()
def currency(value, code='rub'):
    '''
    value: значение, к которому нужно применить фильтр
    '''
    postfix = CURRENCIES_SYMBOLS[code]
    # Возвращаемое функцией знасение подставится в шаблон.
    return f'{value}{postfix}'

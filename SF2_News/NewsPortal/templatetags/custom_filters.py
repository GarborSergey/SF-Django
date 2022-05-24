from django import template

register = template.Library()

stop_words = ['стоп1', 'стоп2', 'стоп3', 'стоп4']

@register.filter()
def text_filter(text):
    filtered_text = ''
    for word in text.split():
        if word.lower() in stop_words:
            filtered_text += word[0] + ('*' * (len(word) - 1)) + ' '
        else:
            filtered_text += word + ' '

    return f'{filtered_text}'




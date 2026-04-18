def capitalize(text):

    if text == '':
        return ''

    first_char = text[0].upper()
    rest_text = text[1:]
    return f'{first_char}{rest_text}'
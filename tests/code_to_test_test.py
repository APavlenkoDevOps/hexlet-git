from code_to_test import capitalize


if capitalize('hello!') != 'Hello!':
    raise Exception ('Функция работает не верно')

if capitalize('') != '':
    raise Exception ('Функция работает не верно')

print('Функция работает верно')
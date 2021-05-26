
ru_kg = {'обезьяна': 'маймыл',
         'корова':'уй',
         'собака':'ит'}

ru_en = {'обезьяна': 'monkey',
         'корова': 'cow',
         'собака': 'dog'}
kg_en = {'акча': 'money',
         'суу': 'water',
         'мышык':'cat'}
en_ru = {'money':'деньги',
         'blue':'синий',
         'error':'ошибка'}
kg_ru = {'акча':'деньги',
         'бак': 'дерево',
         'бала':'ребенок'}
en_kg = {'money': 'акча',
         'white': 'ак',
         'children':'балдар'}
library = [
             'на кыргызском языке',kg_ru, 'на русском языке'] ,\
             ['на кыргызском языке',kg_en, 'English'], \
            ['English', en_kg, 'на кыргызском языке'], \
             ['English', en_ru, 'на русском языке'], \
             ['на русском языке', ru_en, 'English'],\
             ['на русском языке', ru_kg, 'на кыргызском языке']
while True:
    zapros = input('Введите слово для перевода :')
    zaprosdude = False
    for i in library:
        for key in i[1]:
            if key == zapros:
                zaprosdude = True
                print("Язык оригинал: " + i[0])
                print("Язык перевода: " + i[2] + '  - '+ i[1][key] )
    if zaprosdude == False:
        print('Такого слова нет в словаре')
        action = input('Хотите ввести новое слово словарь? Y/N ')
        if action.lower() == 'y':
            language = input('Выберите оригинал слова kg, eng,ru    ')
            if language == 'kg':
                kg_ru[zapros] = input(f'Введите перевод к слову {zapros} на русском языке ')
                kg_en[zapros] = input(f'Введите перевод к слову {zapros} на английском языке ')
            elif language == 'ru':
                ru_en[zapros] = input(f'Введите перевод  к слову {zapros} на английском языке ')
                ru_kg[zapros] = input(f'Введите перевод к слову {zapros} на кыргызском языке ')
            elif language == 'eng':
                en_ru[zapros] = input(f'Введите перевод к слову {zapros} на русском языке ')
                en_kg[zapros] = input(f'Введите перевод к слову {zapros} на кыргызском языке ')

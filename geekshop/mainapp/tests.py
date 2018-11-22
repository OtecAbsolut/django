from django.test import TestCase
import json
import os

# Create your tests here.

# подгружаем данные из json объекта
file = open('db_json.json', encoding='utf-8')
db_json = json.load(file)
file.close()

# Ищем в словаре данные для menu, product_menu и.т.д.
for element in db_json:
    for key, value in element.items():
        if key == 'menu':
            menu = value
        if  key == 'product_menu':
            product_menu = value

content = {
        'menu': menu,
        'product_menu': product_menu,
}


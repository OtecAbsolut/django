from django.shortcuts import render
import json
import os

# подгружаем данные из json объекта
def json_base():
    if os.path.isfile('db_json.json'):
        file = open('db_json.json', encoding='utf-8')
        db_json = json.load(file)
        file.close()
        return db_json

# Ищем в словаре данные для menu, product_menu и.т.д.
def search_content(db):
    for element in db:
        for key, value in element.items():
            if key == 'menu':
                menu = value
            if key == 'product_menu':
                product_menu = value
            if key == 'title':
                title = value
    content = {
        'menu': menu,
        'product_menu': product_menu,
        'title': title
    }
    return content


# Create your views here.
def main(request):
    title = 'ГЛАВНАЯ'
    db = json_base()
    content = search_content(db)
    return render(request, 'mainapp/index.html', content)

def products(request):
    title = 'ПРОДУКТЫ'
    db = json_base()
    content = search_content(db)
    return render(request, 'mainapp/products.html', content)

def contact(request):
    title = 'КОНТАКТЫ'
    db = json_base()
    content = search_content(db)
    return render(request, 'mainapp/contact.html', content)





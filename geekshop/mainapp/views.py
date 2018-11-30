from django.shortcuts import render
import json
import os
import random
from .models import ProductCategory, Product
#
# # подгружаем данные из json объекта
# def json_base():
#     if os.path.isfile('db_json.json'):
#         file = open('db_json.json', encoding='utf-8')
#         db_json = json.load(file)
#         file.close()
#         return db_json

# Ищем в словаре данные для menu, product_menu и.т.д.
def search_content():
    menu = [{"href": "main", "name": "домой"},
            {"href": "products:index", "name": "продукты"},
            {"href": "contact", "name": "контакты"}]
    return menu


# Create your views here.
def main(request):
    title = 'ГЛАВНАЯ'
    products = Product.objects.all()[:4]
    menu = search_content()
    content = {
        'menu': menu,
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)

def products(request, pk = None):
    title = 'ПРОДУКТЫ'
    menu = search_content()
    category = ProductCategory.objects.all()
    products = Product.objects.all()
    r = random.randint(0, 3)
    rand = Product.objects.all()[r]
    content = {
        'menu': menu,
        'title': title,
        'products': products,
        'category': category,
        'rand': rand
    }
    return render(request, 'mainapp/products.html', content)

def contact(request):
    title = 'КОНТАКТЫ'
    menu = search_content()

    content = {
        'menu': menu,
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/contact.html', content)





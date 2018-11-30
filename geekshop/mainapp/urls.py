from django.conf.urls import url
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    url('', mainapp.products, name='index'),
    url(r'^(\d+)/', mainapp.products, name = 'category'),
]

from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='название категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.CharField(verbose_name='цена', max_length=64, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    image570 = models.ImageField(upload_to='product_images', blank=True)
    image370 = models.ImageField(upload_to='product_images', blank=True)
    image270 = models.ImageField(upload_to='product_images', blank=True)
    image70 = models.ImageField(upload_to='product_images', blank=True)
    image570_2 = models.ImageField(upload_to='product_images', blank=True)
    image70_2 = models.ImageField(upload_to='product_images', blank=True)
    image570_3 = models.ImageField(upload_to='product_images', blank=True)
    image70_3 = models.ImageField(upload_to='product_images', blank=True)

    def __str__(self):
        return f'{self.name}({self.category.name})'

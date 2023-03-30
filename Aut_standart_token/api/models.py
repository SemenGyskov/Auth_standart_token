from django.db import models

class Producer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование производителя')
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование страны')
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    producer = models.ManyToManyField(Producer, verbose_name='Производитель')
    country = models.ManyToManyField(Country, verbose_name='Страна')
    new = models.BooleanField(default=False, verbose_name='новинка?')
    cost = models.IntegerField(default=0, verbose_name='Стоимость')
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Cart(models.Model):
    products = models.ManyToManyField(Product, verbose_name='Продукт')
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
class Order(models.Model):
    num = models.IntegerField(default=0, verbose_name='Номер заказа')
    cost = models.IntegerField(default=0, verbose_name='Общая Стоимость')
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
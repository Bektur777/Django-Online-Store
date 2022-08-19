from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from store.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, related_name='Заказы', on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField()
    address = models.CharField('Адрес', max_length=255)
    city = models.CharField('Город', max_length=50)
    phone = models.IntegerField('Номер телефона')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='Заказ', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='Товар', on_delete=models.CASCADE)
    price = models.IntegerField('Цена')
    quantity = models.IntegerField('Количество', default=1)


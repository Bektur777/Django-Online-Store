from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категория"""
    name = models.CharField('Категория', max_length=50)
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Manufacture(models.Model):
    name = models.CharField('Производитель', max_length=50)
    description = models.TextField('Описание')
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class OperatingSystem(models.Model):
    name = models.CharField('Операционная система', max_length=50)
    description = models.TextField('Описание')
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'


class Memory(models.Model):
    name = models.CharField('Память', max_length=50, help_text='пример для ввода "4GB/64GB"')
    description = models.TextField('Описание')
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Память'
        verbose_name_plural = 'Память'


class Cpu(models.Model):
    name = models.CharField('Процессор', max_length=50)
    description = models.TextField('Описание')
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'


class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена', default=0, help_text='указывать сумму в сомах')
    manufacture = models.ForeignKey(Manufacture, verbose_name='Производитель', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    operating_system = models.ForeignKey(OperatingSystem, verbose_name='Операционная система', on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, verbose_name='Память', on_delete=models.CASCADE)
    cpu = models.ForeignKey(Cpu, verbose_name='Процессор', on_delete=models.CASCADE)
    poster = models.ImageField('Постер', upload_to='product/')
    year = models.PositiveSmallIntegerField('Год выхода', default=2022)
    premier = models.DateField('Дата выхода', default=date.today)
    slug = models.SlugField(max_length=60, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductPictures(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'



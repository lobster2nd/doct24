from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='URL')
    image = models.ImageField(verbose_name='Изображение')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='URL')
    image = models.ImageField(verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='subcategories',
                                 verbose_name='Категория')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(AbstractUser):

    def __str__(self):
        return self.username


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

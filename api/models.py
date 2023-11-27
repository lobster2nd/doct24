import os

from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='URL')
    image = models.ImageField(upload_to='media/category_images',
                              verbose_name='Изображение')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='URL')
    image = models.ImageField(upload_to='media/subcategory_images',
                              verbose_name='Изображение')
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
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='URL')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена', default=0)
    image = models.ImageField(upload_to='media/product_images',
                              verbose_name='Фото')
    cat = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                            verbose_name='Название продукта',
                            related_name='product')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # Определение пути и имени файла без расширения
            file_path, file_extension = os.path.splitext(self.image.path)
            file_name = os.path.basename(file_path)

            # Сохранение исходного изображения с суффиксом "original"
            img_original_path = f'{file_path}_original{file_extension}'
            img.save(img_original_path)

            # Создание и сохранение изображения в маленьком размере
            img_small = img.resize((100, 100))
            img_small_path = f'{file_path}_small{file_extension}'
            img_small.save(img_small_path)

            # Создание и сохранение изображения в большом размере
            img_large = img.resize((500, 500))
            img_large_path = f'{file_path}_large{file_extension}'
            img_large.save(img_large_path)

            # Удаление исходного файла
            os.remove(self.image.path)

            # Обновление поля изображения на измененные версии
            self.image = File(open(img_original_path, 'rb'))
            self.image_small = File(open(img_small_path, 'rb'))
            self.image_large = File(open(img_large_path, 'rb'))


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

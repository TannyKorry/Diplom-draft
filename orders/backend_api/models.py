from django.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='Название')
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = "Список магазинов"
        ordering = ['-name']

    def __str__(self):
        return f'{self.name}'



class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = 'Категория'
        ordering = ['-name']

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=False)


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Список продуктов"
        ordering = ['-name']

    def __str__(self):
        return f'{self.category} {self.name}'





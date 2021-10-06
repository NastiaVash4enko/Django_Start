from django.db import models
from django.db import models
from django.core.validators import MinValueValidator


# Создаем модель товара
class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,  # газвание не должно повтряться
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',  # все продукты в категории будут доступны через поле Products
    )
    price = models.FloatField(
        validators=[MinValueValidator],
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


# создаем катнгорию к которой будет привязываться товар

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,  # название не должны повторяться
    )

    def __str__(self):
        return f'{self.name.titile()}'
from django.db import models
from simple_history.models import HistoricalRecords


class SFC(models.Model):
    
    fats = models.FloatField(verbose_name='Жиры')
    carbohydrates = models.FloatField(verbose_name='Углеводы')
    proteins = models.FloatField(verbose_name='Белки')

    history = HistoricalRecords()

    def __str__(self):
        return f'{self. proteins} {self.fats} {self.carbohydrates}'

    class Meta:
        verbose_name = 'БЖУ'
        verbose_name_plural = 'БЖУ'


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name
    
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Recipe(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    creator = models.CharField(verbose_name='Автор', max_length=255)
    category = models.ManyToManyField(Category, verbose_name='Категории')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    calories = models.ForeignKey(SFC, verbose_name='Калории', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст рецепта')

    history = HistoricalRecords()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Users(models.Model):
    nickname = models.CharField(verbose_name='Имя пользователя', max_length=255)
    mail = models.CharField(verbose_name='Почта', max_length=255)
    reviews = models.IntegerField(verbose_name='Количество одобрений')
    dishes = models.IntegerField(verbose_name='Рецептов')

    history = HistoricalRecords()

    def __str__(self):
        return self.nickname


    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


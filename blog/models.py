from core.abstract_models import Abstract
from core.validators import check_phonenum
from django.db import models
from django_countries import Countries
from django_countries.fields import CountryField

# Create your models here.
class Bloger(Abstract):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    location = CountryField()
    email = models.EmailField()
    phone = models.CharField(
        max_length=13,
        validators=[check_phonenum]
    )

    class Meta:
        ordering = ['second_name']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.second_name


class Blog(Abstract):
    title = models.CharField(max_length=255)
    content = models.TextField()
    comments = models.TextField(blank=True)
    bloger = models.ForeignKey(
        Bloger,
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

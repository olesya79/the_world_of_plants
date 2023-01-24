from core.abstract_models import Abstract
from core.enums.garden_center_enums import Currency
from core.enums.garden_center_enums import StatusOfPlant
from core.validators import check_phonenum
from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Plant(Abstract):
    title = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)
    propagation = models.TextField(blank=True)
    grows = CountryField()
    price = models.IntegerField(default=1000)
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.RUB
    )

    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
    )

    status = models.CharField(
        max_length=255,
        choices=StatusOfPlant.choices,
        default=StatusOfPlant.Available
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

    def __str__(self):
        return self.title


class Category(Abstract):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Garden_center(Abstract):
    title = models.CharField(max_length=255)
    content = models.TextField()
    location = CountryField()
    contact = models.EmailField()
    plants = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Садовый центр'
        verbose_name_plural = 'Садовые центры'

    def __str__(self):
        return self.title


class Founder(Abstract):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    age = models.IntegerField()
    contact = models.EmailField()
    phone = models.CharField(
        max_length=13,
        validators=[check_phonenum]
    )
    garden_center = models.ForeignKey(
        Garden_center,
        on_delete=models.PROTECT
    )

    class Meta:
        ordering = ['second_name']
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'

    def __str__(self):
        return self.name

from core.abstract_models import Abstract
from core.enums.purchaser_enums import SexOfPurchaser
from core.validators import check_phonenum
from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Purchaser(Abstract):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255, blank=True)
    sex = models.CharField(
        max_length=6,
        choices=SexOfPurchaser.choices,
        default=SexOfPurchaser.Female
    )

    age = models.IntegerField()
    location = CountryField()
    email = models.EmailField()
    phone = models.CharField(
        max_length=13,
        validators=[check_phonenum]
    )

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.first_name


class Balance(Abstract):
    value = models.DecimalField(max_digits=5, decimal_places=2)
    purchaser = models.ForeignKey(
        Purchaser,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['value']
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'

    def __str__(self):
        return self.purchaser

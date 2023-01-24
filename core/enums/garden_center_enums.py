from django.db import models

class Currency(models.TextChoices):
    EUR = 'EUR', 'EUR'
    USD = 'USD', 'USD'
    RUB = 'RUB', 'RUB'


class StatusOfPlant(models.TextChoices):
    Available = 'Available', 'Available'
    Out_of_stock = 'Out_of_stock', 'Out_of_stock'


class Category(models.TextChoices):
    Garden_plants = 'Garden', 'Garden'
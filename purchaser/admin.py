from purchaser.models import Purchaser, Balance
from django.contrib import admin
from django.db.models import QuerySet


# Register your models here.


@admin.register(Purchaser)
class PurchaserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'sex', 'age', 'location', 'email', 'phone']
    ordering = ['first_name']
    search_fields = ['first_name__istartwith']


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['value']
    ordering = ['value']





from garden_center.models import Plant, Category, Founder, Garden_center
from django.contrib import admin
from django.db.models import QuerySet


# Register your models here.


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['title', 'kind', 'propagation', 'price', 'currency']
    ordering = ['title']
    search_fields = ['title__istartwith']
    actions = ['change_to_rub']

    @admin.action(description='Изменить валюту выбранных элементов на рубли')
    def change_to_rub(self, request, qs: QuerySet):
        update_plants = qs.update(currency=Currency.RUB)
        self.message_user(
            request,
            f'Обновлено {update_cars} записей',
            messages.SUCCES
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
    search_fields = ['title__istartwith']
    actions = ['fruit_plants']

    @admin.action(description='Изменить категорию элементов на плодовые растения')
    def fruit_plants(self, request, qs: QuerySet):
        update_plants = qs.update(fruit_plants=Category.Fruit_plants)
        self.message_user(
            request,
            f'Обновлено {update_cars} записей',
            messages.SUCCES
        )


@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'age', 'contact', 'phone']
    ordering = ['second_name']
    search_fields = ['second_name']


@admin.register(Garden_center)
class Garden_centerAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'contact']
    ordering = ['title']
    search_fields = ['title']
    actions = ['passenger_car']




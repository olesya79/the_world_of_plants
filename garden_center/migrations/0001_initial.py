# Generated by Django 4.1.3 on 2023-01-24 17:41

import core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('kind', models.CharField(max_length=255)),
                ('propagation', models.TextField(blank=True)),
                ('grows', django_countries.fields.CountryField(max_length=2)),
                ('price', models.IntegerField(default=1000)),
                ('currency', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD'), ('RUB', 'RUB')], default='RUB', max_length=3)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Out_of_stock', 'Out_of_stock')], default='Available', max_length=255)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='garden_center.category')),
            ],
            options={
                'verbose_name': 'Растение',
                'verbose_name_plural': 'Растения',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Garden_center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('contact', models.EmailField(max_length=254)),
                ('plants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_center.plant')),
            ],
            options={
                'verbose_name': 'Садовый центр',
                'verbose_name_plural': 'Садовые центры',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('contact', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13, validators=[core.validators.check_phonenum])),
                ('garden_center', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='garden_center.garden_center')),
            ],
            options={
                'verbose_name': 'Основатель',
                'verbose_name_plural': 'Основатели',
                'ordering': ['second_name'],
            },
        ),
    ]

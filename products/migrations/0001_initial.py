# Generated by Django 4.2.6 on 2023-10-24 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, unique=True, verbose_name='Наименование')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Фирма',
                'verbose_name_plural': 'Фирмы',
            },
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doors', to='products.organization', verbose_name='Фирма')),
            ],
            options={
                'verbose_name': 'Дверь',
                'verbose_name_plural': 'Двери',
            },
        ),
    ]
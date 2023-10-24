# Generated by Django 4.2.6 on 2023-10-24 09:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'doors',
                    models.ManyToManyField(
                        blank=True,
                        related_name='doors',
                        related_query_name='door',
                        to='products.door',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'password',
                    models.CharField(max_length=128, verbose_name='password'),
                ),
                (
                    'last_login',
                    models.DateTimeField(
                        blank=True, null=True, verbose_name='last login'
                    ),
                ),
                (
                    'is_superuser',
                    models.BooleanField(
                        default=False,
                        help_text='Designates that this user has all permissions without explicitly assigning them.',
                        verbose_name='superuser status',
                    ),
                ),
                (
                    'first_name',
                    models.CharField(
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile('^[A-Za-zА-Яа-яёЁ -]{1,51}$'),
                                message='Для ввода доступны только латинские символы, кириллица, пробел, дефис.',
                            )
                        ],
                        verbose_name='Имя',
                    ),
                ),
                (
                    'last_name',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile('^[A-Za-zА-Яа-яёЁ -]{1,51}$'),
                                message='Для ввода доступны только латинские символы, кириллица, пробел, дефис.',
                            )
                        ],
                        verbose_name='Фамилия',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        db_index=True,
                        error_messages={
                            'unique': 'Пользователь с таким адресом электронной почты уже зарегистрирован.'
                        },
                        max_length=255,
                        unique=True,
                        verbose_name='Адрес электронной почты',
                    ),
                ),
                (
                    'phone',
                    models.CharField(
                        blank=True,
                        help_text='Не обязательно',
                        max_length=15,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message='Укажите корректный номер в формате +7XXXXXXXXXX',
                                regex='^(\\+7)(\\d{10})$',
                            )
                        ],
                        verbose_name='Телефон',
                    ),
                ),
                (
                    'is_active',
                    models.BooleanField(
                        default=False,
                        help_text='Активен ли пользователь (пройдена ли активация через email)',
                        verbose_name='Активен',
                    ),
                ),
                (
                    'basket',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='user',
                        to='accounts.basket',
                    ),
                ),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.group',
                        verbose_name='groups',
                    ),
                ),
                (
                    'user_permissions',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Specific permissions for this user.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.permission',
                        verbose_name='user permissions',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-03 16:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_alter_user_managers_user_date_joined_user_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='basket',
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
    ]

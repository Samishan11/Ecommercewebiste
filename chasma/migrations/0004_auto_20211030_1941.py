# Generated by Django 3.1.6 on 2021-10-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chasma', '0003_auto_20211027_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]

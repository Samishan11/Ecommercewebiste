# Generated by Django 3.1.6 on 2021-11-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chasma', '0009_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.CharField(choices=[('Sunglass', 'Sunglass'), ('Frame', 'Frame'), ('Eyelens', 'Eyelens'), ('Male', 'Male'), ('Female', 'Female')], max_length=12),
        ),
    ]
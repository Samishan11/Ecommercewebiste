# Generated by Django 3.1.6 on 2021-11-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chasma', '0008_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

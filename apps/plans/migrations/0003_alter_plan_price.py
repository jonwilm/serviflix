# Generated by Django 3.2.15 on 2022-10-25 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_auto_20221024_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='price',
            field=models.FloatField(default=0, verbose_name='Precio del plan'),
        ),
    ]

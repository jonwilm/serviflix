# Generated by Django 3.2.15 on 2022-10-29 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_service_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección'),
        ),
    ]

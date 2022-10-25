# Generated by Django 3.2.15 on 2022-10-24 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20221024_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymethod', models.CharField(max_length=50, verbose_name='Metodo de Pago')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='Servicio')),
            ],
            options={
                'verbose_name': 'Metodo de Pago',
                'verbose_name_plural': 'Metodos de Pagos',
            },
        ),
    ]

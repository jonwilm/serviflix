# Generated by Django 3.2.15 on 2022-10-25 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_alter_plan_price'),
        ('services', '0012_alter_paymentmethods_paymethod'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='cuota',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='plans.timediscount', verbose_name='Cuota'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='plan',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='plans.plan', verbose_name='Plan'),
            preserve_default=False,
        ),
    ]

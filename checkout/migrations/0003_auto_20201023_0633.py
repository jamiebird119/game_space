# Generated by Django 3.1.2 on 2020-10-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20201021_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='original_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

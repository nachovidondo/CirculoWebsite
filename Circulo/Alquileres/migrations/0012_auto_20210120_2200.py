# Generated by Django 3.1.3 on 2021-01-21 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquileres', '0011_auto_20210120_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postalquiler',
            name='dormitorios',
            field=models.IntegerField(verbose_name='Dormitorios'),
        ),
    ]

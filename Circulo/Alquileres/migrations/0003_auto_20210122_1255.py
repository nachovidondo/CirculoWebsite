# Generated by Django 3.1.3 on 2021-01-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquileres', '0002_auto_20210122_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postalquiler',
            name='plantas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Plantas (locales u oficinas)'),
        ),
        migrations.AlterField(
            model_name='postalquiler',
            name='superficie',
            field=models.IntegerField(blank=True, verbose_name='Superficie (locales u oficinas)'),
        ),
    ]

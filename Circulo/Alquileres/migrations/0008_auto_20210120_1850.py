# Generated by Django 3.1.3 on 2021-01-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquileres', '0007_auto_20210120_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postalquiler',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='Alquileres', verbose_name='Imagen'),
        ),
    ]

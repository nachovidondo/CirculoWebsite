# Generated by Django 3.1.3 on 2021-06-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_postinicio_moneda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimagenes',
            name='image',
            field=models.ImageField(upload_to='Inicio', verbose_name='Imagenes'),
        ),
    ]

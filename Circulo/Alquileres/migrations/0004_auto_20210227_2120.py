# Generated by Django 3.1.3 on 2021-02-28 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquileres', '0003_auto_20210227_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postalquiler',
            name='balcon',
            field=models.CharField(choices=[('Con Balcon', 'Con Balcon'), ('', '')], default='Con Balcon', max_length=100),
        ),
    ]

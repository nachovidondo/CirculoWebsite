# Generated by Django 3.1.3 on 2021-02-28 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0002_auto_20210207_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='balcon',
            field=models.CharField(choices=[('Con Balcon', 'Con Balcon'), ('Sin Balcon', 'Sin Balcon')], default='Con Balcon', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='frente',
            field=models.CharField(choices=[('Externo', 'Externo'), ('Contrafrente', 'Contrafrente')], default='Externo', max_length=100),
        ),
    ]

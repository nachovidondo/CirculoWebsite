# Generated by Django 3.1.3 on 2021-02-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_auto_20210122_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postinicio',
            name='content',
            field=models.TextField(max_length=200, verbose_name='Contenido'),
        ),
    ]

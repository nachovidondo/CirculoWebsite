# Generated by Django 3.1.3 on 2021-02-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0006_auto_20210204_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postinicio',
            name='content',
            field=models.TextField(max_length=400, verbose_name='Contenido'),
        ),
    ]

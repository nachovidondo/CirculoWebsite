# Generated by Django 3.1.3 on 2021-02-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0003_auto_20210227_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='superficie',
            field=models.FloatField(blank=True, null=True, verbose_name='Superficie'),
        ),
    ]

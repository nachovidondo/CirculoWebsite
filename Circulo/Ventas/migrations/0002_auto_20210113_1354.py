# Generated by Django 3.1.3 on 2021-01-13 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.CreateModel(
            name='PostImagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Imagenes', verbose_name='Imagenes')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Ventas.post')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-16 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='img',
            field=models.ImageField(default='static/img/indisponivel.jpg', upload_to=''),
        ),
    ]
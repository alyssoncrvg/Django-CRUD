# Generated by Django 4.0.3 on 2022-05-16 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_carro_img_alter_carro_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='img',
            field=models.ImageField(default='static/img/indisponivel.jpg', upload_to='img'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-18 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_carro_data_cadastro_alter_carro_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='img',
            field=models.ImageField(default='images/indisponivel.png', upload_to='images/'),
        ),
    ]

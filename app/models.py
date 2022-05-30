from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.datetime_safe import datetime

class carro(models.Model):
    img = models.ImageField(upload_to = 'images/', default='images/indisponivel.png')
    modelo = models.CharField(max_length=50, null=False)
    marca = models.CharField(max_length=50, null=False)
    ano = models.PositiveIntegerField(validators=[MinValueValidator(2000)], null=False)
    valor = models.FloatField(null=False)
    data_cadastro = models.DateTimeField(default=datetime.now(), null=False)
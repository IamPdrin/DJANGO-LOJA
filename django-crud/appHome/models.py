from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)
    quantidade = models.IntegerField(default = 0)
    foto = models.ImageField(upload_to='imagens/', null=True, blank=True)

class Login(models.Model):
    usuario = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=16)


    
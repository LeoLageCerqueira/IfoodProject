from django.db import models

class Restaurante(models.Model):
    nome_restaurante = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    tipo_culinaria = models.CharField(max_length=50)

class Prato(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nome_prato = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    tipo_prato = models.CharField(max_length=100)

class Pedido(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    cliente = models.OneToOneField('Cliente', on_delete=models.CASCADE)
    pratos = models.ManyToManyField(Prato)
    entregador = models.ForeignKey('Entregador', on_delete=models.SET_NULL, blank=True, null=True)
    d_entra = models.DateTimeField(auto_now_add=True)
    d_saida = models.DateTimeField(blank=True, null=True)

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    cpf = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Entregador(models.Model):
    nome_entregador = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
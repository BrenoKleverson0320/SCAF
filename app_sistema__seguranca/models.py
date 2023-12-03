
from django.db import models

# class Aluno(models.Model):
#     nome = models.CharField(max_length=100)
#     email = models.EmailField()
#     endereco = models.CharField(max_length=200)
#     telefone = models.CharField(max_length=15)
#     foto = models.ImageField(upload_to='Alunos/')

# class Funcionario(models.Model):
#     nome = models.CharField(max_length=100)
#     email = models.EmailField()
#     endereco = models.CharField(max_length=200)
#     telefone = models.CharField(max_length=15)
#     foto = models.ImageField(upload_to='Funcionarios/')

# class Bloqueado(models.Model):
#     nome = models.CharField(max_length=100)
#     email = models.EmailField()
#     endereco = models.CharField(max_length=255)
#     telefone = models.CharField(max_length=20)
#     descricao = models.TextField()

# class FotoBloqueado(models.Model):
#     bloqueado = models.ForeignKey(Bloqueado, on_delete=models.CASCADE)
#     foto = models.ImageField(upload_to='Bloqueado/')



class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)

class Bloqueado(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    descricao = models.TextField()
    
class FotoBloqueado(models.Model):
    bloqueado = models.ForeignKey(Bloqueado, on_delete=models.CASCADE)
    foto = models.ImageField()
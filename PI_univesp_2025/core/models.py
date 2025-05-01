from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Matricula(models.Model):
     nome_completo = models.CharField(max_length=100)
     idade = models.IntegerField()
     instrumento = models.CharField()
     email = models.EmailField()
     telefone = models.CharField()
     observacao = models.TextField()
     instrutor =models.ForeignKey(User, on_delete=models.CASCADE)
     
     class Meta:
        db_table = 'matricula'

     def __str__(self):
        return self.nome_completo
    
class agendamento_de_aula(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data_agendamento = models.DateField(verbose_name= 'Data do agendamento')
    hora = models.TimeField()
    instrutor =models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'agendamento_de_aula'

    def __str__(self):
        return self.nome
    

class deletarAgendamento(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField()
    data_agendamento = models.DateField(verbose_name= 'Data do agendamento')
    hora = models.TimeField()
    instrutor =models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'deletarAgendamento'

    def __str__(self):
        return self.nome
    
    



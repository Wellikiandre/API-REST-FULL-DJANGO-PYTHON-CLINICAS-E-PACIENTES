from django.db import models

# Create your models here.

class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_nasc = models.DateTimeField(blank=True, null=True)
    endereco = models.CharField(max_length=80,blank=True, null=True)
    num_endereco = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=60,blank=True, null=True)
    cep = models.IntegerField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    cpf_cnpj = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'pacientes'
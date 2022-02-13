from msilib.schema import Class
from django.db import models
from django.forms import DateTimeField
from pacientes.models import Pacientes

# Create your models here.

class Agendamentos(mode.Model):
    id_agendamento = models.AutoField(primary_key=True)
    data_hora = models.DateTimeField(blank=False, null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    cancelado = models.BooleanField(default=False)
    obs = models.TextField(blank=True,null=True)
    tipo = models.CharField(max_length=100, blnk=True, null=True)
    id_pacientes = models.ForeignKey(Pacientes,on_delete=models.CASCADE, related_name='agendamentos', blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'agendamentos'
        unique_together =  ('data_hora','id_paciente')

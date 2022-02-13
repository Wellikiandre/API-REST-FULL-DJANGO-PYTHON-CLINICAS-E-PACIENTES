from pyexpat import model

from attr import fields
from rest_framework import serializers
from pacientes.models import Pacientes

class PacientesSerializers(serializers.MOdelSerializers):
    class Meta:
        model = Pacientes
        fields = '__all__'
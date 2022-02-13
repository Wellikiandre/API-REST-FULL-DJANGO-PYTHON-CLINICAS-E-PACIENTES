from rest_framework import serializers
from agendamentos.models import Agendamentos

class AgendamentosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = '__all__'
        
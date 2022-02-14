from rest_framework import serializers

from pacientes.models import Pacientes
from agendamentos.api.serializers import AgendamentosDetalhesSerializer

class PacientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'

class PacientesDetalhesSerializers(serializers.ModelSerializer):
    agendamentos = AgendamentosDetalhesSerializer(many=True, read_only=True)

    class Meta:
        model = Pacientes
        fields = [
            'id_paciente',
            'nome',
            'data_nasc',
            'endereco',
            'num_endereco',
            'bairro',
            'cep',
            'data_cadastro',
            'cpf_cnpj',
            'agendamentos'
        ]
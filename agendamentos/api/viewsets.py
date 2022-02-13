from rest_framework import viewsets
from agendamentos.models import Agendamentos
from agendamentos.api.serializers import AgendamentosSerializers


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all().order_by('data_hora')
    serializer_class = AgendamentosSerializers

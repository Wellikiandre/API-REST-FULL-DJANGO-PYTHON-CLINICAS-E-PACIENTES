
from rest_framework import serializers

from historicos.models import Historicos

class HistoricosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Historicos
        fields = '__all__'
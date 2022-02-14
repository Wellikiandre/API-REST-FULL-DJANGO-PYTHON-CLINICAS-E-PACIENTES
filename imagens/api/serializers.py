from dataclasses import fields
from rest_framework import serializers
from imagens.models import ImagensHistorico

class ImagensHistoricoSerializer(serializers.ModelSerializer):
    model = ImagensHistorico
    fields = '__all__'
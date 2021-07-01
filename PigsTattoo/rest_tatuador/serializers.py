from rest_framework import serializers
from core.models import Tatuador

class TatuadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tatuador
        fields= '__all__'
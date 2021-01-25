from rest_framework import serializers
from .models import Server

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('__all__')

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('name',)

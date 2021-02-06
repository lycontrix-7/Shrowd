from rest_framework import serializers
from .models import PublicServer, PrivateServer
from django.contrib.auth.models import User

class PublicServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicServer
        fields = ('__all__')

class PrivateServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateServer
        fields = ('__all__')
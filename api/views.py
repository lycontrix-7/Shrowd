from django.shortcuts import render
from rest_framework import generics, status
from .models import Server
from .serializers import ServerSerializer, CreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ServerView(generics.ListAPIView):
	queryset = Server.objects.all()
	serializer_class = ServerSerializer

class CreateView(APIView):
	serializer_class = CreateSerializer

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			queryset = Server.objects.filter(name=name)
			if not queryset.exists():
				server = Server(name=name)
				server.save()
				return Response(ServerSerializer(server).data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
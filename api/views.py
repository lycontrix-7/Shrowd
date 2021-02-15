from django.shortcuts import render
from rest_framework import generics, status
from .models import PublicServer, PrivateServer
from .serializers import PublicServerSerializer, PrivateServerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class PublicServerView(generics.ListAPIView):
	queryset = PublicServer.objects.all()
	serializer_class = PublicServerSerializer

class PublicCreateView(APIView):
	serializer_class = PublicServerSerializer

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			queryset = PublicServer.objects.filter(name=name)
			if not queryset.exists():
				server = PublicServer(name=name)
				server.save()
				return Response(PublicServerSerializer(server).data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublicJoinView(APIView):
	def post(self, request, format=None):
		name = request.data.get('name')
		if name != None:
			name_result = PublicServer.objects.filter(name=name)
			if len(name_result) > 0:
				server = name_result[0]
				return Response({'message': 'Server Joined!'}, status=status.HTTP_200_OK)
			return Response({'Bad Request': 'Invalid Room Code'}, status=status.HTTP_400_BAD_REQUEST)
		return Response({'Bad Request': 'Invalid post data, did not find a server key'}, status=status.HTTP_400_BAD_REQUEST)



class PrivateServerView(generics.ListAPIView):
	queryset = PrivateServer.objects.all()
	serializer_class = PrivateServerSerializer

class PrivateCreateView(APIView):

	def post(self, request, format=None):
		serializer = PrivateServerSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			password = serializer.data.get('password')
			queryset = PrivateServer.objects.filter(name=name)			
			if not queryset.exists():	
				server = PrivateServer(name=name, password=password)
				server.save()
				return Response(PrivateServerSerializer(server).data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrivateJoinView(APIView):

	def post(self, request, format=None):
		
		name = request.data.get('name')
		password = request.data.get('password')
		if name != None:
			queryset = PrivateServer.objects.filter(name=name).first()
			if queryset:
				if queryset.password == password:
					return Response({'message': 'Server Joined!'}, status=status.HTTP_200_OK)
				return Response({'Wrong Password': 'Cannot join wrong password'}, status=status.HTTP_401_UNAUTHORIZED) 
			return Response({'Bad Request': 'Invalid Server Name'}, status=status.HTTP_400_BAD_REQUEST)
		return Response({'Bad Request': 'Invalid post data, did not find a server name'}, status=status.HTTP_400_BAD_REQUEST)
		 
		# serializer = PrivateServerSerializer(data=request.data)
		
		# if serializer.is_valid():
		# 	name = serializer.data.get('name')
		# 	password = serializer.data.get('password')
		# 	queryset = PrivateServer.objects.filter(name=name).first()		
		# 	if queryset.exists():	
		# 		if queryset.password == password:
		# 			return Response({'message': 'Server Joined!'}, status=status.HTTP_200_OK)
		# 		return Response({'Wrong Password': 'Cannot join wrong password'}, status=status.HTTP_401_UNAUTHORIZED)
		# 	return Response({'No req': 'Invalid Server Name'}, status=status.HTTP_400_BAD_REQUEST)
		# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
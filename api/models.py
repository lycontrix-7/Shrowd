from django.db import models

class PublicServer(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name
	
class PrivateServer(models.Model):
	name = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.name

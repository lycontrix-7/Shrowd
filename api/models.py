from django.db import models

class Server(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name
	
class Message(models.Model):
	content = models.TextField()
	server = models.ForeignKey(Server, on_delete=models.CASCADE)

	def __str__(self):
		return self.content

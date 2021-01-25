from django.forms import ModelForm
from .models import Server, Message

class PublicForm(ModelForm):
	class Meta:
		model = Server
		fields = '__all__'

class MessageForm(ModelForm):
	class Meta:
		model = Message
		fields = ('content',)
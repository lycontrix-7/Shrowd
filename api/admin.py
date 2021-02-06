from django.contrib import admin
from .models import PrivateServer, PublicServer

admin.site.register(PublicServer)
admin.site.register(PrivateServer)
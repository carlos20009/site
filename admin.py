from django.contrib import admin
from .models import Client
from .models import Pay

@admin.register(Client)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellido","correo"]

@admin.register(Pay)
class PaysAdmin(admin.ModelAdmin):
    list_display = ["id","nombre"]
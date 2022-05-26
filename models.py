from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length=120)
    correo = models.EmailField(max_length=200)

    def __str__(self):
        return self.Client_text

class Pay(models.Model):
    nombre = models.CharField(max_length= 20)

    def __str__(self):
        return self.nombre

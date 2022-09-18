from django.db import models

class Desarrollador(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    legajo = models.IntegerField()
    puesto = models.CharField(max_length=50)

    def __str__(self):
        return print(f"{self.nombre} {self.apellido} leg: {self.legajo}")

class Grupo(models.Model):

    id_grupo = models.IntegerField()
    tabla = models.CharField(max_length=30)
    desarrollador = models.IntegerField()
    frecuencia_act = models.CharField(max_length=30)
    area_solicitud = models.CharField(max_length=30)
    herramienta = models.CharField(max_length=30)

    def __str__(self):
        return self.id_grupo

class Dicty(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tabla(models.Model):

    nombre = models.CharField(max_length=50)
    campo = models.CharField(max_length=240, db_index=True)
    descripcion = models.CharField(max_length=240, db_index=True)

    def __str__(self):
        return self.container


from django.db import models

class Estudiante(models.Model):
    CodEstudiante = models.AutoField(primary_key=True)
    anioingreso = models.DateField()
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    CodCurso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    credito = models.IntegerField()

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    codDocente = models.AutoField(primary_key=True)
    apeliido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Matricula(models.Model):
    anioacademico = models.DateField('Año académico')
    ciclo = models.CharField(max_length=2)
    fecha = models.DateField('Fecha de matrícula')
    codigoestudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    codigocurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    codigodocente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.ciclo

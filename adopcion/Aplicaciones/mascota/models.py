from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula})"


class Mascota(models.Model):
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('no_disponible', 'No Disponible'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    raza = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='disponible')
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo} - {self.raza})"




    def __str__(self):
        return f"Adopción: {self.persona} - {self.mascota} en {self.fecha_adopcion}"

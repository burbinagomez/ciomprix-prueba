from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Persona(AbstractUser):
    identificacion = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=100, null=True)
    rol = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'identificacion', 
        'first_name', 
        'last_name',
        'email',
        'password'
        ]
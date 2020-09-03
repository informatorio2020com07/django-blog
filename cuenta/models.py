from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Perfil(AbstractUser):
    nacimiento = models.DateField(null=True)
    foto = models.ImageField(upload_to="perfil", null=True, blank=True)
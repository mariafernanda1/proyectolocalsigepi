from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class usu(AbstractUser):

#    id_rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=True, blank =True)  # Identificador del  módulo# Identificador del Rol de Usuario de Sistema
    fch_regi = models.DateField('fecha de registro', auto_now = False,  null=True, blank =True) # fecha de registro de usurio
    activo = models.BooleanField('¿Activo o desactivado.?', default=False,  null=True, blank =True) # estatus del usuario activo (True) inactivo (False)

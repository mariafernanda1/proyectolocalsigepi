from django.db import models
from django.conf import settings

class Basemodels(models.Model):
    user_crear = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_crear', null= True, blank=True)
    fech_crear = models.DateField(auto_now_add=True, null= True, blank=True)
    user_modif = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_modif', null= True, blank=True)
    fech_modf = models.DateField(auto_now= True, null=False, blank = False)

    class Meta:
        abstract = True

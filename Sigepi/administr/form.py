from django import forms
from .models import *

class RolForm(forms.ModelForm):
    class Meta:
        model = rol
    #    fields = ('nombre', 'descricion',) para llamar a campos especificos
        fields = '__all__'

class ModForm(forms.ModelForm):
    class Meta:
        model = mod
        fields = '__all__'

class PermisoForm(forms.ModelForm):
    class Meta:
        model =  Permiso
        fields = '__all__'

class AppForm(forms.ModelForm):
    class Meta:
        model = app_mod
        fields = '__all__'

class FuentForm(forms.ModelForm):
    class Meta:
        model =  func_app
        fields = '__all__'

class AplicativoForm(forms.ModelForm):
    class Meta:
        model =  listado_aplicativo
        fields = '__all__'

class UsuForm(forms.ModelForm):
    class Meta:
        model = usu
        fields = '__all__'

class RlmodrolForm(forms.ModelForm):
    class Meta:
        model = rl_mod_rol
        fields = '__all__'

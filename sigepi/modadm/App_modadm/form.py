from django.contrib.admin.widgets import AutocompleteSelect
from django.forms import BaseModelFormSet
from django.contrib import admin
from django import forms
from django.forms import Select
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class funcionForm(forms.ModelForm):
    class Meta:
        model =  func_app
        fields = '__all__'

class funciongrupForm(forms.ModelForm):

    #def _init__(self, solicitud, *args,**kwargs):
    #    super(app_modForm,self).__init__(*args, **kwargs)
    #    self.fields['id_func'].ModelMultipleChoiceField(self)
    #id_func = forms.ModelMultipleChoiceField(queryset=rl_func_app.objects.all())
    #id_func = forms.ModelMultipleChoiceField(queryset=None)
    class Meta:
        model = rl_func_rol
        fields = ['id_rol',
                  'id_func',
                  'reg_bd',
                 ]
        #resultado = solicitud.GET.get('id_app_sel',None)
        #id_func = forms.ModelChoiceField(queryset= rl_func_app.objects.filter(id_app__titulo='App_modadm'))
    #    resultado = solicitud.GET.get('id_app_sel',None)
    #    id_func = forms.ModelChoiceField(queryset= rl_func_app.objects.filter(id_app__pk=resultado))


class app_modForm(forms.ModelForm):

    def __init__(self, solicitud, *args,**kwargs):
        super(app_modForm,self).__init__(*args, **kwargs)
        self.fields['titulo'].queryset=app_mod.objects.all()

    class Meta:
        model =  app_mod
        fields = '__all__'

#class grup_rol_func_Form(forms.ModelForm):
#    class Meta:
#       model = Folder
#       fields = ['name', 'parent']
#
#    def __init__(self, *args, **kwargs):
#       user = kwargs.pop('user')
#       super(FolderForm, self).__init__(*args, **kwargs)
#       self.fields['parent'].queryset = Folder.objects.filter(user=user)

class frm_func_grupo(forms.ModelForm):
    #Calse que automatiza la creación de formularios de Registro de Usuario en Django.
    class Meta:
        model = rl_func_rol
        fields = ['id_rol',
                  'id_func',
                  'reg_bd',
                 ]
        widgets = {
                'id_func' : AutocompleteSelect(
                rl_func_rol._meta.get_field('id_func').remote_field,
                admin.site,
                attrs={'placeholder':'seleccionar...'},
            )
        }


class appForm(forms.Form):
    app = forms.ModelChoiceField(queryset=app_mod.objects.all().order_by('titulo'))

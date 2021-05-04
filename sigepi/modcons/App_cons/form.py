from django import forms
from django.contrib.auth.models import User
from modadm.App_regusu.models import usu_inf_apps
from modadm.App_regusugr.models import usugr
from modadm.App_regusui.models import usui
from modadm.App_modadm.models import mod,app_mod,func_app, rl_func_app

class frm_con_usu(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                 ]
        labels ={
                'username' : 'username',
                'first_name' : 'nombre',
                'last_name' : 'apellido',
                'email' : 'correo',
                }

class frm_con_usugr(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model = usugr
        fields = ['id_gr',
                  'passgr',
                  'id_usu_admin',
                  'id_rol_app',
                  'activo',
                 ]
        labels = {
                'id_gr' : 'identificador de usuario grupo',
                'passgr' : 'contraseña',
                'id_usu_admin' : 'identificador usuario',
                'id_rol_app' : 'identificador rol',
                'activo' : 'estas activo?',
                }

class frm_con_usui(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model = usui
        fields = ['id_usuinst',
                  'passinst',
                  'id_usu_admin',
                  'id_rol_app',
                  'fch_regi',
                  'activo'
                 ]
        labels = {
                'id_usuinst' : 'identificador de usuario institucional',
                'passinst' : 'contraseña',
                'id_usu_admin' : 'identificador usuario  administartivo ',
                'id_rol_app' : 'identificador rol',
                'fch_regi' : 'fecha registro',
                'activo' : 'si estas activo?',
                }

class frm_con_mod(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de modulos en Django.
    class Meta:
        model = mod
        fields = [
                'id_mod',
                'titulo',
                'desc',
                'url_doc',
                'version',
                'activo',
                'instalado',
                'visible',
                'ls_param_cnf'
                ]
        labels = {
                'id_mod' : 'Identificador Módulos',
                'titulo' : 'Título Módulo',
                'desc' :  'Descripción Módulo',
                'url_doc' : 'Url del documento Módulo',
                'version' : 'versión del Módulo',
                'activo' : 'El Módulo activo',
                'instalado' : 'El Módulo esta instalado?',
                'visible' : 'El Módulo esta visible',
                'ls_param_cnf' : 'parametros',
                }

class frm_con_app(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de modulos en Django.
    class Meta:
        model = app_mod
        fields = [
                'id_app',
                'titulo',
                'desc',
                'url_doc',
                'version',
                'mod_prin',
                'ver_mod',
                'activo',
                'instalada',
                'visible'
                ]

        labels = {
                'id_app' : 'Identificador del Aplicativo',
                'titulo' : 'Título Aplicativo',
                'desc' :  'Descripción Aplicativo',
                'url_doc' : 'Url del documento Aplicativo',
                'version' : 'versión del Aplicativo',
                'mod_prin': 'Identificador del Módulo Principal',
                'ver_mod' : 'Versión mínima del módulo principal',
                'activo' : 'El Aplicativo activo',
                'instalada' : 'El Aplicativo esta instalado?',
                'visible' : 'El Aplicativo esta visible'
                }


class frm_con_mod(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de modulos en Django.
    class Meta:
        model = mod
        fields = [
                'id_mod',
                'titulo',
                'desc',
                'url_doc',
                'version',
                'activo',
                'instalado',
                'visible',
                'ls_param_cnf'
                ]
        labels = {
                'id_mod' : 'Identificador Módulos',
                'titulo' : 'Título Módulo',
                'desc' :  'Descripción Módulo',
                'url_doc' : 'Url del documento Módulo',
                'version' : 'versión del Módulo',
                'activo' : 'El Módulo activo',
                'instalado' : 'El Módulo esta instalado?',
                'visible' : 'El Módulo esta visible',
                'ls_param_cnf' : 'parametros',
                }

class frm_rol_usu(forms.ModelForm):
    #Calse que busca los campos de roles de usaurio
    class Meta:
        model = usu_inf_apps
        fields = '__all__'

class frm_con_func_app(forms.ModelForm):
    #Calse que busca los campos de roles dsegun su funcion
    class Meta:
        model = rl_func_app
        fields = '__all__'

#class frm_con_func_app_rol(forms.ModelForm):
#    #Calse que busca los campos de roles dsegun su funcion
#    class Meta:
#        model = rl_func_rol
#        fields = '__all__'


class frm_con_func(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de modulos en Django.
    class Meta:
        model = func_app
        fields = [
                'id_func',
                'nom_func',
                'lib_func',
                'url_loc',
                'com_exc',
                'text',
                'context',
                'activa',
                'indice'
                ]

        labels = {
                'id_func' : 'Identificador Funciones',
                'nom_func' : 'Nombre la la función',
                'lib_func' : 'librería ed la función',
                'url_loc' : 'Url local de la función',
                'com_exc' : 'Comando de Ejecución de la Función',
                'text' : 'Nombre de Función para menús o etiquetas.',
                'context' : 'Nombre de Función para menús contextuales',
                'activa' : ' La función está activa o desactiva.',
                'indice' : 'Índice de selección, para navegar con el tabulador.',
                }

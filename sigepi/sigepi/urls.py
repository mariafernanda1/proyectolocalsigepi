#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado: 21-04-2021
Última Modificación: 21-04-2021 08:02
Autor: Milton castro
colaboración: María Fernanza Zambrano
Hora:04:24

Urls aplicación principal SIGEPI

"""
#Librerías de sistema
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles import views
from django.urls import re_path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

#Librerías de aplicaciones
from modadm.App_modadm.views import *
from modadm.App_modadm.urls import *
from modadm.App_modadm.class_view import *
from modcons.App_cons.views import *
from modadm.App_regusu.urls import *
from modadm.App_regusugr.urls import *

from .views import *
#from administr.views import inicio, inicio2, inicioapp, crearrol, crearmod, editarRol, crearapp, editarMod,editarApp, eliminarMod,eliminarApp
#inicio nombre de la f<input type="hidden" name="next" value="{{ next }}" />uncion importada e viw de adminityr

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]
    urlpatterns += staticfiles_urlpatterns()

urlpatterns = [
    #direcciones del front (finales en producción)
    path('',front().vst_raiz),
    path('inicio',front().vst_inicio),
    path('cerrar', front().vst_cerrar, name = 'cerrar'),
    path('doc', front().vst_doc, name ='doc'),
    #Direcciones del backend Django
    path('serv/', admin.site.urls),
    path('accounts', include('django.contrib.auth.urls')),
    #Direcciones de administración SIGEPI
    path('modadm/',include("modadm.App_modadm.urls")),
    #Direcciones de la Aplicación App_regusu
    path('modadm/',include("modadm.App_regusu.urls")),
    #Direcciones de la Aplicación App_regusui
    path('modadm/',include("modadm.App_regusui.urls")),
    #Direcciones de la Aplicación App_reguusgr
    path('modadm/',include("modadm.App_regusugr.urls")),
    #Direcciones de prueba (se deben eliminar en producción)
    path('inicioprb',front_prb().vst_indexprueba, name = 'iniciop'),
    path('ingresoprb',front_prb().vst_ingreso, name = 'ingresop'),
    path('registro_suprb',vst_frm_reg_usu_su.as_view(), name = 'registro_su_p'),
    path('registro_admprb',vst_frm_reg_usu_adm.as_view(), name = 'registro_adm_p'),
    path('registroprb',vst_frm_reg_usu.as_view(), name = 'registrop'),
    path('rolesusuprb',front_prb().vst_indexprueba, name = 'rolesusup'),


    path("select2/", include("django_select2.urls")),

    # … other patterns

    #consultas globales
    #consultar usuario
    path('conusus', vts_ls_usu.as_view(), name='consulta_usuarios'),
    #consultar isntitucion
    path('con_usui', vts_ls_usui.as_view(), name='cons_usui'),
    #consultar grupo
    path('conusugr', vts_ls_usugr.as_view(), name = 'cons_usugr'),
    #consultar modulos
    path('conmod', vts_ls_mod.as_view(), name = 'cons_mod'),
    #consultar aplicativos
    path('conapp', vts_ls_app.as_view(), name = 'consulta_app'),
    #consultar funciuones
    path('confunc', vts_ls_func.as_view(), name = 'consulta_funciones'),
    #consultar roles de usuario
    path('confunciones', vts_ls_func_app.as_view(), name = 'con_func_app'),
    #consultar roles de usuario
    path('conusuroles', ls_rol_usu.as_view(), name = 'consulta_roles'),

    #consultar funciones segun roles
#    path('conusurolfunc', vts_ls_func_rol_grup.as_view(), name = 'consulta_roles_func'),


    #prueba para ver los roles de un usuario
    path('prueba_rol_usu/<int:id_usu>', vst_roles().rol_usu, name = 'prueba_rol'),

#    path('rol_selc/<int:id_rolusu>', mirolselc.as_view(), name = 'prueba_rol'),

    #consulta generica para verificar la funcion que asigna datos
    path('congeneric', funcionrelaciones, name = 'cons_generic'),


    #prueba de roles
    #path('listarrol',rolusuList.as_view(), name = 'listarrol'),

    ]
urlpatterns += staticfiles_urlpatterns()

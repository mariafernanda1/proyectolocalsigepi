from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from modadm.App_modadm.views import *
from modadm.App_modadm.class_view import *



urlpatterns = [

# direcciones del modulo admin
    path('inicioadmin', backend.modadm, name="inicioadmin"),

# direcciones del modulo admin de prueba
    path('inic_adm_prb', backend_prb().modadmprb, name="inic_adm_prb"),
#ingreso de login para modulo administrativo prueba
    path('ingreso_adm_prb', ingreso().vst_ingreso, name="ingreso_adm_prb"),
    path('ingreso_adm_prb', ingreso().vst_cerrar, name="cerrar_adm_prb"),

# registrar modulos
    path('reg_modu', vts_reg_mod.as_view(), name ='reg_mod'),
    path('editar_mod/<int:pk>/', vst_modf_reg_mod.as_view(), name = 'modificar_mod'),
    path('ls_modf_mod',vst_selc_mod_cons.as_view(), name='ls_modificar_mod'),

# registro de aplicaciones
    path('reg_app', vts_reg_app.as_view(), name ='reg_app'),
    path('editar_app/<int:pk>/', vst_modf_reg_app.as_view(), name = 'modificar_app'),
    path('ls_modf_app',vst_selc_app_cons.as_view(), name='ls_modificar_app'),

# registro de #funciones por aplicativos
    path('reg_func_app', vts_reg_func_app.as_view(), name ='reg_func_app'),
    path('editar_func_app/<int:pk>/', vst_modf_reg_func_app.as_view(), name = 'modificar_func_app'),
    path('ls_modf_func_app',vst_selc_func_app_cons.as_view(), name='ls_modificar_func_app'),

# registro de funciones por roles

    path('reg_func_rol', crearrolfunc().crearfuncrol, name ='reg_func_rol'),
    path('slec_app', vts_listarapp.as_view(), name ='selct_app'),
    path('pasarr', pasar1().pasar, name ='pasarr'),

#    path('editar_func_rol/<int:pk>/', vst_modf_reg_func_rol.as_view(), name = 'modificar_func_rol'),
#   path('ls_modf_func_rol',vst_selc_func_rol_cons.as_view(), name='ls_modificar_func_tol'),


#prueba de sesion usu
    path('sesion',sesion().sesionusu, name='sesion_pr'),


# registro de #funciones
    path('reg_func', vts_reg_func.as_view(), name ='reg_func'),
    path('editar_func/<int:pk>/', vst_modf_reg_func.as_view(), name = 'modificar_func'),
    path('ls_modf_func',vst_selc_func_cons.as_view(), name='ls_modificar_func'),


]

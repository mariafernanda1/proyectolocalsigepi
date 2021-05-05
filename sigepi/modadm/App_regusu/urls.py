from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from modadm.App_regusu.views import *
from modadm.App_regusu.class_view import *


urlpatterns = [

    #editar usuario de consulta
    path('edi_usu/<int:pk>/',vst_mod_reg_usu.as_view(), name = 'editar_usu'),
    path('ls_mod_usu',vst_selc_usu_cons.as_view(), name='ls_mod_usu'),
    #crear usuario del modulo adm
    path('creausuprb/',vts_reg_usu_su.as_view(), name = 'crea_usuprb'),

#ingreso de login para modulo usuario prueba
    path('index_usu', backend().modusu, name="index_usu"),
    path('ingreso_usu_prb', ingreso().vst_ingreso, name="ingreso_usu_prb"),
    path('ingreso_usu_prb', ingreso().vst_cerrar, name="cerrar_usu_prb"),

#registro de usuario contacto
    path('infocont/',infousucontCreate.as_view(), name = 'infocont'),
    path('infocontc_usu/<int:id_usu>', listar_inf_cont().inf_cont, name = 'infocontc_usu'),
    path('editarinf/<int:pk>/',infousucontUpdate.as_view(), name='editarinf'),

#registro de usuario formacion academica
    path('infoacad/',infoacadusuRegis.as_view(), name = 'reg_formacad'),
    path('form_acad_usu/<int:id_usu>', listar_formacad_cont().form_acad, name = 'listformaca_usu'),
    path('editarformacad/<int:pk>/',formacad_usuModif.as_view(), name='editarforaca'),

#registro de informacion personal
    path('infopersusu/',infopers_usuRegis.as_view(), name = 'reg_infoperusu'),


    path('infopers/',infoperslList.as_view(), name = 'infopers'),
    path('crearinf/',infopersCreate.as_view(), name = 'crearinf'),
    path('editarinf/<int:pk>/',infopersUpdate.as_view(), name='editarinf'),
    path('eliminarinf/<int:pk>/',infopersDelete.as_view(), name='eliminarinf')
#funciones

]

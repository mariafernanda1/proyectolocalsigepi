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
    path('borrarinf/<int:pk>/',infousucontBorrar.as_view(), name='borrarinf'),

#registro de informacion personal
    path('infopersusu/',infopers_usuRegis.as_view(), name = 'reg_infoperusu'),
    path('info_pers_usu/<int:id_usu>', listar_infopers_usu().infopers, name = 'listusuinfpers_usu'),
    path('editarinfopers/<int:pk>/',infopers_usu_Modif.as_view(), name='editar_infoper_usu'),
    path('borrarinfper/<int:pk>/',infopers_usu_Borrar.as_view(), name='borrarinfper'),

#registro de usuario formacion academica
    path('infoacad/',infoacadusuRegis.as_view(), name = 'reg_formacad'),
    path('form_acad_usu/<int:id_usu>', listar_formacad_cont().form_acad, name = 'listformaca_usu'),
    path('editarformacad/<int:pk>/',formacad_usuModif.as_view(), name='editarforaca'),
    path('borrarformacad/<int:pk>/',formacad_usuBorrar.as_view(), name='borrarformacad'),

#registro de informacion EMPLEO
    path('infoempleousu/',empleo_usuRegis.as_view(), name = 'reg_empleousu'),
    path('empleos_usu/<int:id_usu>', listar_empleo_usu().empleo_usu, name = 'listempleo_usu'),
    path('editarempleo/<int:pk>/',empleo_usuModif.as_view(), name='editarempleo'),
    path('borrarempleo/<int:pk>/',empleo_usuBorrar.as_view(), name='borrarempleo'),

#registro de redes sociales por parte del usuario
    path('reg_redsocialusu/',redsocial_usuRegis.as_view(), name = 'reg_redsocialusu'),
    path('redsocial_usu/<int:id_usu>', listar_redsocial_usu().redsocial_usu, name = 'listredsoci_usu'),
    path('editarred/<int:pk>/',redsocial_usuModif.as_view(), name='editaredsocial'),
    path('borrared/<int:pk>/',redsocial_usuBorrar.as_view(), name='borrarrecsocail'),

#registro de cursos dictados por parte del usuario
    path('reg_cursductusu/',cursodict_usuRegis.as_view(), name = 'reg_cursdictusu'),
    path('cursdict_usu/<int:id_usu>', listar_cursodict_usu().cursdict_usu, name = 'listcursodict_usu'),
    path('editarcurso/<int:pk>/',cursdict_usuModif.as_view(), name='editacursodict'),
    path('borrarcurso/<int:pk>/',cursdict_usuBorrar.as_view(), name='borrarcursodict'),

#registro de de habilidades por usuario
    path('reg_infhabusu/',inf_hab_usuRegis.as_view(), name = 'reg_infhabusu'),
    path('infhab_usu/<int:id_usu>', listar_inf_hab_usu().infhab_usu, name = 'listinfhab_usu'),
    path('editarinfhab/<int:pk>/',inf_hab_usuModif.as_view(), name='editarinfhab'),
    path('borrarhabilidad/<int:pk>/',inf_hab_usuBorrar.as_view(), name='borrarinfhab'),

#registro de de validar  habilidades por usuario
    path('reg_valhabusu/',val_hab_usuRegis.as_view(), name = 'reg_valhabusu'),
    path('valhab_usu/<int:id_usu>', listar_val_hab_usu().valhab_usu, name = 'listinfval_usu'),
    path('editarvalhab/<int:pk>/',val_hab_usuModif.as_view(), name='editarvalhab'),
    path('borrarvalhabl/<int:pk>/',val_hab_usuBorrar.as_view(), name='borrarvalhab'),

]

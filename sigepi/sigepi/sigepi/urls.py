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
from moduloAdm.views import *
from moduloAdm.class_view import *
from moduloAdm.urls import *
#from administr.views import inicio, inicio2, inicioapp, crearrol, crearmod, editarRol, crearapp, editarMod,editarApp, eliminarMod,eliminarApp
#inicio nombre de la funcion importada e viw de adminityr

urlpatterns = [
    path('serv/', admin.site.urls),
    path('inicio',front().v_inicio),
    path('accounts/', include('django.contrib.auth.urls')),
    path("apisigepi/", include("moduloAdm.urls")),
        #path('admi', include('administr.urls')),
        #path('', LoginView.as_view(template_name='login.html')),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),

    ]
urlpatterns += staticfiles_urlpatterns()

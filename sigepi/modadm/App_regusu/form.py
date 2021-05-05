#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado: 25-04-2021
Última Modificación: 25-04-2021 08:02
Autor: Milton castro
colaboración: María Fernanza Zambrano
Hora:04:24

Formularios de Registro de usuarios (form.py)
Aplicación registro de usuarios
Módulo administrativo SIGEPI

"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class frm_reg_usu_pers(forms.ModelForm):
    #clase para la creación de un formulario de registro de información personal de usuario SIGEPI.
    class Meta:
        #Metadatos de la clase
        model =  usu_inf_pers
        fields = [
            'nuip',
            'tipo_nuip',
            'nombres',
            'apelllidos',
            'nal',
            'fch_naci',
            'gene',
            'ocup',
            'dir',
            'discap',
            'tipo_discap',
            'url_imag',
            'zona_hor'
        ]

        labels = {
            'nuip' : 'NUIP',
            'tipo_nuip': 'Tipo',
            'nombres': 'Nombres',
            'apelllidos':'Apellidos',
            'nal' : 'Nacionalidad',
            'fch_naci' : 'Fecha de nacimiento',
            'gene' : 'Género',
            'ocup':'Ocupación',
            'dir' : 'Dirección',
            'discap' : 'Discapacidad',
            'tipo_discap':'Tipo de Disc.',
            'url_imag' : 'URL Imagen',
            'zona_hor' : 'Zona Horaria',
        }

class frm_reg_usu_cont(forms.ModelForm):
    #clase para la creación de un formulario de registro de información personal de usuario SIGEPI.
    class Meta:
        #Metadatos de la clase
        model =  usu_inf_contac
        fields = [
            'ind_nal',
            'cel',
            'wa',
            'email',
            'cod_post',
            'ls_ha',
            'web',
            'dir_offi'

        ]

        labels = {
            'ind_nal' : 'Nacionalidad',
            'cel': 'Numero de celular',
            'wa': 'WhatsApp',
            'email': 'Correo',
            'cod_post' : 'Codigo Postal',
            'ls_ha' : 'Horario',
            'web' : 'Direccion  Web',
            'dir_offi':'Direccion de oficina',
        }

class frm_reg_usu_acad(forms.ModelForm):
    #clase para la creación de un formulario de registro de información personal de usuario SIGEPI.
    class Meta:
        model =  form_acad
        fields = [
            'instit',
            'tipo_form',
            'fch_ini',
            'fch_fin',
            'certif',
            'nal',
            'ciudad',
            'mod',
            'tit',
            'menc',
            'token'
        ]

        labels = {
            'instit' : 'Institucion ',
            'tipo_form': 'Tipo de formación ',
            'fch_ini': 'Fecha de Inicio ',
            'fch_fin': 'Fecha de Fin ',
            'certif' : 'Certificado ',
            'nal' : 'Nacionalidad ',
            'ciudad' : 'Cuidad ',
            'mod':'Modalidad ',
            'tit' : 'Titulo ',
            'menc' : 'Mencion ',
            'token' : 'Token ',
        }

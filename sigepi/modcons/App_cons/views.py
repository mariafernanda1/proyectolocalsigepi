from django.shortcuts import render
from django.views.generic import CreateView, DeleteView,ListView,UpdateView,View
from django.urls import reverse_lazy
from django.contrib import messages
from .form import *
from django.http import HttpResponse
from modadm.App_regusu.models import usu_inf_apps
from registro.models import usu
from modadm.App_regusugr.models import usugr
from modadm.App_regusui.models import usui
from modadm.App_modadm.models import mod, app_mod

class vts_ls_usu(ListView):
    # clase para listar usuarios del sistema
    model = usu
    form_class = frm_con_usu
    template_name = 'cn_usu.html'
    success_url = reverse_lazy('cn_usu.html')
    success_message = 'listado cargado correctamente'

class vts_ls_usui(ListView):
    # clase para listar usuarios del sistema
    model = usui
    form_class = frm_con_usui
    template_name = 'cn_usui.html'
    success_url = reverse_lazy('cn_usui.html')
    success_message = 'listado cargado correctamente'

class vts_ls_usugr(ListView):
    # clase que me lsta todos los grupos
    model = usugr
    form_class = frm_con_usugr
    template_name = 'cn_usugr.html'
    success_url = reverse_lazy('cn_usugr.html')
    success_message = 'listado cargado correctamente'

class vts_ls_mod(ListView):
    # clase que me lsta todos los modulos
    model = mod
    form_class = frm_con_mod
    template_name = 'cn_mod.html'
    success_url = reverse_lazy('cn_mod.html')
    success_message = 'listado cargado correctamente'

class vts_ls_app(ListView):
    #clase que  me lista todos las aplicaciones del Sistema
    model = app_mod
    form_class = frm_con_app
    template_name = 'cn_aplic.html'
    success_url = reverse_lazy('cn_aplic.html')
    success_message = 'listado cargado correctamente'

class vts_ls_func(ListView):
    #clase que  me lista todos las funciones  del Sistema
    model = func_app
    form_class = frm_con_func
    template_name = 'cn_func.html'
    success_url = reverse_lazy('cn_func.html')
    success_message = 'listado cargado correctamente'

class vts_ls_func_app(ListView):
    #clase que  me lista todos las aplicaciones por fucniones
    model = rl_func_app
    form_class = frm_con_func_app
    template_name = 'cn_func_app.html'
    success_url = reverse_lazy('cn_func_app.html')
    success_message = 'listado cargado correctamente'

#class vts_ls_func_rol_grup(ListView):
#    #clase que  me lista todos las funciones segun los roles del Sistema
#    model = rl_func_rol
#    form_class = frm_con_func_app_rol
#    template_name = 'cn_func_app_rol.html'
#    success_url = reverse_lazy('cn_func_app_rol.html')
#    success_message = 'listado cargado correctamente'

#class vts_ls_rol_mod_app(ListView):
#    #clase que  me lista todos las aplicaciones segun el rol del Sistema
#    model = rl_app_mod_rol
#    form_class = frm_con_rol_app_mod
#    template_name = 'cn_rol_app.html'
#    success_url = reverse_lazy('cn_rol_app.html')
#    success_message = 'listado cargado correctamente'


#class vts_ls_rol_mod(ListView):
#    #clase que  me lista todos los modulos segun el modulo del Sistema
#    model = rl_mod_rol
#    form_class = frm_con_rol_mod
#    template_name = 'cn_rol_mod.html'
#    success_url = reverse_lazy('cn_rol_mod.html')
#    success_message = 'listado cargado correctamente'

class ls_rol_usu(ListView):
    # clase para listar roles en general de los  usuarios del sistema
    model = usu_inf_apps
    form_class = frm_rol_usu
    template_name = 'cn_rol_usu.html'
    success_url = reverse_lazy('cn_rol_usu.html')
    success_message = 'listado cargado correctamente'

class vst_roles():
# funcion que me carga los roles por usurio
    def rol_usu(self, solicitud, id_usu):
        roles = usu_inf_apps.objects.filter(id_usu=id_usu)
        return render(solicitud, "cn_rol_usu.html",{'roles':roles})


class ls_rol_usup(ListView):
    # clase para listar roles de usuarios del sistema
    model = usu_inf_apps
    form_class = frm_rol_usu
    template_name = 'cn_rol_usu.html'
    success_url = reverse_lazy('cnsl_generic.html')
    success_message = 'listado cargado correctamente'

class mod_usu(UpdateView):
    #clase que me modifica usuarios del sistema
    model = usu
    form_class = frm_con_usu
    template_name = 'sl_usu.html'
    success_url = reverse_lazy('mod_usu_prb.html')
    success_message = 'modificado correctamente'

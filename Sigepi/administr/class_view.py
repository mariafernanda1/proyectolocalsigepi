from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .models import *
from .form import *

class PermisoList(ListView): #heredaa de listwview
    model = Permiso
    template_name = 'adminer/permisos/permisos.html'

"""
#si quiero cambiar la consulta
    def get_queryset(self):
        return self.model.objects.all()[:2] #para indicar que mme traiga los ultimos dos registros
"""
class PermisosCreate(CreateView):
    model = Permiso
    form_class = PermisoForm
    template_name = 'adminer/permisos/crearpermiso.html'
    success_url = reverse_lazy('permisos')

class PermisosUpdate(UpdateView):
    model = Permiso
    form_class = PermisoForm
    template_name = 'adminer/permisos/crearpermiso.html'
    success_url = reverse_lazy('permisos')

class PermisosDelete(DeleteView):
    model = Permiso
    template_name = 'adminer/permisos/verificacion.html'
    success_url = reverse_lazy('permisos')


############# listado aplicativo vistas hecgas en clases

class AplicativoList(ListView): #heredaa de listwview
    model = listado_aplicativo
    template_name = 'adminer/aplicativos/listado_aplicativo.html'

class AplicativoCreate(CreateView):
    model = listado_aplicativo
    form_class = AplicativoForm
    template_name = 'adminer/aplicativos/crearaplicativo.html'
    success_url = reverse_lazy('aplicativo')

class AplicativoUpdate(UpdateView):
    model = listado_aplicativo
    form_class = AplicativoForm
    template_name = 'adminer/aplicativos/crearaplicativo.html'
    success_url = reverse_lazy('aplicativo')

class AplicativoDelete(DeleteView):
    model = listado_aplicativo
    template_name = 'adminer/aplicativos/verificacion.html'
    success_url = reverse_lazy('aplicativo')


############# listado apps vistas hechas en clases

class AppList(ListView): #heredaa de listwview
    model = app_mod
    template_name = 'adminer/apps/app.html'

class AppCreate(CreateView):
    model = app_mod
    form_class = AppForm
    template_name = 'adminer/apps/crearapp.html'
    success_url = reverse_lazy('app')

class AppUpdate(UpdateView):
    model = app_mod
    form_class = AppForm
    template_name = 'adminer/apps/crearapp.html'
    success_url = reverse_lazy('app')

class AppDelete(DeleteView):
    model = app_mod
    template_name = 'adminer/apps/verificacion.html'
    success_url = reverse_lazy('app')

############# listado usuarios vistas hechas en clases

class UsuList(ListView): #heredaa de listwview
    model = usu
    template_name = 'adminer/usuarios/usu.html'

class UsuCreate(CreateView):
    model = usu
    form_class = UsuForm
    template_name = 'adminer/usuarios/crearusu.html'
    success_url = reverse_lazy('usu')

class UsuUpdate(UpdateView):
    model = usu
    form_class = UsuForm
    template_name = 'adminer/usuarios/crearusu.html'
    success_url = reverse_lazy('usu')

class UsuDelete(DeleteView):
    model = usu
    template_name = 'adminer/usuarios/verificacion.html'
    success_url = reverse_lazy('usu')

############ listado rol vistas hechas en clases

class RolList(ListView): #heredaa de listwview
    model = rol
    template_name = 'adminer/roles/roles.html'

class RolCreate(CreateView):
    model = rol
    form_class = RolForm
    template_name = 'adminer/roles/crearrol.html'
    success_url = reverse_lazy('roles')

class RolUpdate(UpdateView):
    model = rol
    form_class = RolForm
    template_name = 'adminer/roles/crearrol.html'
    success_url = reverse_lazy('roles')

class RolDelete(DeleteView):
    model = rol
    template_name = 'adminer/roles/verificacion.html'
    success_url = reverse_lazy('roles')

################ listado de modulo

class modList(ListView): #heredaa de listwview
    model = mod
    template_name = 'adminer/modulos/mod.html'

class modCreate(CreateView):
    model = mod
    form_class = ModForm
    template_name = 'adminer/modulos/crearmod.html'
    success_url = reverse_lazy('mod')

class modUpdate(UpdateView):
    model = mod
    form_class = ModForm
    template_name = 'adminer/modulos/crearmod.html'
    success_url = reverse_lazy('mod')

class modDelete(DeleteView):
    model = mod
    template_name = 'adminer/modulos/verificacion.html'
    success_url = reverse_lazy('mod')

################ listado de relacion entre modulo y rol

class modrolList(ListView): #heredaa de listwview
    model = rl_mod_rol
    template_name = 'adminer/rl_mod_adm/mod_rol/mod_rol.html'

class modrolCreate(CreateView):
    model = rl_mod_rol
    form_class = RlmodrolForm
    template_name = 'adminer/rl_mod_adm/mod_rol/crear_rl_mod_rol.html'
    success_url = reverse_lazy('modrol')

class modrolUpdate(UpdateView):
    model = rl_mod_rol
    form_class = RlmodrolForm
    template_name = 'adminer/rl_mod_adm/mod_rol/crear_rl_mod_rol.html'
    success_url = reverse_lazy('modrol')

class modrolDelete(DeleteView):
    model = rl_mod_rol
    template_name = 'adminer/rl_mod_adm/mod_rol/verificacion.html'
    success_url = reverse_lazy('modrol')

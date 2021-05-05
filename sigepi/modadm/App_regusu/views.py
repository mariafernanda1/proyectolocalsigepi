from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.core import serializers
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *
from .form import *
from modcons.App_cons.form import frm_con_usu
from modcons.App_cons.views import vts_ls_usu


class backend():
     # inicio del index de usuario
    def modusu(self,solicitud):
        return render(solicitud,'index_usu_prb.html')

#ingreso de usuario al sistema
class ingreso(ObtainAuthToken):

    def vst_ingreso(self, solicitud, *args, **kwargs):

        if solicitud.method == "POST":
            form = AuthenticationForm(solicitud, data=solicitud.POST)
            if form.is_valid():
                nombreusu = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                usuario = authenticate(solicitud, username = nombreusu, password = password)
                user_id = usuario.id #obtengo todos los datos de usuario
                #print(user_id)
                if usuario is not None:
                    token, created = Token.objects.get_or_create(user_id = user_id)
                    login(solicitud, usuario)
                    #solicitud.session.['usuariosesi'] = User.id
                    messages.success(solicitud,F"bienvenido {nombreusu}")
                    return render(solicitud,'index_usu_prb.html')
                else:
                    messages.success(solicitud,F"los datos son incorrectos")
        form = AuthenticationForm()
        return render(solicitud,'ingreso_modadmusu.html', {"form": form} )

    def vst_cerrar(self, solicitud):
        logout(solicitud)
        messages.success(solicitud,"tu sesión ha cerrado ")
        form = AuthenticationForm()
        return render(solicitud,'ingreso_modadm.html', {"form": form})

##### informacion de contacto
#crear informaciond e contacto
class infousucontCreate(CreateView):
    model = usu_inf_contac
    form_class = frm_reg_usu_cont
    template_name = 'registro_usuario/crearinfocontc.html'
    success_url = reverse_lazy('index_usu')

#listar informacion e contacto
class listar_inf_cont(ListView):
    def inf_cont(self, solicitud, id_usu):
        contacto = usu_inf_contac.objects.filter(id_usu=id_usu)
        return render(solicitud,"cn_infocont_usu.html", {'contacto':contacto})

#modificar infrmacion de contacto
class infousucontUpdate(UpdateView):
    model = usu_inf_contac
    form_class = frm_reg_usu_cont
    template_name = 'registro_usuario/crearinfocontc.html'
    success_url = reverse_lazy('index_usu')


##### informacion de formacion academica
#crear formacion academica
class infoacadusuRegis(CreateView):
    model = form_acad
    form_class = frm_reg_usu_acad
    template_name = 'crearinfoacad.html'
    success_url = reverse_lazy('index_usu')

#listar informacion formacion academica
class listar_formacad_cont(ListView):
    def form_acad(self, solicitud, id_usu):
        formacion = form_acad.objects.filter(id_usu=id_usu)
        return render(solicitud,"cn_formacad_usu.html", {'formacion':formacion})

#modificar infrmacion de contacto
class formacad_usuModif(UpdateView):
    model = form_acad
    form_class = frm_reg_usu_acad
    template_name = 'crearinfoacad.html'
    success_url = reverse_lazy('index_usu')


##### informacion de formacion academica
#crear formacion academica
class infopers_usuRegis(CreateView):
    model = usu_inf_pers
    form_class = frm_reg_usu_pers
    template_name =  'crearinfopers.html'
    success_url = reverse_lazy('index_usu')



class func_usu():
    #clase que me almacena las vistas de la aplicacion registro de usuario
    def vst_ls_modf_usu(self, solicitud):
        plt = loader.get_template('sl_usu.html')
        respuesta = plt.render()
        return HttpResponse(respuesta)

class vst_selc_usu_cons(vts_ls_usu):
    #funcion que me pinta la lista para modificar el usuario
    template_name = 'sl_usu.html'
    success_url = reverse_lazy('sl_usu.html')

class vst_mod_reg_usu(UpdateView):
    #clase que me modifca los usuarios para registro de usuario
    model = User
    form_class = frm_con_usu
    template_name = 'nvo_usu_prb.html'
    success_url = reverse_lazy('consulta_usuarios')

class vts_reg_usu_su(CreateView):
    #Clase que devuelve un formulario para registro de usuario
    form_class = frm_con_usu
    template_name = 'nvo_usu_prb.html'
    success_url = reverse_lazy('consulta_usuarios')
    success_message = "El usuario fue creado correctamente"

class infoperslList(ListView): #heredaa de listwview
    model = usu_inf_pers
    template_name = 'moduloAdm/usuarios/infopers.html'

class infopersCree(CreateView):
    model = usu_inf_pers
    form_class = frm_reg_usu_pers
    template_name = 'moduloAdm/usuarios/crearinfopers.html'
    success_url = reverse_lazy('infopers')


class infopersCreate(CreateView):
    model = usu_inf_pers
    form_class = frm_reg_usu_pers
    template_name = 'backend/registro_usuario/crearinfopers.html'
    success_url = reverse_lazy('infopers')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.id_usu = self.request.User
        self.object.save()
        return super(infopersCreate, self).form_valid(form)

class infopersUpdate(UpdateView):
    model = usu_inf_pers
    form_class = frm_reg_usu_pers
    template_name = 'moduloAdm/usuarios/crearinfopers.html'
    success_url = reverse_lazy('infopers')

class infopersDelete(DeleteView):
    model = usu_inf_pers
    template_name = 'moduloAdm/usuarios/verificacion.html'
    success_url = reverse_lazy('infopers')

#class Torneo_ListView(ListView):
#    template_name = 'torneos/torneo_listar.html'

#    def get_queryset(self, *args, **kwargs):
#        return Torneo.objects.filter(user=self.request.user)

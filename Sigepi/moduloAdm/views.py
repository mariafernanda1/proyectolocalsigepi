from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.core import serializers
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import *
from .models import *
from .form import *

class front():
    def v_inicio(self, solicitud):
        #vista de inicio
        plt=loader.get_template('index.html')
        ctx=Context()
        respuesta=plt.render()
        return HttpResponse(respuesta)

"""
def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'moduloAdm/aplicativos/index.html')
"""

class RegistroUsuario(CreateView):
    model = User
    form_class = formregistro
    template_name = 'moduloAdm/usuarios/crearusu.html'
    success_url = reverse_lazy('usu')

class UsuList(ListView): #heredaa de listwview
    model = User
    template_name = 'moduloAdm/usuarios/usu.html'

class UsuUpdate(UpdateView):
    model = User
    form_class = formregistro
    template_name = 'moduloAdm/usuarios/crearusu.html'
    success_url = reverse_lazy('usu')

class UsuDelete(DeleteView):
    model = User
    template_name = 'moduloAdm/usuarios/verificacion.html'
    success_url = reverse_lazy('usu')

class permisoViewSet(viewsets.ModelViewSet):
    serializer_class = PermisosSerializer
    queryset = Permiso.objects.all()

class moduloViewSet(viewsets.ModelViewSet):
    serializer_class = ModelSerializer
    queryset = mod.objects.all()

class funcionViewSet(viewsets.ModelViewSet):
    serializer_class = FuncionSerializer
    queryset = func_app.objects.all()

class rolViewSet(viewsets.ModelViewSet):
    serializer_class = RolSerializer
    queryset = rol.objects.all()

class appViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    queryset = app_mod.objects.all()


 class Torneo_ListView(ListView):
     template_name = 'torneos/torneo_listar.html'

    def get_queryset(self, *args, **kwargs):
        return Torneo.objects.filter(user=request.user)


class Torneo_CreateView(CreateView):
    model = Torneo
    form_class = TorneoForm
    template_name = "torneos/torneo_crear.html"
    succes_url = reverse_lazy('torneos:torneo_listar')

#models.py
class Torneo(models.Model):
	user = models.ForeignKey(User)
	descripcion = models.CharField(max_length=200)

	def __str__(self):
		return (self.descripcion)



############################################################3
 #para llamar a todos los objetos del rol en tipo fucniones
"""
def iniciorol(request):
    roles = rol.objects.all()
    contexto = {
        'roles':roles
    }
    return render(request,'roles/roles.html',contexto)

def crearrol(request):
    if request.method == 'GET':
        form = RolForm()
        contexto = {
            'form':form
        }
    else:
        form = RolForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('roles/roles')
    #    print(form) verificar en consola si llego

    return render(request,'roles/crearrol.html',contexto)

def editarRol(request,id):
    roles = rol.objects.get(id_rol = id)
    if request.method == 'GET':
        form = RolForm(instance = roles)
        contexto = {
            'form':form
        }
    return render(request,'roles/crearrol.html',contexto)


def eliminarrol(request, id):
    roles = rol.objects.get(id_rol = id)
    roles.delete()
    return redirect('roles/roles')
"""

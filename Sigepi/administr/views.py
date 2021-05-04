from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.core import serializers
from django.views.generic import ListView
from rest_framework import viewsets
from .serializers import *
from .models import *
from .form import *

def Home(request):
    return render(request,'index.html')




def Caracterizacion_estudianteUpdate(request, estudiante_id, caracterizacion_id):

    caracterizacion = Caracterizacion.objects.get(id=caracterizacion_id)
    estudiante = Estudiante.objects.get(id=estudiante_id)

    semestres = Semestre.objects.exclude(id__in = estudiante.caracterizacion_set.values_list('semestre'))
    semestres |= Semestre.objects.filter(id=caracterizacion.semestre.id)

    if request.method == 'POST':
        form = CaracterizacionForm(request.POST, instance=caracterizacion)
        if form.is_valid():
            form.save()
            # recargo la pagina cuando se guarda la caracterizacion
            return redirect('caracterizacion_estudiante:list', estudiante_id=estudiante_id)
    else:
        form = CaracterizacionForm(instance=caracterizacion)
        form.fields['semestre'].queryset = semestres
        contexto = {
            'estudiante': estudiante,
            'form': form,
        }
        return render(request, 'caracterizacion/caracterizacion_update_form.html',

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


     #permiso

def iniciopermisos(request):
    permisos = Permiso.objects.all()   #para llamar a todos los objetos del rol
    print(permisos)
    contexto = {
        'permisos':permisos
    }
    return render(request,'permisos/permisos.html',contexto)

def crearpermiso(request):
    if request.method == 'GET':
        form = PermisoForm()
        contexto = {
            'form':form
        }
    else:
        form = PermisoForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('permisos/permisos')
    #    print(form) verificar en consola si llego
    return render(request,'permisos/crearpermiso.html',contexto)

def editarpermiso(request, id):
    permisos = Permiso.objects.get(id_permisos = id)
    if request.method == 'GET':
        form = PermisoForm(instance = permisos)
        contexto = {
            'form':form
        }
    else:
        form = PermisoForm(request.POST, instance =permisos)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('permisos/permisos')
    return render(request,'permisos/crearpermiso.html',contexto)

def eliminarpermiso(request, id):
    permisos = Permiso.objects.get(id_permisos = id)
    permisos.delete()
    return redirect('permisos/permisos')


#############################################
#objetos de fuentes

def iniciofuentes(request):
    fuentes =  func_app.objects.all()   #para llamar a todos los objetos del rol
    print(fuentes)
    contexto = {
        'fuentes':fuentes
    }
    return render(request,'fuentes.html',contexto)

def crearfuente(request):
    if request.method == 'GET':
        form = FuentForm()
        contexto = {
            'form':form
        }
    else:
        form = FuentForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('fuentes')
    #    print(form) verificar en consola si llego
    return render(request,'crearfuentes.html',contexto)

def editarfuente(request, id):
    fuentes = func_app.objects.get(id_func = id)
    if request.method == 'GET':
        form = FuentForm(instance = fuentes)
        contexto = {
            'form':form
        }
    else:
        form = FuentForm(request.POST, instance =fuentes)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('fuentes')
    return render(request,'crearfuentes.html',contexto)

def eliminarfuente(request, id):
    fuentes = func_app.objects.get(id_func = id)
    fuentes.delete()
    return redirect('fuentes')



############################################################3
 #para llamar a todos los objetos del rol
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


###############################################################
 #para llamar a todos los objetos del app

def inicioapp(request):
    app_modelos = app_mod.objects.all()   #para llamar a todos los objetos del rol
    print(app_modelos)
    contexto = {
        'app_modelos':app_modelos
    }
    return render(request,'app.html',contexto)

def crearapp(request):
    if request.method == 'GET':
        form = AppForm(request.POST)
        contexto = {
            'form' : form
        }
    else:
        form = AppForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('app')
    return render(request,'crearapp.html', contexto)

def editarApp(request, id):
    app_modelos = app_mod.objects.get(id_app = id)
    if request.method == 'GET':
        form = AppForm(instance = app_modelos)
        contexto = {
            'form':form
        }
    else:
        form = AppForm(request.POST, instance =app_modelos)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('app')
    return render(request,'crearapp.html',contexto)

def eliminarApp(request, id):
    app_modelos = app_mod.objects.get(id_app = id)
    app_modelos.delete()
    return redirect('index')

##################################333333

# modelos
def inicio(request):
    modelos = mod.objects.all()   #para llamar a todos los objetos del rol
    print(modelos)
    contexto = {
        'modelos':modelos
    }
    return render(request,'index.html',contexto)

def crearmod(request):
    if request.method == 'GET':
        form = ModForm(request.POST)
        contexto = {
            'form' : form
        }
    else:
        form = ModForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crearmod.html', contexto)

def editarMod(request, id):
    modelos = mod.objects.get(id_mod = id)
    if request.method == 'GET':
        form = ModForm(instance = modelos)
        contexto = {
            'form':form
        }
    else:
        form = ModForm(request.POST, instance =modelos)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crearmod.html',contexto)

def eliminarMod(request, id):
    modelos = mod.objects.get(id_mod = id)
    modelos.delete()
    return redirect('index')


###############################################################
 #vistas basadas en clasess

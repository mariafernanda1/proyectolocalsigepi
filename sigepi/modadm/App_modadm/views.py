from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.core import serializers
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from .serializers import *
from .models import *
from .form import *
from modcons.App_cons.form import frm_con_mod, frm_con_app,frm_con_func, frm_con_func, frm_con_func_app
from modcons.App_cons.views import vts_ls_mod, vts_ls_app,vts_ls_func, vts_ls_func_app


class backend():
     # inicio del index
    def modadm(self,solicitud):
        return render(solicitud,'index_adm.html')

class backend_prb():
     # inicio del index prueba
    def modadmprb(self,solicitud):
        return render(solicitud,'index_adm_prb.html')

def funcionrelaciones(solicitud):
    #milista = app_mod.objects.all()
    #milista = rl_func_app.objects.filter(id_app__pk=1)
#    milista = rl_func_app.objects.filter(id_app__titulo='App_modadm')
    milista = rl_func_app.objects.filter(id_app__titulo__icontains='App_modadm')
    print(milista)
    contexto ={
        'milista':milista
    }
    return render(solicitud,'cnsl_generic.html',contexto)



class crearrolfunc():

    def crearfuncrol(self, solicitud):
        resultado = solicitud.GET.get('id_app_sel',None)
    #    contexto1 = rl_func_app.filtroporidapp(self,resultado)
    #    contexto2 = rol.flt_x_idpp(self, resultado)
    #    print(contexto1)
    #    print(contexto2)
        if solicitud.method == 'POST':
            form = funciongrupForm(solicitud.POST)
            #print(form)
            if form.is_valid():
                #form.fields['id_func'] = form.cleaned_data.get("id_func")
                #form.fields['id_rol'] = form.cleaned_data.get("id_rol")
            #    edit_coins = request.POST.getlist('edit-coins')
            #    form.fields['id_func'] = solicitud.POST.id_func("id_func")
                form.save()
            return redirect('consulta_app')
        else:
        #    resultado = solicitud.GET.get('id_app_sel',None)
            form = funciongrupForm(solicitud.GET)
            form.fields['id_rol'].queryset = rol.flt_x_idpp(self, resultado)
            form.fields['id_func'].queryset = rl_func_app.fl_id_app(self,resultado)
        return render(solicitud, 'nvo_func_rol_prb.html',{'form':form})

        #    form.fields['id_rol'] = contexto2["objetos"]
        #    form.field['id_grup'] = contexto2["objetos"].objects.get.all()
        #    form.field['id_func'] = contexto1["objetos"].objects.get.all()
    #        form.fields['sub_code'].queryset = Subcode.objects.filter(code=form.cleaned_data['code'])
        #form.fields['id_func'] = contexto1["objetos"].values_list
        #form.fields['id_rol'] = contexto2["objetos"].values_list

        #form.fields['id_rol'].choices = contexto2["objetos"]
        #form.fields['id_func'].choices = contexto1["objetos"]
        #    form.fields['id_rol'].values = rl_func_app.filtroporidapp(self,resultado)
        #formset = AuthorFormSet(queryset=Author.objects.filter(name__startswith='O'))
            #id_func = forms.ModelChoiceField(queryset= rl_func_app.objects.filter(id_app__titulo='App_modadm'))
        #    print(ls_obj)
        #    h = form.fields["id_func"].queryset=app_mod.objects.filter(id_app__titulo__icontains='App_modadm')
        #    print(h)




class pasar1():

    def pasar(self, solicitud):
        resultado = solicitud.GET.get('id_app_sel',None)
        milista = rl_func_app.objects.filter(id_app__pk=resultado)
        print(milista)
        contexto ={
            'milista':milista
        }
        return render(solicitud,'cnsl_generic.html',contexto)

#class vts_reg_func_rol(CreateView):
#    #clase que me registra todos las funciones otra prueba
#    model = rl_func_group_rol
#    template_name = 'nvo_func_rol_prb.html'
#    form_class = frm_func_grupo
#    success_url =  reverse_lazy('ls_modificar_func_app')
#    success_message = 'creado satisfactoriamente'



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

                    #login_serializer = self.serializer_class(data = solicitud.data, context = {'solicitud':solicitud})
                #    if login_serializer.is_valid():
                #     user = login_serializer.validated_data['user']
                    token, created = Token.objects.get_or_create(user_id = user_id)
                    #user_serializer = UserTokenSerializer(usuario)
                    #if created:
                    #    return Response({
                    #        'token': token.key,
                    #        'user': user_serializer.data
                    #            }, status = status.HTTP_201_CREATED)
                    #else:
                    #    token.delete()
                    #    token = token.objects.create(user= usuario)
                    #    return Response({
                    #        'token': token.key,
                    #        'user': user_serializer.data
                    #        }, status = status.HTTP_201_CREATED)
                    login(solicitud, usuario)
                    #solicitud.session.['usuariosesi'] = User.id
                    messages.success(solicitud,F"bienvenido {nombreusu}")
                    return render(solicitud,'index_adm_prb.html')
                else:
                    messages.success(solicitud,F"los datos son incorrectos")
        form = AuthenticationForm()
        return render(solicitud,'ingreso_modadm.html', {"form": form} )

    def vst_cerrar(self, solicitud):
        logout(solicitud)
        messages.success(solicitud,"tu sesión ha cerrado ")
        form = AuthenticationForm()
        return render(solicitud,'ingreso_modadm.html', {"form": form})

class sesion():
#funcion que me trae el id del usuario que ha iniciado sesion
    def sesionusu(self, solicitud,*args, **kwargs):
        session_key = solicitud.session.session_key
        session = Session.objects.get(session_key=session_key)
        idusu = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=idusu)
        print (user.id)
        return render(sesion)
        pass


class vts_listarapp(ListView):
    model = app_mod
    form_class = app_modForm
    template_name = 'nvo_func_grup.html'
    success_url = reverse_lazy('nvo_func_grup.html')
    success_message = 'listado cargado correctamente'



## modulos
class vts_reg_mod(CreateView):
    #clase que almacena los modulos generales del sistema
    form_class = frm_con_mod
    template_name = 'nvo_mod_prb.html'
    success_url = reverse_lazy('cons_mod')
    success_message = 'el modelo creado satisfactoriamente'

class vst_selc_mod_cons(vts_ls_mod):
    #funcion que me pinta la lista para modificar el modulo
    template_name = 'sl_mod.html'
    success_url = reverse_lazy('cons_mod')

class vst_modf_reg_mod(UpdateView):
    #clase que me modifca los modulos para registro de usuario
    model = mod
    form_class = frm_con_mod
    template_name = 'nvo_mod_prb.html'
    success_url =  reverse_lazy('cons_mod')

#aplicaciones
class vts_reg_app(CreateView):
    #clase que me registra todas las aplicaciones
    form_class = frm_con_app
    template_name = 'nvo_app_prb.html'
    success_url =  reverse_lazy('consulta_app')
    success_message = 'el modelo creado satisfactoriamente'

class vst_selc_app_cons(vts_ls_app):
    #funcion que me pinta la lista para modificar el aplicativo
    template_name = 'sl_app.html'
    success_url = reverse_lazy('consulta_app')

class vst_modf_reg_app(UpdateView):
    #clase que me modifca los modulos para registro de aplicaciones
    model = app_mod
    form_class = frm_con_app
    template_name = 'nvo_app_prb.html'
    success_url =  reverse_lazy('consulta_app')


# funciones  por aplicativos
class vts_reg_func_app(CreateView):
    #clase que me registra todos las funciones  por Aplicativos
    form_class = frm_con_func_app
    template_name = 'nvo_func_app_prb.html'
    success_url =  reverse_lazy('con_func_app')
    success_message = 'creado satisfactoriamente'




class vst_selc_func_app_cons(vts_ls_func_app):
#funcion que me pinta la lista para modificar los funciones por Aplicativos
    form_class = frm_con_func_app
    template_name = 'sl_func_app.html'
    success_url = reverse_lazy('con_func_app')

class vst_modf_reg_func_app(UpdateView):
    #clase que me modifca los modulos para registro los funciones por Aplicativos
    model = rl_func_app
    form_class = frm_con_func_app
    template_name = 'nvo_func_app_prb.html'
    success_url =  reverse_lazy('con_func_app')



#class vts_ls_func_rol_grup(ListView):
#    #clase que  me lista todos las funciones segun los roles del Sistema
#    model = rl_func_rol
#    form_class = frm_con_func_app_rol
#    template_name = 'cn_func_app_rol.html'
#    success_url = reverse_lazy('cn_func_app_rol.html')
#    success_message = 'listado cargado correctamente'




class funcionLista(ListView):
    # funciones del sistema listar
    model = func_app
    form_class = frm_con_func
    template_name = 'nvo_func_rol_prb.html'

# funciones del sistema
class vts_reg_func(CreateView):
    #clase que me registra todos las funciones
    form_class = frm_con_func
    template_name = 'nvo_func_prb.html'
    success_url =  reverse_lazy('consulta_funciones')
    success_message = 'creado satisfactoriamente'

class vst_selc_func_cons(vts_ls_func):
    #funcion que me pinta la lista para modificar las funciones
    form_class = frm_con_func
    template_name = 'sl_func.html'
    success_url = reverse_lazy('consulta_funciones')

class vst_modf_reg_func(UpdateView):
    #clase que me modifca los modulos para registro las funciones
    model = func_app
    form_class = frm_con_func
    template_name = 'nvo_func_prb.html'
    success_url =  reverse_lazy('consulta_funciones')




#no sirvio
#class app():
#    def ver_app(self, solicitud):
#      # form = appForm()
#       if solicitud.method == "POST":
#          form = appForm(solicitud.POST)
#          print(form)
#          if form.is_valid:
#             #redirect to the url where you'll process the input
#             return render(solicitud,'nvo_func_rol_prb.html', {"form": form})
            # return HttpResponseRedirect(reverse_lazy('nvo_func_rol_prb.html') # insert reverse or url
#    pass




# funciones segun roles del sistema no sirvio
#class vts_reg_func_rol(CreateView):
#    #clase que me registra todos las funciones
#    form_class = frm_con_func_app_rol
#    second_form_class = frm_app
#    template_name = 'nvo_func_rol_prb.html'
#    success_url =  reverse_lazy('consulta_roles_func')
#    success_message = 'creado satisfactoriamente'

#    def get_context_data(self, **kwargs):
#        context = super(vts_reg_func_rol, self).get_context_data(**kwargs)
#        if 'form' not in context:
#            context['form'] = self.form_class(self.request.GET)
#        if 'form2' not in context:
#            context['form2'] = self.second_form_class(self.request.GET)
#            pass
#    def post(self, request, *args, **kwargs):
#        self.object = self.get_object
#        form = self.form_class(request.POST)
#        form2 = self.second_form_class(request.POST)
#        if form.is_valid() and form2.is_valid():

#            pass
#            return HttpResponseRedirect(self.get_success_url())
#        else:
#            return self.render_to_response(self.get_context_data(form=form, form2=form2))
#            pass


# funciones segun roles del sistema
#class vts_reg_func_rol1(CreateView):
    #clase que me registra todos las funciones
#    form_class = frm_con_func_app_rol
#    second_form_class = frm_app
#    template_name = 'nvo_func_rol_prb.html'
#    success_url =  reverse_lazy('consulta_roles_func')
#    success_message = 'creado satisfactoriamente'

#    def get_context_data(self, **kwargs):
#        context = super(vts_reg_func_rol, self).get_context_data(**kwargs)
#        if 'form' not in context:
#            context['form'] = self.form_class(self.request.GET)
#        if 'form2' not in context:
#            context['form2'] = self.second_form_class(self.request.GET)

#    def post(self, request, *args, **kwargs):
#        self.object = self.get_object
#        form = self.form_class(request.POST)
#        form2 = self.second_form_class(request.POST)
#        if form.is_valid() and form2.is_valid():
#            pass
#            return HttpResponseRedirect(self.get_success_url())
#        else:
#            return self.render_to_response(self.get_context_data(form=form, form2=form2))
#        HttpResponse
#        pass



class vst_selc_func_rol_cons():
    #funcion que me pinta la lista para modificar las funciones por roles
    #form_class = frm_con_func_app_rol
    #template_name = 'sl_func_app_rol.html'
    #success_url = reverse_lazy('consulta_roles_func')
    pass

class vst_modf_reg_func_rol(UpdateView):
    #clase que me modifica el registro las funciones segun los roles
#    model = rl_func_rol
#    form_class = frm_con_func_app_rol
#    template_name = 'nvo_func_rol_prb.html'
#    success_url =  reverse_lazy('consulta_roles_func')
    pass

class funcionList(ListView):
    # funciones del sistema listar
    model = func_app
    template_name = 'backend/registro_mod/funciones/funciones.html'

class funcionCreate(CreateView):
    #crear funciones del sistema
    model = func_app
    form_class = funcionForm
    template_name = 'backend/registro_mod/funciones/crearfunciones.html'
    success_url = reverse_lazy('funciones')

class funcionUpdate(UpdateView):
    #modificar funciones del sistema
    model = func_app
    form_class = funcionForm
    template_name = 'backend/registro_mod/funciones/crearfunciones.html'
    success_url = reverse_lazy('funciones')

class funcionDelete(DeleteView):
    # eliminar funciones del sistema
    model = func_app
    template_name = 'backend/registro_mod/funciones/verificacion.html'
    success_url = reverse_lazy('funciones')

class ingreso1():

    def vst_ingreso(self, solicitud):
        if solicitud.method == "POST":
            form = AuthenticationForm(solicitud, data=solicitud.POST)
            if form.is_valid():
                nombreusu = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                usuario = authenticate(solicitud, username = nombreusu, password = password)
                if usuario is not None:
                    login(solicitud, usuario)
                    messages.success(solicitud,F"bienvenido {nombreusu}")
                    return render(solicitud,'index_adm_prb.html')
                else:
                    messages.success(solicitud,F"los datos son incorrectos")
        form = AuthenticationForm()
        return render(solicitud,'ingreso_modadm.html', {"form": form} )
    pass

    def vst_cerrar(self, solicitud):
        logout(solicitud)
        messages.success(solicitud,"tu sesión ha cerrado ")
        form = AuthenticationForm()
        return render(solicitud,'ingreso_modadm.html', {"form": form})
    pass

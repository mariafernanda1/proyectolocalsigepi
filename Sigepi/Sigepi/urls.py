from django.contrib import admin
from django.urls import path, include
from administr.views import *
from administr.class_view import *
from administr.urls import *
from rest_framework.routers import DefaultRouter

#from administr.views import inicio, inicio2, inicioapp, crearrol, crearmod, editarRol, crearapp, editarMod,editarApp, eliminarMod,eliminarApp
#inicio nombre de la funcion importada e viw de adminityr

router = DefaultRouter()
router.register(r'permisosj', permisoViewSet)
router.register(r'modelosj', moduloViewSet)
router.register(r'rolesj', rolViewSet)
router.register(r'appsj', appViewSet)
router.register(r'funcionesj', funcionViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('home/',Home, name = 'index'),
    path('adm/', include('administr.urls')),

    ]

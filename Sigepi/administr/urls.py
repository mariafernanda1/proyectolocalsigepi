from django.urls import path, include
from administr.views import *
from administr.class_view import *
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
#    path('admin/', admin.site.urls),
#    path('',inicio,name = 'index'),
#    path('home/',Home, name = 'index'),

    path('aplicativo/',AplicativoList.as_view(), name = 'aplicativo'),
    path('crear_aplicativo/',AplicativoCreate.as_view(), name = 'crearaplicativo'),
    path('editar_aplicativo/<int:pk>/',AplicativoUpdate.as_view(), name='editaraplicativo'),
    path('eliminar_aplicativo/<int:pk>/',AplicativoDelete.as_view(), name='eliminaraplicativo'),

    path('permisos/',PermisoList.as_view(), name = 'permisos'),
    path('crear_permiso/',PermisosCreate.as_view(), name = 'crearpermiso'),
    path('editar_permiso/<int:pk>/',PermisosUpdate.as_view(), name='editarpermiso'),
    path('eliminar_permiso/<int:pk>/',PermisosDelete.as_view(), name='eliminarpermiso'),

    path('app/',AppList.as_view(), name = 'app'),
    path('crear_app/',AppCreate.as_view(), name = 'crearapp'),
    path('editar_app/<int:pk>/',AppUpdate.as_view(), name='editarapp'),
    path('eliminar_app/<int:pk>/',AppDelete.as_view(), name='eliminarapp'),

    path('roles/', RolList.as_view(), name = 'roles'),
    path('crear_rol/', RolCreate.as_view(), name = 'crearrol'),
    path('editar_rol/<int:pk>/', RolUpdate.as_view(), name='editarRol'),
    path('eliminar_rol/<int:pk>/',RolDelete.as_view(), name='eliminarrol'),

    path('usuarios/',UsuList.as_view(), name = 'usu'),
    path('crear_usu/',UsuCreate.as_view(), name = 'crearusu'),
    path('editar_usu/<int:pk>/',UsuUpdate.as_view(), name='editarusu'),
    path('eliminar_usu/<int:pk>/',UsuDelete.as_view(), name='eliminarusu'),

    path('modulos/',modList.as_view(), name = 'mod'),
    path('crear_mod/',modCreate.as_view(), name = 'crearmod'),
    path('editar_mod/<int:pk>/',modUpdate.as_view(), name='editarmod'),
    path('eliminar_mod/<int:pk>/',modDelete.as_view(), name='eliminarmod'),

    path('rlmodulorol/',modrolList.as_view(), name = 'modrol'),
    path('crear_modrol/',modrolCreate.as_view(), name = 'crearmodrol'),
    path('editar_modrol/<int:pk>/',modrolUpdate.as_view(), name='editarmodrol'),
    path('eliminar_modrol/<int:pk>/',modrolDelete.as_view(), name='eliminarmodrol'),

    path('fuentes/',iniciofuentes, name = 'fuentes'),
    path('crear_fuente/',crearfuente, name = 'crearfuente'),
    path('editar_fuente/<int:id>/',editarfuente, name='editarfuente'),
    path('eliminar_fuente/<int:id>/',eliminarfuente, name='eliminarfuente'),



#    path('eliminar_rol/<int:id>/',eliminarRol, name='eliminarrol'),
#    path('<int:user_id>/', account_view, name="view"),

]

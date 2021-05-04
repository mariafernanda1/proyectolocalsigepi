from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from crum import get_current_user
from modadm.App_modadm.base_models import Basemodels

#roles segun el modulo Adminitrativo
ROL_APP_MODADM = [
    (0, 'Adminitrador de sigepi', 'rol_adm_sigepi'),
    (1, 'Adminitrador del módulo administrativo', 'rol_adm_modadm'),
    (2, 'Adminitrador de Institución', 'rol_adm_usui'), #ojo preguntar
    (3, 'Administrador de grupo', 'rol_adm_usugr'), #preguntar
    (4, 'Usuario Sigepi', 'rol_usu_sigepi'),
    ]


#Tipo de rol dentro de la plataforma
TIPO_ROL = [
    (0,'Sistema'),
    (1,'Módulo'),
    (2,'Aplicación'),
    (3,'Extensión'),
    (4,'Otro')
    ]

#Tipos de números de identificación personal
TIPO_NUIP_CO = [
    (0,'Cédula de Ciudadanía'),
    (1,'Tarjeta de Identidad'),
    (2,'Cédula de Extranjería'),
    (3,'Pasaporte'),
    (4,'Permiso de Residencia')
    ]

#Tipos de número de Único de Identificación Institucional
TIPO_NUII_CO = [
    (0,'NIT'), #Número de Identificación tributaria (Colombia)
    (1,'RUT') #Registro Único Tributario.
    ]

#Tipos de Identidad de Género
GENERO = [
    (0,'Neutro'),
    (1,'Femenino'),
    (2,'Masculino'),
    (3,'Intergénero'),
    (4,'Transgénero'),
    (5,'Sisgénero'),
    (6,'Otro')
    ]

#tipo de formación Académica
TIPO_FORM_CO = [
    (0,'Universitaria'),
    (1,'Especializacion'),
    (2,'Maestría'),
    (3,'Doctorado'),
    (4, 'PHD'),
    (5,'Posdoctorado'),
    (6,'Básica Secundaria'),
    (7,'Básica Primaria'),
    (8,'Diplomado'),
    (9,'Curso Corto'),
    (10,'Técnica'),
    (11,'tecnológica'),
    (12,'Curso libre')
    ]

#tipo de formación Académica para grupos
TIPO_FORM_GR = [
    (0,'Seminario'),
    (1,'Taller'),
    (2,'Foro'),
    (3,'Charla'),
    (4,'Encuentro'),
    (5,'Simposio'),
    (6,'Panel'),
    (7,'Conferencia'),
    (8,'Diplomado'),
    (9,'Curso Corto'),
    (10,'Congreso'),
    (11,'Socialización'),
    (12,'Coloquio'),
    (13,'Otro')
    ]

#tipo de modalidad de formación Académica
MODALIDAD = [
    (0,'Presencial'),
    (1,'Virtual'),
    (2,'Semipresencial'),
    (3,'A distancia'),
    (4,'Aprendizaje Acompañado')
    ]

#Tipo de Contratación
TIPO_CONTR_CO = [
    (0,'Término Indefinido'),
    (1,'Término Fijo'),
    (2,'Temporal'),
    (3,'Orden de Servicio'),
    (4,'Contrato de Obra'),
    (5,'Asesoría'),
    (6,'Consultoría'),
    (7,'independiente')
    ]


#Tipos de gupos de Investigación
TIPO_GR_INV = [
    (0,'Independiente'), #Grupo registrado en la plataforma como independiente, asociación de usuarios de la plataforma.
    (1,'Reconocido Inst'), #Grupo que además de registrado está vinculado y reconocido por una Institución o Entidad.
    (2,'Reconocido COLC'), #Grupo que además de registrado está vinculado y reconocido por Colciencias.
    (3,'Semillero de Inv.'), #Grupo que está reconocido como semillero por una Institución o Entidad.
    (4,'Comunidad'), #Grupo de comunidad de conocimiento abierto o libre. Con o sin cuotas de participación.
    (5,'Estado del Arte') #Grupo orientado a la construcción de estados del arte temáticos. Son grupos de comunidades abiertas con vinculación temporal y cuotas de participación.
    ]

#Integrantes según modelo de Colciencias
INTEGR_GR_COLC = [
    (0,'Investigador Emérito'), # Cumple con las características de Investigador Emérito - Se le asigna vinculación.
    (1,'Investigador Sénior'), # Cumple con las características de Investigador Sénior - Se le asigna vinculación.
    (2,'Investigador Asociado'), # Cumple con las características de Investigador Asociado - Se le asigna vinculación.
    (3,'Investigador Junior'), # Cumple con las características de Investigador Junior - Se le asigna vinculación.
    (4,'Integrante vinculado'), # Cumple con las características de Integrante vinculado con doctorado - Se le asigna vinculación.
    (5,'Estudiante de doctorado'), # Cumple con las características de Estudiante de doctorado - Se le asigna vinculación.
    (6,'Integrante vinculado'), # Cumple con las características de Integrante vinculado con maestría o especialidad clínica - Se le asigna vinculación."":
    (7,'Estudiante de maestría o especialidad clínica'), # Cumple con las características de Estudiante de maestría o especialidad clínica - Se le asigna vinculación."":
    (8,'Integrante vinculado con especialización'), # Cumple con las características de Integrante vinculado con especialización - Se le asigna vinculación.
    (9,'Integrante vinculado con pregrado'), # Cumple con las características de Integrante vinculado con pregrado - Se le asigna vinculación.
    (10,'Estudiante de pregrado'), # Cumple con las características de Estudiante de pregrado - Se le asigna vinculación.
    (11,'ninguna de las anteriores') # No cumple ninguna de las anteriores características - Se vincula como Integrante vinculado.
    ]

#Estado de desarrollo del grupo.
ESTADO_DLLO_GR = [
    (0,'Creado'), #El grupo apenas se está convocando y aún no ha culminado al etapa de conformación.
    (1,'Desarrollo Temprano'),
    (2,'Dearrollo Medio'),
    (3,'Desarrollo Alto'),
    (4,'Consolidado'),
    (5,'Ramificado'),
    (6,'Fusionado'),
    (7,'Disgregado'),
    (8,'Disuelto'),
    (9,'liquidado'),
    (10,'Abandonado')
    ]

#Tipo de Institución o entidad
TIPO_INS = [
    (0,'Privada'),
    (1,'Publica'),
    (2,'xxx'),
    (3,'zzzz'),
    ]


#Sector Económico
SECTOR_ECO = [
    (0,'Privado'),
    (1,'Publico'),
    (2,'xxx'),
    (3,'zzzz'),
    ]

# Tipo de fuente de inst. Externa, local, remota.
TIPO_FUENTE = [
    (0,'Externa'),
    (1,'Local'),
    (2,'Remota')
    ]

 #Numerar las posibles extensiones del archivo de instalación 1=".zip";2=".gz",3=".deb";4=".exe"; etc)
TIPO_EXTEN = [
    (0,'.Zip'),
    (1,'.Gz'),
    (2,'.ded'),
    (3,'.exe'),
    (4,'otro'),
    ]

#LIstado de  Horarios
HORARIO = [
    (0,'8am 12pm'),
    (1,'2pm 6pm'),
    (2,'8am 12pm - 2pm 6pm')
    ]

 #Modulo Adminitrativo

class mod(Basemodels):
    # clase que almacena todos los modelos del sistema
    id_mod = models.AutoField(primary_key = True) # Identificador único del módulo
    titulo = models.CharField('Título del módulo', max_length=40, null=False, blank = False) # Título del módulo ej. "Administración Plataforma"
    desc  = models.CharField('descripcion del Módulo', max_length=50, null=False, blank = False) # descripcion del Módulo
    url_doc = models.URLField('url Documentación', null=False, blank=False) # sitio url # direción local a la documentación o manual del módulo.
    version = models.DecimalField('Versión de desarrollo ', max_digits=4, decimal_places=2, null=False, blank = False) # Versión de desarrollo del Módulo ej. "0.01.04"
    activo = models.BooleanField('Activo', default=False) # estatus de la aplicacion para indicar  el modulo de Administración
    instalado = models.BooleanField('¿el módulo se encuentra instalado?', default=False) # ¿el módulo se encuentra instalado? sí =True; no= False.
    visible = models.BooleanField('¿Activa o desactiva la visibilidad de la aplicacion.?', default=False)  # Activa o desactiva la visibilidad de la aplicacion.
    ls_param_cnf = models.CharField('Listado de parámetro de configuración', max_length=100, null=False, blank = False, default='0')

    class Meta:
        verbose_name = 'mod'
        verbose_name_plural = 'mods'

    def __str__(self):
        return '{}'.format(self.titulo)

#funcion para identificar el usuario que agrego o modifico un registro en la tabla mod (auditoria)
    def save(self,force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_crear = user
            else:
                self.user_modif = user
            super(mod, self).save()

class func_app(models.Model):

    id_func = models.AutoField(primary_key = True) # identificador único de función
    nom_func = models.CharField('Nombre de la función: ', max_length=30, null=True, blank = True) # Nombre de la función
    lib_func = models.CharField('Librería que contiene la función: ', max_length=30, null=True, blank = True) # Librería que contiene la función
    url_loc = models.URLField('Direción local a la documentación o manual de la aplicación', null=True, blank=True)  # Direción local donde se encuentra la librería que contiene la función
    com_exc = models.CharField('Comando de Ejecución de la Función: ', max_length=20, null=True, blank = True) # Comando de Ejecución de la Función
    text = models.CharField('Nombre de Función para menús o etiquetas.: ', max_length=80, null=True, blank = True) # Nombre de Función para menús o etiquetas.
    context = models.CharField('Contexto: ', max_length=20, null=True, blank = True) # Nombre de Función para menús contextuales o emergentes y panel de inf.
    activa = models.BooleanField('¿Activa o desactiva.?', default=False)  # La función está activa o desactiva.
    indice = models.IntegerField() #Índice de selección, para navegar con el tabulador.

    def clear(self):
        pass

    def save(self,*args, **kwargs):
        #aqui va lo que queremos validar, si queremos validadr antes
        #que se guarde aqui y si es despues se coloca despues de
        #del super
        super(func_app, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'func_app'
        verbose_name_plural = 'func_apps'

    def __str__(self):
        return '{}'.format(self.nom_func)

class app_mod(models.Model):
    #Clase que almacena los datos del objeto aplicación, las aplicaciones son unidades de
    id_app = models.AutoField(primary_key = True)  # Identificador único de la aplicación.
    titulo = models.CharField('Título de la aplicacion: ', max_length=100, null=False, blank = False) # Título de la aplicacion ej. "Editor de Texto SABER"
    desc  = models.CharField('Descricion de la aplicacion ', max_length=80, null=False, blank = False) # descripcion de la Aplicación.
    url_doc = models.URLField('Direción local a la documentación o manual de la aplicación', null=False, blank=False)  # direción local a la documentación o manual de la aplicación.
    version = models.DecimalField('Versión de desarrollo de la aplicación: ', max_digits=4, decimal_places=2, null=False, blank = False)  # Versión de desarrollo de la aplicación. "0.01.04"
    mod_prin = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)# Id del módulo principal con el cual se integra.
    ver_mod = models.DecimalField('Versión de desarrollo de la aplicación: ', max_digits=4, decimal_places=2, null=False, blank = False)  # Versión mínima del módulo principal con la que la actual versión de la aplicación es compatible.
    activo = models.BooleanField('estatus de la aplicacion ', default=False)# estatus de la aplicacion para indicar  el modulo de Administración
    instalada = models.BooleanField('¿La aplicación se encuentra instalada? ', default=False) # ¿La aplicación se encuentra instalada? sí =True; no= False.
    visible = models.BooleanField('¿Activa o desactiva la visibilidad de la aplicacion.?', default=False)  # Activa o desactiva la visibilidad de la aplicacion.


#NOTA: #nota ls_func foranea, rol
    class Meta:
        verbose_name = 'app_mod'
        verbose_name_plural = 'app_mods'

    def __str__(self):
        return '{}'.format(self.titulo)

class rol(Group):
    # roles del sistema
#    id_rol = models.AutoField(primary_key = True) # Identificador único del Rol
    etq_rol = models.CharField('Etiqueta: ', max_length=30, null=True, blank = True) # Etiqueta del Rol
    desc = models.CharField('Descripcion del Rol: ', max_length=150, null=True, blank = True) # Descripcion del Rol
    tipo = models.IntegerField(null = True, blank = True, choices = TIPO_ROL, default = 0) # Ver diccionario TIPO_ROL
    #id_sis = models.ForeignKey(listado_aplicativo, on_delete=models.CASCADE, null=False, blank =False)  #Identificador de sistema
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=True, blank =True)  #Identificador de Módulo
    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=True, blank =True)  #Identificador de Aplicación
#    id_ext_mod = models.ForeignKey(ext_mod, on_delete=models.CASCADE, null=True, blank =True)  #Identificador de Extensión de módulo
#    id_ext_app = models.ForeignKey(ext_app, on_delete=models.CASCADE, null=True, blank =True)  #Identificador de Extensión de aplicación
    req_reg = models.BooleanField('¿Activa o desactiva.?', default=False) # Variable que indica si require registro en aplicativo o plataforma o no.

    class Meta:
        verbose_name = 'rol'
        verbose_name_plural = 'rols'


    def __str__(self):
        return '{}'.format(self.etq_rol)

#funcion para filtrar por id app (aplicacion)
    def flt_x_idpp(self, id_app):
        seleccion = rol.objects.filter(id_app = id_app)
    #    contexto = {
    #        'objetos' : seleccion
    #        }
        return  seleccion

class rl_func_rol(models.Model): #Listado de funciones y roles que estan ligados a esas funciones

    id = models.AutoField(primary_key = True)
    id_rol = models.ForeignKey(rol,on_delete=models.CASCADE, null=False, blank =False, default= 0)# grupos de django
    id_func = models.ForeignKey(func_app, on_delete=models.CASCADE, null=True, blank =True)
    reg_bd = models.BooleanField('requiere registrar en la base de datos', default=True)

    class Meta:
        verbose_name = 'rl_func_rol'
        verbose_name_plural = 'rl_func_rol'

    def __str__(self):
        return '{}'.format(self.id_func)


class rl_func_app(models.Model): #Listado de funciones propias de la aplicacion, objetos de la clase func_app().

    id = models.AutoField(primary_key = True)
    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False, default= 0)#  identificador de la aplicacion
    id_func =  models.ForeignKey(func_app, on_delete=models.CASCADE, null=False, blank =False)#) # Listado de funciones propias del módulo, objetos de la clase func_app().

    #funcion para filtrar por id app
    def fl_id_app(self, id_app):
        seleccion = rl_func_app.objects.filter(id_app = id_app)
        #contexto = {
        #    'objetos' : seleccion
        #    }
        return  seleccion

    class Meta:
        verbose_name = 'rl_func_app'
        verbose_name_plural = 'rl_func_apps'

class rl_mod_app_mod(models.Model):  # relacion Listado de id de aplicaciones vinculadas al módulo.
    id = models.AutoField(primary_key = True)
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)
    ls_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)

    class Meta:
        verbose_name = 'rl_mod_app_mod'
        verbose_name_plural = 'rl_mod_app_mods'

##############
#class rl_app_mod_mod(models.Model): #Listado de id de módulos a los que está vinculada la aplicación esta repetiad ojooooooo
#    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)#
#    ls_mods = models.ForeignKey(mod,on_delete=models.CASCADE, null=False, blank =False) # Listado de id de módulos a los que está vinculada la aplicación


class rl_app_mod_func(models.Model): # relacion Listado de funciones propias del módulo, objetos de la clase func_app().
    id = models.AutoField(primary_key = True)
    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)#
    ls_func =  models.ForeignKey(func_app, on_delete=models.CASCADE, null=False, blank =False)#) # Listado de funcion

    class Meta:
        verbose_name = 'rl_app_mod_func'
        verbose_name_plural = 'rl_app_mod_funcs'

#este usuario no se esta utilizando ojo...
class User(AbstractUser):

#    id_rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=True, blank =True)  # Identificador del  módulo# Identificador del Rol de Usuario de Sistema
    fch_regi = models.DateField('fecha de registro', auto_now = False,  null=True, blank =True) # fecha de registro de usurio
    activo = models.BooleanField('¿Activo o desactivado.?', default=False,  null=True, blank =True) # estatus del usuario activo (True) inactivo (False)


class mod_adm(models.Model):
# verificar inicio de sesion de django ojo, django todo
    id = models.AutoField(primary_key = True)
    sesion = models.CharField('Sesion: ', max_length=150, null=True, blank = True)# # código o número de id_sesion
    #ls_sesion = [] # listado de sesiones activas
    #log_sesion = [] # listado del registro de sesiones
    id_usu_adm = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank =False) # Id del usuario Super Administrador de la plataforma
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)
    # nota preguntar mod.__init__(self), donde tomo las sesiones activas etc
    class Meta:
        verbose_name = 'mod_adm'
        verbose_name_plural = 'mod_adms'
    pass


class log_acc_mod(models.Model):

    id_log_acces = models.AutoField(primary_key = True)  # Identificador único de registro de acceso
    id_usu = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank =False)  # Identificador único de usuario
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)  # Identificador del  módulo
    fch_ini = models.DateField('fecha de inicio', auto_now = False)  # fecha de inicio formato AAAA-MM-DD-HH:MM
    fch_fin = models.DateField('fecha de fin', auto_now = False)  # fecha de finalización formato AAAA-MM-DD-HH:MM

    class Meta:
        verbose_name = 'log_acc_mod'
        verbose_name_plural = 'log_acc_mods'

class log_acc_pltf(models.Model):

    id_acc_pltf = models.AutoField(primary_key = True)  # Identificador único
    id_usu = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank =False) # Identificador único de usuario
    fch_ini = models.DateField('fecha de inicio', auto_now = False) # fecha de inicio formato AAAA-MM-DD-HH:MM
    fch_fin = models.DateField('fecha de fin', auto_now = False) # fecha de finalización formato AAAA-MM-DD-HH:MM

    class Meta:
        verbose_name = 'log_acc_pltf'
        verbose_name_plural = 'log_acc_pltfs'

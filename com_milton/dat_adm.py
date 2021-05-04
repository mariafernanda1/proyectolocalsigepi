#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado: 06-05-2021
Última Modificación: 13-04-2021
Modificado por: Milton castro
Hora:5:00 am

Módulo de Administración para la Plataforma Icogniaa
Contiene el modelo de datos para las aplicaciones:
    -Administración
        -Registro de Usuarios
        -Registro de Grupos
        -Registro de Institución
        -Registro de Patrocinadores (sin maquetar)
        -Registro de Beneficiarios (sin maquetar)
"""

"""
Listas únicas, Conjuntos y Diccionarios del Módulo de Administración
"""
#Tipo de rol dentro de la plataforma
TIPO_ROL={
    "sistema":0,
    "Módulo":1,
    "Aplicación":2,
    "Extensión":3,
    "otro":4
    }

#Tipos de números de identificación personal
TIPO_NUIP_CO={
    "Cédula de Ciudadanía":0,
    "Tarjeta de Identidad":1,
    "Cédula de Extranjería":2,
    "Pasaporte":3,
    "Permiso de Residencia":4
    }

#Tipos de número de Único de Identificación Institucional
TIPO_NUII_CO={
    "NIT":0, #Número de Identificación tributaria (Colombia)
    "RUT":1 #Registro Único Tributario.
    }

#Tipos de Identidad de Género
GENERO={
    "Neutro":0,
    "Femenino":1,
    "Masculino":2,
    "Intergénero":3,
    "Transgénero":4,
    "Sisgénero":5,
    "otro":6
    }

#tipo de formación Académica
TIPO_FORM_CO={
    "Universitaria":0,
    "Especializacion":1,
    "Maestría":2,
    "Doctorado":3,
    "PHD":4,
    "Posdoctorado":5,
    "Básica Secundaria":6,
    "Básica Primaria":7,
    "Diplomado":8,
    "Curso Corto":9,
    "Técnica":10,
    "tecnológica":11,
    "Curso libre":12
    }

#tipo de formación Académica para grupos
TIPO_FORM_GR={
    "Seminario":0,
    "Taller":1,
    "Foro":2,
    "Charla":3,
    "Encuentro":4,
    "Simposio":5,
    "Panel":6,
    "Conferencia":7,
    "Diplomado":8,
    "Curso Corto":9,
    "Congreso":10,
    "Socialización":11,
    "Coloquio":12,
    "otro":13
    }

#tipo de modalidad de formación Académica
MODALIDAD={
    "Presencial":0,
    "Virtual":1,
    "Semipresencial":2,
    "A distancia":3,
    "Aprendizaje Acompañado":4
    }

#Tipo de Contratación
TIPO_CONTR_CO={
    "Término Indefinido":0,
    "Término Fijo":1,
    "Temporal":2,
    "Orden de Servicio":3,
    "Contrato de Obra":4,
    "Asesoría":5,
    "Consultoría":6,
    "independiente":7
    }

#Tipos de gupos de Investigación
TIPO_GR_INV={
    "Independiente":0, #Grupo registrado en la plataforma como independiente, asociación de usuarios de la plataforma.
    "Reconocido Inst.":1, #Grupo que además de registrado está vinculado y reconocido por una Institución o Entidad.
    "Reconocido COLC":2, #Grupo que además de registrado está vinculado y reconocido por Colciencias.
    "Semillero de Inv.":3, #Grupo que está reconocido como semillero por una Institución o Entidad.
    "Comunidad":4, #Grupo de comunidad de conocimiento abierto o libre. Con o sin cuotas de participación.
    "Estado del Arte":5 #Grupo orientado a la construcción de estados del arte temáticos. Son grupos de comunidades abiertas con vinculación temporal y cuotas de participación.
    }

#Integrantes según modelo de Colciencias
INTEGR_GR_COLC={
    "Investigador Emérito":1, # Cumple con las características de Investigador Emérito - Se le asigna vinculación.
    "Investigador Sénior":2, # Cumple con las características de Investigador Sénior - Se le asigna vinculación.
    "Investigador Asociado":3, # Cumple con las características de Investigador Asociado - Se le asigna vinculación.
    "Investigador Junior":4, # Cumple con las características de Investigador Junior - Se le asigna vinculación.
    "Integrante vinculado":5, # Cumple con las características de Integrante vinculado con doctorado - Se le asigna vinculación.
    "Estudiante de doctorado":6, # Cumple con las características de Estudiante de doctorado - Se le asigna vinculación.
    "Integrante vinculado":7, # Cumple con las características de Integrante vinculado con maestría o especialidad clínica - Se le asigna vinculación."":
    "Estudiante de maestría o especialidad clínica":8, # Cumple con las características de Estudiante de maestría o especialidad clínica - Se le asigna vinculación."":
    "Integrante vinculado con especialización":9, # Cumple con las características de Integrante vinculado con especialización - Se le asigna vinculación.
    "Integrante vinculado con pregrado":10, # Cumple con las características de Integrante vinculado con pregrado - Se le asigna vinculación.
    "Estudiante de pregrado":11, # Cumple con las características de Estudiante de pregrado - Se le asigna vinculación.
    "ninguna de las anteriores":12 # No cumple ninguna de las anteriores características - Se vincula como Integrante vinculado.
    }

#Estado de desarrollo del grupo.
ESTADO_DLLO_GR={
    "Creado":0, #El grupo apenas se está convocando y aún no ha culminado al etapa de conformación.
    "Desarrollo Temprano":1,
    "Dearrollo Medio":2,
    "Desarrollo Alto":3,
    "Consolidado":4,
    "Ramificado":5,
    "Fusionado":6,
    "Disgregado":7,
    "Disuelto":8,
    "liquidado":9,
    "Abandonado":10
}

#Tipo de Institución o entidad
TIPO_INS={

}

#Sector Económico
SECTOR_ECO={

}

"""
Clases del Módulo de Adminsitración
"""

class mod():
    #Clase que almacena los datos del objeto módulo, los módulos son unidades de organización funcional que agrupan aplicaciones con una unidad funcional.
    #No se debe confundir con el módulo de administración de Django, aunque debe interactuar con ese módulo.
    def __init__(self):
        self.id_mod = 0 # Identificador único del módulo
        self.titulo = "" # Título del módulo ej. "Administración Plataforma"
        self.desc  = "" # descripcion del Módulo
        self.url_doc = "" # direción local a la documentación o manual del módulo.
        self.version = "" # Versión de desarrollo del Módulo ej. "0.01.04"
        self.ls_app = [] # Listado de id de aplicaciones vinculadas al módulo.
        self.ls_rol = [] # Listado de id de roles vinculados al módulo.
        self.activo = False # estatus de la aplicacion para indicar  el modulo de Administración
        self.instalado = False # ¿el módulo se encuentra instalado? sí =True; no= False.
        self.ls_param_cnf =[] # Listado de parámetro de configuración objetos de la clase param_config().
        self.ls_func = [] # Listado de funciones propias del módulo, objetos de la clase func_app().
        self.visible = False # Activa o desactiva la visibilidad de la aplicacion.

    def agregar_mod(self):
        pass

    def elim_mod(self):
        pass

    def modif_mod(self):
        pass

    def info_mod(self):
        pass

    def __str__(self):
        pass

class app_mod():
    #Clase que almacena los datos del objeto aplicación, las aplicaciones son unidades de
    #funcionamiento autónomo que se agrupan en módulos extendiendo la funcionalidad del módulo.
    #Debe corresponder a una app o micro servicio de un Framework como Django o Laravel y debe permitir su interacción.

    def __init__(self):
        self.id_app = 0 # Identificador único de la aplicación.
        self.titulo = "" # Título de la aplicacion ej. "Editor de Texto SABER"
        self.desc  = "" # descripcion de la Aplicación.
        self.url_doc = "" # direción local a la documentación o manual de la aplicación.
        self.version = "0.0.0" # Versión de desarrollo de la aplicación. "0.01.04"
        self.mod_prin = 0 # Id del módulo principal con el cual se integra.
        self.ver_mod = "0.0.0" # Versión mínima del módulo principal con la que la actual versión de la aplicación es compatible.
        self.ls_mods = [] # Listado de id de módulos a los que está vinculada la aplicación
        self.activo = False # estatus de la aplicacion para indicar  el modulo de Administración
        self.instalada = False # ¿La aplicación se encuentra instalada? sí =True; no= False.
        self.ls_param_cnf =[] # Listado de parámetro de configuración objetos de la clase param_config().
        self.ls_func = [] # Listado de funciones propias del módulo, objetos de la clase func_app().
        self.ls_rol = [] #listado de los diferentes id_rol de aplicación para los cuales la aplicación estará activa.
        self.visible = False # Activa o desactiva la visibilidad de la aplicacion.

    def agregar_app(self):
        pass

    def elim_app(self):
        pass

    def modif_app(self):
        pass

    def info_app(self):
        pass

    def __str__(self):
        pass

class ext_mod(mod):
    #Clase que almacena los datos de las Extensiones.
    pass

class ext_app(app_mod):
    #Clase que almacena los datos de las Aplicaciones Externas o Plugins.
    pass

class param_config():
    #Clase que almacena los datos del ojeto parámetro de configuración.
    pass

class func_app():
    #Clase que contiene los campos del objeto función de aplicación.
    #Permite listar las acciones, procesos o funciones que se pueden ejecutar en un Módulo, una Aplicación o Extensión.
    #Facilita la asignación de permisos por tipo de usuario en la unidades funcionales.

    def __init__(self):
        self.id_func = 0 # identificador único de función
        self.nom_func ="" # Nombre de la función
        self.lib_func ="" # Librería que contiene la función
        self.url_loc ="" # Direción local donde se encuentra la librería que contiene la función
        self.com_exc ="" # Comando de Ejecución de la Función
        self.text = "" # Nombre de Función para menús o etiquetas.
        self.tecrap = "" # Combinación de teclas rápidas para acceder a la función
        self.context = "" # Nombre de Función para menús contextuales o emergentes y panel de inf.
        self.activa = False # La función está activa o desactiva.
        self.ls_rol_bd = [[0,False,True,False,False]]
        #listado de los diferentes id_rol de aplicación para los cuales la función estará activa.
        #[,False,,,]¿genera registro en base de datos?;[,,True,,] Permiso de lectura en BD
        #[,,,False,]Permiso de excritura en BD.[,,,,False]Permiso de Ejecución.
        self.indice = 0 #Índice de selección, para navegar con el tabulador.
        self.ico = "" #Nombre delícono con extensión.

    def agregar_func():
        pass

    def elminar_func():
        pass

    def editar_func():
        pass

    def info_func():
        pass

    def __str__(self):
        pass

class mod_adm(mod):
    #Clase que almacena los datos de operación del Módulo de Administración de la plataforma Icogniaa
    #No se debe confundir con el módulo de administración de Django, aunque debe interactuar con ese módulo.
    #Hereda de la clase mod().
    ls_sesion = [] # listado de sesiones activas
    log_sesion = [] # listado del registro de sesiones
    id_usu_adm = 0 # Id del usuario Super Administrador de la plataforma

    def __init__(self):
        mod.__init__(self)
        self.sesion = "" # código o número de id_sesion

    def crear_mod_adm(self):
        pass

    def elim_Modulo_adm(self):
        pass

    def modif_Modulo_adm(self):
        pass

    def __str__(self):
        pass

class adm_install():
    # Clase que permite adminsitrar e instalar Módulos, Aplicaciones o Extensiones propias de la plataforma o externas.

    def __init__():
        pass

    def instalar_fuente():
        # Agrega una fuente de isntalación
        pass

    def instalar_mod(self):
        pass

    def instalar_app(self):
        pass

    def instalar_ext(self):
        pass

class fuente_ins():
    #Clase que contiene los campos del objeto fuente de instalación.
    def __init__():
        self.id_rep = 0 #identificador de repositorio o fuente de instalación
        self.tipo = 0 # Tipo de fuente de inst. Externa, local, remota.
        self.tipo_arch = 0 # Numerar las posibles extensiones del archivo de instalación 1=".zip";2=".gz",3=".deb";4=".exe"; etc)
        self.url_loc ="" # dirección local relativa
        self.url_rem =""
        self.url =""
        self.log = [] # lista de valores: archivo,id app o mod, dir relativa
        self.valid = False # fuente validada o no
        self.ls_param_cnf =[] # Listado de parámetro de configuración objetos de la clase param_config().

    def agregar_fnt_inst():
        pass

    def eliminar_fnt_inst():
        pass

    def editar_fnt_inst():
        pass

    def info_fnt_inst():
        pass

    def __str__(self):
        pass

class rol():
    # Clase que contiene los campos del objeto rol.

    def __init__(self):
        self.id_rol   = 0 # Identificador único del Rol
        self.etq_rol = "" # Etiqueta del Rol
        self.desc = "" # Descripcion del Rol
        self.tipo = 0 # Ver diccionario TIPO_ROL
        self.id_sis = 0 #Identificador de sistema
        self.id_mod = 0 #Identificador de Módulo
        self.id_app = 0 #Identificador de Aplicación
        self.id_ext_mod = 0 #Identificador de Extensión de módulo
        self.id_ext_app = 0 #Identificador de Extensión de aplicación
        self.req_reg = False # Variable que indica si require registro en aplicativo o plataforma o no.

    def crear_rol(self):
        pass

    def elim_rol(self):
        pass

    def modif_rol(self):
        pass

    def info_rol():
        pass

    def __str__(self):
        pass

class log_acc_mod():
    # Clase que almacena y procesa el acceso a los diferentes Módulos

    def __init__(self):
        self.id_log_acces = 0 # Identificador único de registro de acceso
        self.id_usu = 0 # Identificador único de usuario
        self.id_mod =  0 # Identificador del  módulo
        self.fch_ini = 0 # fecha de inicio formato
        self.fch_fin = 0 # fecha de finalización formato

    def reg_log_accesos_mod(self):
        #registrar neuvo log de acceso
        pass

    def sel_reg_acc_mod_usu():
        #Seleccionar log de registros de accesos a módulo de usuario
        pass

class log_acc_pltf():
    # Clase que almacena y procesa los registros del acceso a la plataforma
    def __init__(self):
        self.id_acc_pltf = 0 # Identificador único
        self.id_usu = 0 # Identificador único de usuario
        self.fch_ini = 0 # fecha de inicio
        self.fch_fin = 0 # fecha de finalización

    def reg_log_acces_platf(self):
        pass

    def sel_reg_acc_pltf_usu():
        #Seleccionar log de registros de accesos a plataforma de usuario
        pass


""""
Clases de la Aplicación Registro de Usuarios
"""
class usu():
    # Clase base que almacena y procesa la información para iniciar sesion del usuario en el sistema.
    def __init__(self):
        self.id_usu = 0 # Identificador único
        self.usuario  = "" # Nick o identificador de usuario
        self.pasw  = "" # contraseña
        self.id_rol_sis = 0 # Identificador del Rol de Usuario de Sistema
        self.fch_regi = "" # fecha de registro de usurio
        self.activo = False # estatus del usuario activo (True) inactivo (False)

    def crear_usu(self):
        pass

    def elim_usu(self):
        pass

    def modif_usu(self):
        pass

    def sel_usu():
        #seleccionar usuario
        pass

    def info_usu():
        pass

    def __str__(self):
        pass

class usu_inf_apps(usu):
    # Clase que almacena y procesa la información de la aplicaciones de usuario y sus respectivos roles
    def __init__(self):
        self.id_usu = 0 #id único de Usuario de sistema
        self.ls_roles =[[0,0]] #Listado de roles en aplicaciones y módulos autorizados por administradores de paltaforma
        # [0,] id_rol; [,0] id_usu quien autoriza.
        self.rol_sis = 0 # Identificador de rol de sistema.
        self.app_act = 0 # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión)
        self.rol_act = 0 # identificador del rol actual.

    def agregar_usu_inf_apps(self):
        pass

    def elim_usu_inf_apps(self):
        pass

    def modi_usu_inf_apps(self):
        pass

    def sel_usu_inf_apps():
        pass

    def info_apps():
        pass

    def __str__(self):
        pass

class usu_inf_pers():
    #clase de información personal de usuario.
    def __init__(self):
        self.id_usu = 0  # identificador de usuario
        self.nuip = 0 # número único de identificación personal sin puntos
        self.tipo_nuip = 0 # tipo de Número de identificación personal
        self.nombres = "" # nombres de usuario
        self.apelllidos = "" # apellidos de usuario
        self.nal = "" # nacionalidad
        self.fch_naci = 0  # fecha de nacimiento de usuario
        self.gene = 0 # genero del usuario
        self.ocup = "" # ocupación del usuario
        self.dir = "" # direccion de residencia
        self.discap = False # Es una persona en condición de discapacidad
        self.tipo_discap = 0 # Tipo de  discapacidad
        self.url_imag = "" # url de la imagen personal.
        self.zona_hor = "" #Zona Horario internacional

    def agregar_usu_inf_pers(self):
        pass

    def elim_usu_inf_pers(self):
        pass

    def modf_usu_inf_pers(self):
        pass

    def info_pers():
        pass

    def __str__(self):
        pass

class usu_inf_contac():
    def __init__(self):
        self.id_usu = 0  # identificador de usuario
        self.ind_nal = "" #Indicativo telefónico de país
        self.cel = "" #Número de telefono móvil del usuario
        self.wa = "" # Número de WhatsApp
        self.email = "" # dirección de correo electrónico
        self.cod_post = 0 # Número de código postal
        self.ls_red = [] # Listado de objetos de redes sociales
        self.ls_ha = [] #Listado de Horario de atención [día,hora ini, hora fin]
        self.web = "" # dirección de página web o blog personal
        self.dir_offi = "" # Dirección de Oficina (país, ciudad, dir)

    def agregar_usu_inf_contac(self):
        pass

    def elim_usu_inf_contac(self):
        pass

    def modf_usu_inf_contac(self):
        pass

    def info_contac():
        pass

    def __str__(self):
        pass

class red_soc():
    # Clase que almacena el objeto red social
    def __init__(self):
        self.nombre_red = ""
        self.usuario ="" #nick o dirección de usuario
        self.url = "" #Url de página principal dentro de la red.
        self.uso = 0 #Uso de la red (frecuente:0; moderado:1; poco frecuente:2; inactivo:3)
        self.pub = False #Acceso público de información de red

class usu_inf_acad():
    # Clase que almacena y procesa la información académica del usuario
    def __init__(self):
        self.id_usu = 0 # identificador unico
        self.nivelform = 0 # me indica la formacion que tiene el usuario
        self.ls_form = [] #listado de id procesos de formación realizados
        self.ls_cursdict = [] #LIstado de id Cursos a cargo dictadospor al persona.

    def agregar_usu_inf_acad(self):
        pass

    def elim_usu_inf_acad(self):
        pass

    def modf_usu_inf_acad(self):
        pass

    def info_acad():
        pass

    def __str__(self):
        pass

class form_acad():
    #clase que almacena la información de formación académica de un usuario
    def __init__():
        self.id_fa = 0 #Id de formación académica
        self.id_usu
        self.instit ="" # Nombre de la institucion académica donde curso la formación
        self.tipo_form = 0 #tipo de formación ver diccionario TIPO_FORM
        self.fch_ini = 0
        self.fch_fin = 0
        self.certif = True
        self.nal ="" #país
        self.ciudad = ""
        self.mod = 0 # modalidad
        self.tit = "" # Título obtenido
        self.menc = "" # Mensión de honor
        self.token = "" #Token de validación electrónica de certificación de la formación

class curs_dict():
    #clase que almacena la información de cursos dictados a cargo de un usuario
    def __init__():
        self.id_cd = 0 #Id de formación académica
        self.id_usu = 0
        self.instit ="" # Nombre de la institucion académica donde dictó el curso.
        self.tipo_form = 0 #tipo de formación ver diccionario TIPO_FORM
        self.fch_ini = 0
        self.fch_fin = 0
        self.certif = True
        self.nal ="" #país
        self.ciudad = ""
        self.mod = 0 # modalidad
        self.num_est = 0 #Cantidad de Estudiantes
        self.dur = 0 #Número total de horas académicas del curso
        self.nom_curs = "" #Nombre del Curso
        self.mun_ciclos = 0 #Número de ciclos del curso "cuántas veces se dictó el curso"
        self.url_prog = "" #Url del documento o sitio web donde se puede localizar el programa del curso

class usu_inf_prof():
    # Clase que almacena y procesa la información de la trayectoria profesional del usuario

    def __init__(self):
        self.id_usu = 0 # identificador unico
        self.prof = "" # Profesión Actual
        self.ls_empl =[] #listado de procesos de formación realizados

    def crear_usu_inf_prof(self):
        pass

    def elim_usu_inf_prof(self):
        pass

    def modi_usu_inf_prof(self):
        pass

    def info_usu_prof(self):
        pass

    def __str__(self):
        pass

class empleos():
    #clase que almacena la información de empleos y experiencia profesional de un usuario
    def __init__():
        self.id_empl = 0
        self.id_usu = 0
        self.instit ="" # Nombre de la institucion académica donde curso la formación
        self.nom_cargo = "" #Nombre del Cargo
        self.fch_ini = ""
        self.fch_fin = ""
        self.certif = True
        self.nal ="" #país
        self.ciudad = ""
        self.tipo_contr = 0 #ver diccionario TIPO_CONTR
        self.tit = "" # Título obtenido
        self.menc = "" # Mensión de honor
        self.token = "" #Token de validación electrónica de certificación de la formación
        self.ret = "" # Motivo del retiro

    def crear_usu_empl(self):
        pass

    def elim_usu_empl(self):
        pass

    def modi_usu_empl(self):
        pass

    def info_usu_empl(self):
        pass

    def __str__(self):
        pass

class usu_inf_hab():
    # Clase que almacena la información de las habilidades o conocimientos adquiridos y certificados por el usuario
    def __init__(self):
        self.id_usu= 0 # identificador unico de usuario
        self.ls_habs = [] # listado de id de habilidades registradas por le usuario
        self.descripcion = 0 # descripcion del conocimiento o habilidad investigador

    def crear_usu_inf_hab(self):
        pass

    def elim_usu_inf_hab(self):
        pass

    def modi_usu_inf_hab(self):
        pass

    def info_usu_hab(self):
        pass

    def __str__(self):
        pass

class habilidades():
    #clase que almacena la información de tipos de habilidad
    def __init__():
        self.id_hab = 0
        self.nom_hab = "" #Nombre de la habilidad
        self.desc ="" #Descripción de la Habilidad

    def crear_hab(self):
        pass

    def elim_hab(self):
        pass

    def modi_hab(self):
        pass

    def info_hab(self):
        pass

    def __str__(self):
        pass

class valid_hab():
    #clase que procesa la información de validación social de habilidades
    def __init__():
        self.id_usu = 0 # Identificador del Usuario que registra la habilidad
        self.id_hab = 0 #Identificador de la habilidad que se va a validar
        self.id_usu_val = 0 #Identificador del Usuario que valida la habilidad
        self.id_esc = 0 #Identificador de la escala de validación
        self.val = 0 #Valor dentro del rango de la escala de validación

    def validar_hab(self):
        pass

    def elim_valiid_hab(self):
        pass

    def modi_valid_hab(self):
        pass

    def info_valid_hab(self):
        pass

    def __str__(self):
        pass

class app_reg_usu(app_mod):
    #Clase que contiene los objetos de la App Registro de Usuarios
    def __init__(self):
        pass

    def crear_app_regusu(self):
        pass

    def elim_app_regusu(self):
        pass

    def modi_app_regusu(self):
        pass

    def info_regusu(self):
        pass

    def __str__(self):
        pass


"""
Clases de la Aplicación Registro de Grupos
"""
class usugr():
    #Clase que registra la información básica del usuario grupo en el sistema.
    def __init__(self):
        self.id_gr = 0 #Identificador único del grupo de investigacion.
        self.passgr  = "" # contraseña para el usuario grupo (diferente a la del usuario del sistema)
        self.id_usu_admin = 0 #Identificador del usuario administrador (debe estar registrado y se le asignan permisos de administración de app_reg_gr)
        self.id_rol_app = 0 # Identificador del Rol de Usuario grupo dentro de la app_reg_gr
        self.ls_etp = [] #Listado histórico de etapas que ha tenido el grupo.
        self.ls_int_usu = [] #Listado de id_usu integrantes del grupo registrados en el sistema.
        self.ls_int_nr = [] #Listado de id de integrantes no registrados en el sistema.
        self.ls_pry = [] #Listado de id de proyectos vinculados al grupo de investigación.
        self.ls_prod = [] #Listado de id de productos de investigación vinculados al grupo.
        self.activo = True #El grupo se encuentra activo.

    def crear_gr(self):
        pass

    def elim_gr(self):
        pass

    def modi_gr(self):
        pass

    def info_gr(self):
        pass

    def __str__(self):
        pass

class usugr_inf_apps():
    # Clase que almacena y procesa la información de la aplicaciones de usuario institucional y sus respectivos roles
    def __init__(self):
        self.id_usugr = 0 #id único de Usuario de grupo
        self.ls_roles =[[0,0]] #Listado de roles en aplicaciones y módulos autorizados por administradores de paltaforma
        # [0,] id_rol; [,0] id_usu quien autoriza.
        self.rol_sis = 0 # Identificador de rol de sistema.
        self.app_act = 0 # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión)
        self.rol_act = 0 # identificador del rol actual.

    def agregar_usu_inf_apps(self):
        pass

    def elim_usu_inf_apps(self):
        pass

    def modi_usu_inf_apps(self):
        pass

    def sel_usu_inf_apps():
        pass

    def info_apps():
        pass

    def __str__(self):
        pass

class usugr_inf_gr():
    #clase de información de usuario grupo.
    def __init__(self):
        self.id_usugr = 0  # identificador de usuario grupo
        self.cod_gr = 0 # código único de identificación del grupo
        self.tipo_gr = 0 # tipo de grupo, ver diccionario TIPO_GR_INV
        self.id_etp_gr = 0 # Identificador de etapa vigente del grupo
        self.nal = "" # País principal con el que se identifica el grupo.
        self.dir = "" # direccion de correspondencia.
        self.estado = 0 # Estado de desarrollo del Grupo. Ver diccionario ESTADO_DLLO_GR
        self.url_imag = "" # url de la imagen o logo del grupo.
        self.zona_hor = "" #Zona Horaria internacional
        self.id_gr_padre = 0 #Identificador del grupo padre si lo tiene, de lo contrario es el valor es cero

    def agregar_usu_inf_pers(self):
        pass

    def elim_usu_inf_pers(self):
        pass

    def modf_usu_inf_pers(self):
        pass

    def info_pers():
        pass

    def __str__(self):
        pass

class usugr_inf_contac():
    def __init__(self):
        self.id_usugr = 0  # identificador de usuario grupo
        self.ind_nal = "" #Indicativo telefónico de país
        self.tel = "" #Número de telefono fijo de oficina del grupo
        self.cel = "" #Número celular de contacto del grupo.
        self.email = "" # dirección de correo electrónico del grupo.
        self.cod_post = 0 # Número de código postal de oficina
        self.ls_red = [] # Listado de objetos de redes sociales
        self.ls_hr = [] #Listado de Horario de reunión semanal[día,hora ini, hora fin]
        self.web = "" # dirección de página web o blog del grupo
        self.dir_offi = "" # Dirección de Oficina (país, ciudad, dir)

    def agregar_usu_inf_contac(self):
        pass

    def elim_usu_inf_contac(self):
        pass

    def modf_usu_inf_contac(self):
        pass

    def info_contac():
        pass

    def __str__(self):
        pass

class usugr_inf_acad():
    # Clase que almacena y procesa la información de actividades académicas y oferta formativa del usuario grupo
    def __init__(self):
        self.id_usugr = 0 # identificador único de grupo
        self.ls_form_gr = [] #listado de id procesos de formación realizados
        self.ls_cursofer = [] #listado de id cursos o eventos acadeḿicos ofertados por el grupo.
        self.ls_prod = [] #Listado de id de productos de investigación vinculados al id usugr
        self.ls_pry_inv = [] #Listado de id de proyectos de investigación vinculados al id usugr

class form_acad_gr():
    #clase que almacena la información de formación académica de un usuario grupo
    def __init__():
        self.tipo_form = 0 #tipo de formación ver diccionario TIPO_FORM_GR
        self.fch_ini = 0
        self.fch_fin = 0
        self.certif = True
        self.nal ="" #país
        self.ciudad = ""
        self.mod = 0 # modalidad
        self.asis = 0 # Número de asistentes
        self.hora = 0 # Número de horas académicas
        self.mem = "" #url de las memorias del tipo de formación.
        self.token = "" #Token de validación electrónica de certificación de la formación

class curs_ofer():
    #clase que almacena la información de cursos ofertados por parte de un usuario grupo
    def __init__():
        self.instit ="" # Nombre de la institucion académica que oferta el curso o evento académico.
        self.tipo_form_gr = 0 #tipo de formación ver diccionario TIPO_FORM_GR
        self.fch_ini = 0
        self.fch_fin = 0
        self.certif = True
        self.nal ="" #país
        self.ciudad = ""
        self.mod = 0 # modalidad
        self.num_est = 0 #Cupo de Estudiantes o asistentes
        self.dur = 0 #Número total de horas académicas del curso o evento académico
        self.nom_curs = "" #Nombre del Curso o evento académico.
        self.mun_ciclos = 0 #Número de ciclos del curso "cuántas veces se realizará el curso o evento"
        self.url_prog = "" #Url del documento o sitio web donde se puede localizar el programa del curso o el evento académico.
        self.inscr = "" #Url del formulario de inscripción.

class etapa_gr():
    #Clase que registra las etapas de los grupos de investigación en el sistema.
    def __init__(self):
        self.id_etp_gr = 0 #Identificador único de la etapa del grupo de investigacion.
        self.nom = "" #Nombre del grupo (puede ser el qeu tuvo en algún momento, se pueden registrar varios nombres según al trayectoria del grupo)
        self.fch_ini_nom = 0 #Fecha en la que se creó el grupo con ese nombre, o en el que cambió a ese nombre.
        self.fch_fin_nom = 0 #Fecha en la que se terminó el grupo con ese nombre, o en el que dejó de usar ese nombre.
        self.vig = True #El nombre se encuentra vigente, es el que se usa actualmente el grupo.
        self.sigla = "" #Sigla con la que se identificó(a) el grupo en esta etapa.
        self.url_arch = "" #Url de sitio web o repositorio virtual donde repose el archivo(memoria o sitio web) del grupo.
        self.gruplac = "" #Url del GrupLac del grupo de Investigación con ese nombre si se está registrado en esa plataforma.

    def agregar_etpgr(self):
        pass

    def elim_etpgr(self):
        pass

    def modi_etpgr(self):
        pass

    def info_etpgr(self):
        pass

    def __str__(self):
        pass

class usu_nr():
    #Clase que registra los datos de investigación de un integrante grupo no registrado en el sistema.
    def __init__(self):
        self.id_usu_nr = 0 # identificador unico
        self.nombres = "" # Nombres del integrante no registrado(a).
        self.apellidos = "" # Apellidos del integrante no registrado(a).
        self.rol = 0 #Rol de investigación que se desempeña actualmente
        self.cvlac = "" #URL del CVlac del investigador(a).
        self.orcid = "" #ID de ORCID del investigador(a).
        self.ggl = "" #URL Google académico del investigador(a).

    def crear_usunr(self):
        pass

    def elim_usunr(self):
        pass

    def modi_usunr(self):
        pass

    def info_usunr(self):
        pass

    def __str__(self):
        pass

class app_reg_gr(app_mod):
    #Clase que contiene los objetos de la App Registro de Grupos
    def __init__(self):
        self.id_app = 0 # Identificador único de aplicacion por modulo _administrador
        pass

    def crear__app_reg_gr(self):
        pass

    def elim_app_reg_gr(self):
        pass

    def modi__app_reg_gr(self):
        pass

    def info_app():
        pass

    def __str__(self):
        pass

"""
Clases de la Aplicación Registro de Instituciones
"""

class usui():
    # Clase que almacena y procesa la información de un usuario institucional

    def __init__(self):
        self.id_usuinst = 0 # Identificador único del usuario institucionnal
        self.passinst  = "" # contraseña para el usuario institucional (diferente a la del usuario del sistema)
        self.id_usu_admin = 0 #Identificador del usuario administrador (debe estar registrado y se le asignan permisos de administración de app_reg_ins)
        self.id_rol_app = 0 # Identificador del Rol de Usuario Institucional dentro de la app_reg_ins
        self.fch_regi = "" # fecha de registro de usurio
        self.activo = False # estatus del usuario activo (True) inactivo (False)

    def crear_usui(self):
        pass

    def elim_usui(self):
        pass

    def modi_usui(self):
        pass

    def info_usui():
        pass

    def __str__(self):
        pass


        self.codi_institucion  = "" # codigo con el que esta registrada la institucion
        self.nomb_institucion  = "" # nombre de la institucion
        self.dire_institucion  = 0 # direccion de la institucion
        self.siti_institucion = "" # sitio url

class usui_inf_apps(usui):
    # Clase que almacena y procesa la información de la aplicaciones de usuario institucional y sus respectivos roles
    def __init__(self):
        self.id_usu = 0 #id único de Usuario de sistema
        self.ls_roles =[[0,0]] #Listado de roles en aplicaciones y módulos autorizados por administradores de paltaforma
        # [0,] id_rol; [,0] id_usu quien autoriza.
        self.rol_sis = 0 # Identificador de rol de sistema.
        self.app_act = 0 # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión)
        self.rol_act = 0 # identificador del rol actual.

    def agregar_usu_inf_apps(self):
        pass

    def elim_usu_inf_apps(self):
        pass

    def modi_usu_inf_apps(self):
        pass

    def sel_usu_inf_apps():
        pass

    def info_apps():
        pass

    def __str__(self):
        pass

class usui_inf_inst():
    #clase de información de usuario institucional.
    def __init__(self):
        self.id_usui = 0  # identificador de usuario institucional
        self.nuii = "" # número único de identificación institucional sin puntos
        self.tipo_nuii = 0 # Tipo de Número de identificación Institucional
        self.rs = "" # Razón Social de la Institución
        self.sigla = "" # Sigla institucional
        self.repleg = "" #Nombre Completo del representante legal
        self.nal = "" # nacionalidad
        self.fch_ini = 0  # fecha de inicio de la institución
        self.fch_reg = 0  # fecha de registro de la institución en al plataforma
        self.tipo_inst = 0 # Tipo de institución o entidad. Ver diccionario TIPO_INS
        self.sector = 0 # sector de desempeño de la entidad o institución. Ver Diccionario SECTOR_ECO
        self.dir = "" # direccion sede administrativa
        self.url_imag = "" # url de la imagen institucional o logo.
        self.zona_hor = "" #Zona Horario internacional

    def agregar_usu_inf_pers(self):
        pass

    def elim_usu_inf_pers(self):
        pass

    def modf_usu_inf_pers(self):
        pass

    def info_pers():
        pass

    def __str__(self):
        pass

class usui_inf_contac():
    def __init__(self):
        self.id_usui = 0  # identificador de usuario institucional
        self.ind_nal = "" #Indicativo telefónico de país
        self.tel = "" #Número de telefono fijo del usuario Institucional
        self.cel = "" #Número de telefono móvil del usuario Institucional
        self.email = "" # dirección de correo electrónico de información y contacto
        self.cod_post = 0 # Número de código postal
        self.ls_red = [] # Listado de objetos de redes sociales
        self.ls_ha = [] #Listado de Horario de atención [día,hora ini, hora fin]
        self.web = "" # dirección de página web o blog institucional
        self.dir_pri = "" # Dirección de sede principal (país, ciudad, dir)

    def agregar_usu_inf_contac(self):
        pass

    def elim_usu_inf_contac(self):
        pass

    def modf_usu_inf_contac(self):
        pass

    def info_contac():
        pass

    def __str__(self):
        pass

class usui_inf_acad():
    # Clase que almacena y procesa la información académica del usuario
    def __init__(self):
        self.id_usui = 0 # identificador unico
        self.nivelform = 0 # me indica la formacion que tiene el usuario
        self.ls_progofer = [] #Listado de id de programas ofertados por la entidad o Institución.

    def agregar_usui_inf_acad(self):
        pass

    def elim_usui_inf_acad(self):
        pass

    def modf_usui_inf_acad(self):
        pass

    def info_usui_acad():
        pass

    def __str__(self):
        pass

class prog_ofer():
    #clase que almacena la información de los programas ofertados a cargo de un usuario Institucional
    def __init__():
        self.id_prog = 0 # identificado único de programa.
        self.id_usui = 0 # Id del usuario institucion .
        self.tipo_form = 0 #tipo de formación ver diccionario TIPO_FORM
        self.fch_ini = 0 #Incripciones
        self.fch_fin = 0 #Cierre de Inscripciones
        self.certif = True
        self.nal ="" #país
        self.ciudad = ""
        self.mod = 0 # modalidad
        self.num_est = 0 #Cantidad de Estudiantes
        self.dur = 0 #Número total de horas académicas del programa
        self.dur_sem = 0 #Número total de semestres del programa
        self.nom_prog = "" #Nombre del Programa
        self.acred = True #El programa se encuentra acreditado
        self.ven_acrd = 0 #Año de vencimiento de la acreditación
        self.url_prog = "" #Url del documento o sitio web donde se puede localizar el programa

    def agregar_progofer(self):
        pass

    def elim_progofer(self):
        pass

    def modf_progofer(self):
        pass

    def info_progofer():
        pass

    def __str__(self):
        pass

class usui_inf_inv():
    # Clase que almacena y procesa la información académica del usuario
    def __init__(self):
        self.id_usui = 0 # identificador unico
        self.ls_usugr = [] #Listado de id de grupos de inv. vinculados a la entidad o Institución.
        self.ls_usu = [] #Listado de id de usuarios vinculados a la entidad o Institución.
        self.ls_pry_inv = [] #Listado de id de proyectos de investigación vinculados a la entidad o Institución.
        self.ls_prod_inv = [] #Listado de id de productos de investigación vinculados a la entidad o Institución.
        self.ls_conv_inv = [] #Listado de id de convocatorias de investigación vinculados a la entidad o Institución.

    def agregar_usui_inf_acad(self):
        pass

    def elim_usui_inf_acad(self):
        pass

    def modf_usui_inf_acad(self):
        pass

    def info_usui_acad():
        pass

    def __str__(self):
        pass

class conv_inv():
    #clase que almacena la información de los programas ofertados a cargo de un usuario Institucional
    def __init__():
        self.id_conv = 0 # identificado único de convocatoria.
        self.id_usui = 0 # Id del usuario institucion .
        self.val_min = 0 #valor mínimo
        self.val_max = 0 #valor máximo
        self.fch_ini = 0 #Fecha de inicio Incripciones
        self.fch_fin = 0 #Fecha de Cierre de Inscripciones
        self.pltf = False #Se puede registrar desde la plataforma.
        self.nal ="" #país
        self.ciudad = ""
        self.mod = 0 # modalidad
        self.und_acdm = "" #Nombre de la unidad académica o dependencia encargada de la convocatoria
        self.resp = "" #Nombre de la persona responsable de la convocatoria.
        self.correo = "" #correo electrónico para informacion
        self.nom_conv = "" #Nombre de la convocatoria
        self.url_conv = "" #Url del documento o sitio web donde se puede localizar los términos de al convocatoria.
        self.url_insc = "" #Url del formulario de inscripción.

    def agregar_convinv(self):
        pass

    def elim_convinv(self):
        pass

    def modf_convinv(self):
        pass

    def info_convinv():
        pass

    def __str__(self):
        pass

class app_reg_inst():
    #Clase que contiene los objetos de la App Registro de Instituciones
    def __init__(self):
        self.app_reg_ins = 0 # identificador unico para App Registro de Instituciones
        self.id_aplicacion_administrador  = 0 # Identificador único ddel modulo administrador
        self.nomb_app_reg_ins = "" # nombre de la App Registro de Instituciones
        self.desc_app_reg_ins = "" # descripcion de la App Registro de Instituciones
        self.status_app_reg_ins = False # estatus de la App Registro de Instituciones

    def crear_app_reginst(self):
        pass

    def elim_app_reginst(self):
        pass

    def modi_app_reginst(self):
        pass

    def info_reginst():
        pass

    def __str__(self):
        pass

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado: 06-05-2021
Última Modificación: 13-04-2021
Autor:Milton castro
Hora:04:24

Módulo de Proyectos para SIGEPI
Contiene el modelo de datos para las aplicaciones:
    -Proyectos
        -Registro de Programas de Investigación
        -Registro de Proyectos de Investigación
        -Registro de Productos y Procesos de Investigación
        -Diseño de Investigación
        -Evaluación de Proyectos de Investigación
        -Gestión de Proyectos de Investigación
        -Marco Lógico
"""
from dat_adm import (
    mod,
    mod_adm,
    TIPO_GR_INV,
    TIPO_FORM_GR,
    INTEGR_GR_COLC,
)


"""
Listas únicas, Conjuntos y Diccionarios del Módulo de Proyectos
"""
#tipos de Investigación
TIPO_INV_FIN={
    #por fuente de financiación:
    "Estatal":0, #Recursos Estatales (Públicos)
    "Privada":1, #Recursos privados
    "Personal":2,#Recursos propios
    "Comunitaria":3, #Recursos comunitarios
    "Mixta PUBPRV":4, #Recursos Públicos y Privados
    "Mixta PUBPER":5, #Recursos Públicos y Personales
    "Mixta PUBCOM":6, #Recursos Públicos y Personales
    "otra":7 #Otra categoría de clasificación de financiación
    }

TIPO_INV_INF={
    #Por fuente de información:
    "":0, #Sin información sobre las fuentes
    "Primarias":1, #Los datos son propios y se toman de forma directa
    "Secundarias":2, #Los datos ajenos y se trabaja con fuentes ajenas, no se recolectan datos de forma directa.
    "Estado de la Cuestión":3, #Es un tipo de investigación trasnversal qeu apunta a identificar las producciones documentales realizadas hasta la actualidad sobre un tema de investigación.
    "Mixta":4, #Los datos son propios en más del 50% de los casos y ajenos en el resto.
    "Minería":5, #Se substrae nueva información de cúmulos de datos existentes.
    "Simulación":6, #Se generan datos no experimentales para realizar pruebas simuladas de modelos.
    "otra":7 #Otra categoría de clasificación de fuente de información
    }

TIPO_INV_MET={
    #Por énfasis metodológico:
    "":0, #Sin información sobre el énfasis metodológico
    "Cualitativa":1, #Se fundamenta en métodos cualitativos, estudios de caso, obervación de campo, etnografía, entre otros.
    "Cuantitativa":2, #Su énfasis es cuantitativo, estadístico o probabilístico.
    "Mixta CC":3, #Utiliza métodos cuantitativos y cualitativos de forma simultánea.
    "Experimental":4, #Sus resultados dependen de los experimentos que deben realizarse durante la investigación.
    "Heurística":5, #Se concentra en la ocnstrucción de apoyos a la investigación por medio de principios, reglas y estrategias para resolver problemas qeu aún no cunetan con solución.
    "Exploratoria":6, #Es la primera investigación que se realiza sobre el tema o desde ese enfoque metodológico.
    "Clínica":7, #Es una investigación derivada de una intervención a partir de un diagnóstico con un método ya probado.
    "IAP":8, #Los objetivos,la metodología y los resultados se consensúan con las poblaciones que se intervienen desde la investigación.
    "Teórica":9, #Su proceso de validación no requiere de evidencias empíricas, sino que ssus resultados se validan por sus premisas lógicas, que permiten explroar nuevas formas de comprensión de los fenómenos.
    "otra":10 #Otra categoría de clasificación metodológica.
    }

TIPO_INV_TMP={
    #Por énfasis temporal:
    "":0, #Sin información sobre el periodo de estudio.
    "Histórica":1, #Se busca acercarse a un objeto de estudio desde una continuidad temporal definida por el equipo de investigación.
    "Genealógica":2, #Parte de una exploración multicausal, que puede ser determinada ordenando cronológicamente los sucesos que explican y se relacionan para comprender una situación presente.
    "Actual":3, #Establece la situación actual de un fenómeno y el concoimiento que se tien hasta el momento en que se realiza.
    "Proyectiva":4, #Permite un abordaje temporal donde la investigación tiene previstos objetivos que se logran por medio del proceso de investigación, busca aproximar el resultado a un estado futuro deseado.
    "Prescriptvia":5,#Tiene como principal objetivo la optimizacion de procesos, partiendo de caminos metodológicos o procedimentales ya explorados en contextos determinados.
    "Descriptiva":6, #Se delimitan los aspectos o variables a estudiar, pero se privilegia la perspectiva subjetiva del investigador sobre la observación realizada, por lo general acompañan investigaciónes preeliminares, exploratorias, etnográficas, artísticas o creativas.
    "Prospectiva":7, #Su principal preocupación es el modelado de los posibles desarrollos futuros de los fenómenos, tratando de brindar marcos de predictibilidad.
    "Longitudinal":8, #Es una investigación que se realiza de forma continua o de forma repetida durante un periodo largo de tiempo, con unas variables iniciales que se mantienen en el tiempo.
    "Transversal":9, #Delimita un tiempo determinado para realizar la investigación y puede trabajar multiplicidad de variables.
    "Periódica":10, #Es un tipo de investigación que se realiza con un intervalo de tiempo determinado y que tiene unos objtivos definidos por quienes la realizan o financian.
    "Seccional":11, #Se puede comprender como una variación de un estudio transversal que se reliza por una sola vez.
    "otra":12 #Otra categoría de clasificación temporal
    }

TIPO_INV_VAR={
    #Por los tipos de variables:
    "":0, #Sin información sobre las variables del estudio.
    "Univariada":1, #El objeto de estudio tiene una causalidad definida, determinable y se realiza el seguimiento de una variable central.
    "Multivariada":2, #El objeto de estudio no tiene una causalidad bien definida, y se relaciona con un conjunto finito de variables que pueden ser susceptibles de medirse.
    "Correlacional":3, #Se conocen als principales variables que intervienen en un fenómeno, pero se busca establecer el peso o la incidencia de las varibles en estudio.
    "Estudio de Caso":4, #Permite construir con base en el estudio de casos particulares, la construcción de tendencias o situaciones comunes que brindan correlación y generalización a partir de multiplicidad de estos estudios.
    "Análisis Comparado":5, #Desde unidades de análisis hermenéuticas, permite establecer correlaciones que facilitan la clasificación de objetos y fenómenos a partir del estudio de sus regularidades y correlaciones.
    "Poblacional":6, #Delimita un tiempo determinado para realizar la investigación y puede trabajar multiplicidad de variables.
    "Muestral":7, #Es un tipo de investigación que se realiza con un intervalo de tiempo determinado y que tiene unos objtivos definidos por quienes la realizan o financian.
    "otra":12 #Otra categoría de clasificación por variables.
    }

TIPO_INV_CNT={
    #Por contextos de investigación:
    "":0, #Sin información sobre las variables del estudio.
    "Laboratorio":1, #La investigación se realiza en un entorno controlado (Laboratorio).
    "Campo":2, #La investigación se debe desarrollar en un entorno no controlado (terreno o en el lugar donde tienen lugar los sucesos)
    "Aplicada":3, #Busca construir escenarios de investigación in situ, donde se puedan controlar los procesos que se están investigando.
    "Operaciones o Procesos":4, #Son técnicas de investigación para corrección, intervención u optimización de sistemas dinámicos, que permiten mejorar la funcionalidad y la eficiencia de diseños y estándares, se utilizan generalmente en etapas de desarrollo de productos o líneas de producción ya existentes, así como sistemas dinámicos complejos.
    "Diagnóstica":5, #La investigación diagnóstica se fundamenta en enfoques probabilíticos y estadísticos, donde la causalidad es múltiple con probabilidades de correlación similares, lo que influye en los tratamientos o las alternativas de solución.
    "Metodológica":6, #Son investigaciones que toman como foco de investigación la forma en que se realizan las investigaciones mismas, sus supuestos teóricos, los problemas de medición, o de interpretación de los datos, en general el cómo de las investigaciones.
    "Forense":7, #Es una investigación de corte histórico, busca establecer las situaciones más probables y demostrables, basados en evidencias para establecer responsabiliddes e imputaciones, a los posibles resposables de situaciones punibles o sancionables.
    "otra":8 #Otra categoría de clasificación de contextos
    }

TIPO_INV_LOG={
    #Por énfasis de marco axiológico
    "":0, #Sin información sobre el marco axiológico del estudio.
    "Hermenéutica":1, #Investigación que concentra sus esfuerzos en logar la mejor interpretación del sentido de los registros, en función de los contextos a los cuales se traduce e interpreta.
    "Ontológica":2, #Indaga sobre los problemas de percepción, subjetividad o distorsión de perspectiva por aprte de quienes realizan la investigación, en el desarrollo del proceso investigativo.
    "Epistemológica":3, #Busca establecer el marco conceptual que sirve de paradigma a los planteamientos teóricos y explicativos que sustentan los sujetos investigadores.
    "Holística":4, #La investigación holística reconoce la necesidad de establecer el más amplio márgen de integración de las diferentes perspectivas epistemológicas y hermenéuticas en torno al objeto de estudio.
    "Formal":5, #Es aquella que se realiza de forma sistemática y ajustada a reglas qeu permiten su replicación, reproducción o desarrollo. También se utiliza en campos de ciencias puras con altos grados de abstracción, mediante métodos lógicos de validación.
    "Informal":6, #Es un tipo de investigación qeu debe improvisar de acuerdo a las circusntancias, contextos y posibilidades del investigador o equipo de investigación, para lograr un abordaje del objeto de estudio.
    "Empírica":7, #Se establece en contraposición a la especulación teórica, permitiendo presentar aquello que es sustentable exclusivamente a partir de los hechos registrables, contrastables y comprobables a partir de la experiencia o la experimentación.
    "Analítica":8, #El analisis es el método de investigación que busca la descomposición de las unidades ya reconocidas, como un todo que se descompone en partes que permitan comprender causalidades con un mayor nivel de precisión y certidumbre.
    "Deductiva":9, #La investigación deductiva parte de la premisa de la existencia de una regla general aplicable a la comprensión de un fenómeno, guiando el diseño de los instrumentos y las premisas de la investigación.
    "Inductiva":10, #El proceso de investigación inductiva, parte de una condición particular buscando construir a partir de evidencias las generalziaciones posibles hasta que la evidencia contradiga el marco de explicación que se induce a aprtir de esta.
    "Mixta AD":11, #Investigación que utiliza el marco Analítico-Deductivo en su planteamiento.
    "Mixta ID":12, #Investigación que utiliza el marco Inductivo-Deductivo en su planteamiento.
    "Hipotética":13, #Es una investigación qeu utiliza la construcción de hipótesis para su planteamiento explicativo, metodológico o teórico, la cual tiene por objetivo comprobar o refutar la(s) hipótesis planteada.
    "Actuarial":14, #Es un tipo de investigación que se concentra en los impactos posibles derivados de als actuaciones de diversos actores o fenomenos causales, tanto para explicar como predecir las situaciones presentes y futuras, a paertir del estudio de los datos pasados. Generalemente permite la construcción de modelos.
    "Factorial":15, #Este tipo de investigación se concentra en la determinación de factores que inciden en un determinado fenómeno, desde una perspectiva fundamentalmente estadística. Ha cobrado relevancia con metodologías de minería de datos y big data.
    "Axiológica":16, #Es la investigación qeu se concentra en el peso qeu tienen los actores del proceso investigativo en los resultados y sesgos propios de las investigaciones, derivados de la acción humana en el proceso investigativo.
    "Taxonómica":17, #La investigación Taxonómica tiene por objetivo lograr la mejor clasificación de lso objetos o fenómenos de estudio, permitiendo encontrar inconsistencias, coincidencias, correlaciones o alternativas en el proceso de clasificación de lso objetos de estudio o los fenomenos estudiados.
    "Conceptual":18, #La investigación conceptual fuera del marco de la cognición y la filosofía, hace referencia a explorar modelos de productos que si bien aún no existen podrían entrar a realizarse. Es el paso previo a la construcción de un prototipo.
    "Crítica":19, #La investigación crítica tiene por objetivo encontrar las fisuras e incosistencias de un planteamiento teórico o un modelo existente o propuesto. Cumple una función depuradora de los principios lógicos sobre los que operan las soluciones y los modelos científicos.
    "otra":20 #Otra categoría de clasificación por marco axiológico.
    }

TIPO_INV_CPR={
    #Por énfasis de campo profesional
    "":0, #Sin información sobre el campo profesional de la investigación.
    "Social":1,#investigación propia de las ciencias sociales.
    "Educativa":2, #Investigación de las ciencias de la Educación.
    "Didáctica":3, #Investigación de las ciencias de la Educación.
    "Periodística":4, #Investigación propia de profesionales de periodismo.
    "Artística":5, #Investigación propia de profesionales de arte, diseño, música.
    "Creativa":6, #Es un enfoque de investigación que se concentra en carreras con énfasis creativo, artes plásticas, diseño, arquitectura, literatura, música, ingenierías, comunicación, entre otras.
    "Jurídica":7, #Propia de las disciplinas del Derecho, la Ciencia Política, las Ciencias de la Administración, las ciencias económicas, entre otras.
    "Epidemiológica":8, #Ciencias de la salud y de la administración.
    "Etnográfica":9, #Propia de la Antropología, sociología y ciencias sociales.
    "Lingüística":10, #Específica de la Lingüística, la filología, antropología, sociología, comunicación, entre otras.
    "Semiótica":11, #Tipo característico de ciencias sociales, artes y ciencias de la comunicación.
    "Genética":12, #Investigación propia de las ciencias de la salud, con énfasis en informática.
    "otra":13 #Otra categoría de clasificación por campo profesional.
    }

#Roles en el proceso de investigación.
ROL_INV={
    "":0, #Sin información sobre el rol desempeñado
    "Investigador(a) Principal":1, #Responsable del proyecto y del equipo de investigación.
    "Investigador(a) Sénior":2, #Categoría según Colciencias.
    "Investigador(a) Asociado(a)":3, #Categoría según Colciencias.
    "Investigador(a) Junior":4, #Categoría según Colciencias.
    "Investigador(a) Emérito(a)":5, #Categoría según Colciencias.
    "Jóven Investigador(a)":6, #Participación en convocatorias orientadas a jóvenes.
    "Auxiliar de Investigación":7, #Se participa(ó) en actividades relacionadas con la investigación.
    "Investigador(a) independiente":8, #No se ha estado vinculado institucionalmente, pero se cuenta con productos de investigación.
    "Par Externo(a)":9, #Persona externa al grupo que cumple funciones de validación, crítica o evaluación de la investigación
    "Jurado":10, #Persona encargada de evaluar la sustentación de una investigación. Generalmente Tesis
    "Director(a)":11, #Persona encargada de dirigir un trabajo de investigación. Generalmente Tesis o Trabajo de Grado
    "Codirector(a)":12, #Persona encargada de codirgir un trabajo de investigación. Generalmente Tesis o Trabajo de Grado
    "Asesor(a)":13, #Persona encargada de asesorar un trabajo de investigación. Generalmente Tesis o Trabajo de Grado
    "Evaluador(a)":14, #Persona encargada de evaluar un trabajo de investigación. Generalmente Tesis o Trabajo de Grado
    "Consultor(a)":15, #Persona encargada de orientar o aportar una solución especializada para un trabajo de investigación.
    "Tutor(a)":15 #Persona encargada de orientar un trabajo de investigación.
    }

"""
Clases del Módulo Proyectos de SIGEPI
"""
class mod_pry(mod):
    #Clase que contiene los objetos del módulo proyectos de SIGEPI
    def __init__(self):
        self.id_mod_pry   = 0 # Identificador único
        self.nomb_mod_pry = '' # nombre de la aplicacion
        self.desc_mod_pry  = '' # descripcion del aplicacion
        self.status_mod_pry = False # estatus de la aplicacion

    def crear_mod_pry(self):
        pass

    def elim_mod_pry(self):
        pass

    def modif_mod_pry(self):
        pass

    def info_modpry(self):
        pass

    def __str__(self):
        pass

"""
Clases de la Aplicación Registro de Proyectos de Investigación
"""

class inf_pry():
        #Clase que contiene toda la informacion referente al proyecto

    def __init__(self):
        self.id_pry = 0 # identificador unico para  App Registro de Proyectos
        self.codigo_pry = '' # Código de identificación del proyecto.
        self.nombre_archivo = '' # Nombre del archivo del proyecto.
        self.url_archivo = '' # Url del archivo del proyecto.
        self.id_lineadeinvestigacion = 0 # Identificador de la linea de investigación
        self.titulo_pry = '' # Título del proyecto.
        self.id_grup_bd = 0  # Identificador del grupo de investigación
        self.id_tipoproyecto = 0 # indentificador unico de tipo de proyecto
        self.num_inv = 1 # Número de investigadores(as) involucrados en el proyecto.
        self.prom_frm = 0 # Nivel de formación promedio del grupo 0:Profesional; 1:esp.; 2:Maestría; 3. Doctorado.
        self.conv = '' # Convenio propuesto o previsto para la realización de la investigación.
        self.dur = 0 # Duración del proyecto valores dentro de un rango.
        self.und_dur = 0 # unidad de medida del rango de tiempo, 0:seg; 1:min; 2:horas; 3:meses; 4:años.
        self.geo = '' # Aŕea geográfica que abarca el proyecto.
        self.resu = '' # Resumen del proyecto.
        self.url_ap = '' # Url de la imágen del árbol de problemas.
        self.url_ao = '' # Url de la imágen del árbol de objetivos.
        self.pobl_bnd = 0 #Tamaño de la ppoblación beneficiaria directa del proyecto.
        self.pobl_bni = 0 #Tamaño de la población beneficiaria indirecta del proyecto.
        self.obj_gen = '' # Objetivo general del proyecto.
        self.obj_esp = '' # Objetivos específicos del proyecto.

    def crear_inf_pry(self):
        pass

    def elim_inf_pry(self):
        pass

    def modif_inf_pry(self):
        pass

class tipos_pry():
    #Clase que contiene los tipos de proyectos Investigación descriptiva y de catalogación.
    #Investigación correlacional, Investigación explicativa, Investigación comparativa

    def __init__(self):
        self.id_tipoproyecto = 0 # indentificador unico de tipo de proyecto
        self.desc_tipoproyecto = '' # descripcionj del tipo de proyecto

    def crear_tipos_pry(self):
        pass

    def elim_tipos_pry(self):
        pass

    def modif_tipos_pry(self):
        pass

class app_reg_pry(app_mod):
    #Clase que contiene los objetos de la App Registro de Proyectos
    def __init__(self):
        self.id_app_reg_pry = 0 # identificador unico para  App Registro de Proyectos
        self.id_id_mod_pry   = 0 # Identificador único ddel modulo proyecto
        self.nomb_app_reg_pry  = '' # nombre de la App Registro de Proyectos
        self.desc_app_reg_pry  = '' # descripcion de la App Registro de Proyectos
        self.status_app_reg_pry  = False # estatus de la App Registro de Proyectos

    def crear_app_reg_pry(self):
        pass

    def elim_app_reg_pry(self):
        pass

    def modif_app_reg_pry(self):
        pass

    def info_mod(self):
        pass

    def __str__(self):
        pass


"""
Clases de la Aplicación Registro de Programas de Investigación
"""

class inf_prog_inv():
        #Clase que contiene toda la informacion referente al proyecto

    def __init__(self):
        self.id_pry = 0 # identificador unico para  App Registro de Proyectos
        self.codigo_pry = '' # Código de identificación del proyecto.
        self.nombre_archivo = '' # Nombre del archivo del proyecto.
        self.url_archivo = '' # Url del archivo del proyecto.
        self.id_lineadeinvestigacion = 0 # Identificador de la linea de investigación
        self.titulo_pry = '' # Título del proyecto.
        self.id_grup_bd = 0  # Identificador del grupo de investigación
        self.id_tipoproyecto = 0 # indentificador unico de tipo de proyecto
        self.num_inv = 1 # Número de investigadores(as) involucrados en el proyecto.
        self.prom_frm = 0 # Nivel de formación promedio del grupo 0:Profesional; 1:esp.; 2:Maestría; 3. Doctorado.
        self.conv = '' # Convenio propuesto o previsto para la realización de la investigación.
        self.dur = 0 # Duración del proyecto valores dentro de un rango.
        self.und_dur = 0 # unidad de medida del rango de tiempo, 0:seg; 1:min; 2:horas; 3:meses; 4:años.
        self.geo = '' # Aŕea geográfica que abarca el proyecto.
        self.resu = '' # Resumen del proyecto.
        self.url_ap = '' # Url de la imágen del árbol de problemas.
        self.url_ao = '' # Url de la imágen del árbol de objetivos.
        self.pobl_bnd = 0 #Tamaño de la ppoblación beneficiaria directa del proyecto.
        self.pobl_bni = 0 #Tamaño de la población beneficiaria indirecta del proyecto.
        self.obj_gen = '' # Objetivo general del proyecto.
        self.obj_esp = '' # Objetivos específicos del proyecto.

    def crear_inf_pry(self):
        pass

    def elim_inf_pry(self):
        pass

    def modif_inf_pry(self):
        pass

class tipos_prog_inv():
    #Clase que contiene los tipos de proyectos Investigación descriptiva y de catalogación.
    #Investigación correlacional, Investigación explicativa, Investigación comparativa

    def __init__(self):
        self.id_tipoproyecto = 0 # indentificador unico de tipo de proyecto
        self.desc_tipoproyecto = '' # descripcionj del tipo de proyecto

    def crear_tipos_pry(self):
        pass

    def elim_tipos_pry(self):
        pass

    def modif_tipos_pry(self):
        pass

class app_reg_prog_inv(app_mod):
    #Clase que contiene los objetos de la App Registro de Proyectos
    def __init__(self):
        self.id_app_reg_pry = 0 # identificador unico para  App Registro de Proyectos
        self.id_id_mod_pry   = 0 # Identificador único ddel modulo proyecto
        self.nomb_app_reg_pry  = '' # nombre de la App Registro de Proyectos
        self.desc_app_reg_pry  = '' # descripcion de la App Registro de Proyectos
        self.status_app_reg_pry  = False # estatus de la App Registro de Proyectos

    def crear_app_reg_pry(self):
        pass

    def elim_app_reg_pry(self):
        pass

    def modif_app_reg_pry(self):
        pass

    def info_mod(self):
        pass

    def __str__(self):
        pass


"""
Clases de la Aplicación Registro de Productos de Investigación
"""
class usu_inf_inv():
    # Clase que almacena y procesa la información de investigación del usuario
    def __init__(self):
        self.id_usu = 0 # identificador unico
        self.rol = 0 #Rol que se desempeña actualmente.
        self.ls_proc_inv = [] #listado de id procesos de investigación realizados
        self.ls_prod_inv = [] #Listado de id productos de investigación realizados
        self.ls_red_div = [] #Listado de redes de divulgación de investigación científica donde se está registrado(a).
        self.cvlac = "" #URL del CVlac del investigador(a).
        self.orcid = "" #ID de ORCID del investigador(a).
        self.ggl = "" #URL Google académico del investigador(a).

    def agregar_usu_inf_inv(self):
        pass

    def elim_usu_inf_inv(self):
        pass

    def modf_usu_inf_inv(self):
        pass

    def info_inv(self):
        pass

    def __str__(self):
        pass

class red_div():
    # Clase que almacena el objeto red de divulgación científica o repositorio
    def __init__(self):
        self.nombre_red = ""
        self.id_usu = 0
        self.usuario ="" #nick o dirección de usuario
        self.url = "" #Url de página principal dentro de la red o repositorio.
        self.uso = 0 #Uso de la red (frecuente:0; moderado:1; poco frecuente:2; inactivo:3)
        self.pub = False #Acceso público de información de red

    def agregar_red_div(self):
        pass

    def elim_red_div(self):
        pass

    def modf_red_div(self):
        pass

    def info_red_div(self):
        pass

    def __str__(self):
        pass

class proc_inv():
    #clase que almacena la información de procesos de investigación en los que ha participado un usuario del sistema.
    def __init__():
        self.id_proc =0 #Identificador único de proceso de investigación.
        self.id_usu = 0
        self.instit ="" # Nombre de la institucion o entidad donde participó en la investigación
        self.clas_inv = 0 #clasificación de la investigación según los tipos de clasificación de los diccionarios TIPO_INV_***
        self.fch_ini = 0
        self.fch_fin = 0
        self.certif = False
        self.nal ="" #país dónde se realizó la investigación
        self.ciudad = ""
        self.rol_inv = "" #Rol de investigación que se asumió en el proceso, ver diccionario ROL_INV
        self.id_grup_inv = 0 #Identificador del grupo de investigación
        self.num_intg = 0 #Número de integrantes del equipo de investigación.
        self.horas = "" #Número de horas semanales dedicadas al proyecto
        self. = 0 "" #Número de ciclos del curso "cuántas veces se dictó el curso"
        self.url_prog = "" #Url del documento o sitio web donde se puede localizar el programa del curso

    def agregar_proc_inv(self):
        pass

    def elim_proc_inv(self):
        pass

    def modf_proc_inv(self):
        pass

    def info_proc_inv(self):
        pass

    def __str__(self):
        pass

class prod_inv():
    #clase que almacena la información de procesos de investigación en los que ha participado.
    def __init__():
        self.id_prod = 0 #Identificador único de producto de investigación.
        self.id_usu = 0 #Identificador único del usuario que realizó el producto
        self.tipo = 0 # tipo de producto de investigación, ver Diccionario TIPO_PROD_INV
        self.pub= False #El producto se encuentra publicado
        self.fch_real = 0 #Fecha de realización.
        self.fch_pub = 0 #Fecha de publicación.
        self.reg = False #El producto se encuentra registrado en Plataforma de Colciencias.
        self.colab = False #El producto se realizó en colaboración de otros(as) Autores(as)
        self.res_inv = False #El producto es resultado de un proyecto de investigación.
        self.id_proc_inv = 0 #Identificador del proceso de investigación del que es derivado.
        self.horas = 0 #Número total de horas dedicadas al producto.
        self.url_prod = "" #Url del documento o sitio web donde se puede localizar el producto en su verisión digital.
        self.form = "" #Extensión del tipo de dpcumento digital (.pdf;.zip;.exe;.mp4;.docx;.txt;.xml;.json;.csv;.jgp;otro)
        self.rep_pub = True #El archvio digital se encuentra en repositorio público (True) o Privado (false), los repositorios privados son los que se encuentran en cuentas comerciales como drive,onedrive,mega,dropbox o similares. Los repositorios públicos son los que están destinados a la divulgación científica, o abierta, no requiere de autenticación en el sistema.

    def agregar_prod_inv(self):
        pass

    def elim_prod_inv(self):
        pass

    def modf_prod_inv(self):
        pass

    def info_prod_inv(self):
        pass

    def __str__(self):
        pass

class tipo_prod_inv():
    # Clase que almacena la información de los tipos producciones: ya sea proyecto, revistas, libros,
    #articulos, ponencias etc
    def __init__(self):
        self.id_prodccuin = 0 # identificador unico
        self.descricion = "" #  descricion
    def crear_tipo_prod(self):
        pass

    def elim_tipo_prod(self):
        pass

    def modi_tipo_prod(self):
        pass

    def info_tipo_prod(self):
        pass

    def __str__(self):
        pass


"""
Clases de la Aplicación Evaluación de Proyectos
"""

class app_ev_pry():
    #Clase que contiene los objetos de la App Evaluación de Proyectos
    def __init__(self):
        self.id_app_ev_pry = 0 # identificador unico para App Evaluación de Proyectos
        self.id_mod_pry  = 0 # Identificador único ddel modulo proyecto
        self.nomb_app_ev_pry  = '' # nombre de la App Evaluación de Proyectos
        self.desc_app_ev_pry = '' # descripcion de la App Evaluación de Proyectos
        self.status_app_ev_pry = False # estatus de la App Evaluación de Proyectos

    def crear_app_ev_pry(self):
        pass

    def elim_app_ev_pry(self):
        pass

    def modif_app_ev_pry(self):
        pass

class evalucion_pry():
    #Clase que contiene la forma de evaluacion del proyecto
    def __init__(self):
        self.id_evalucion = 0 # identificador unico para el tipo de evalucion
        self.desc_tipos_evalucion = '' # descripcion del tipo de evalucion
        self.id_grup_bd = 0 # identificador del grupo de investigación
        self.fech_ini = '' # fecha de inicio de la evaluacion
        self.fecha_fin = '' # fecha de fin de la evaluacion

        def crear_tipos_evalucion(self):
            pass

        def elim_tipos_evalucion(self):
            pass

        def modif_tipos_evalucion(self):
            pass

class rel_evalucion_pry():
    #Clase que contiene la forma de evaluacion individual
    def __init__(self):
        self.id_evalucion = 0 # identificador unico para el tipo de evalucion
        self.id_investigador = 0 # identificador del investigador
        self.id_ipos_evalucion =  '' # nombre del tipo de evaluacion

        def crear_rel_evalucion_pry(self):
            pass

        def elim_rel_evalucion_pry(self):
            pass

        def modif_rel_evalucion_pry(self):
            pass

class tipos_evalucion():
    #Clase que contiene la clase de evalucion, interna, externa y comite de etica
    def __init__(self):
        self.id_ipos_evalucion = 0 # identificador unico para el tipo de evalucion
        self.nomb_tipos_evalucion = '' # nombre del tipo de evaluacion
        self.desc_tipos_evalucion = '' # descripcion del tipo de evalucion

    def crear_tipos_evalucion(self):
        pass

    def elim_tipos_evalucion(self):
        pass

    def modif_tipos_evalucion(self):
        pass

class criterios():
    #Clase que contiene los tipos de criterios a evaluador
    #Relevancia de los objetivos, Experiencia del equipo de investigación,Viabilidad de la propuesta y de la coordinación
    #adecuación  del  presupuesto,Plan de difusión y transferencia de los resultados, Impacto  socioeconómico,Divulgación etc
    def __init__(self):
        self.id_criterios_pry = 0 # identificador unico para criterios del proyecto
        self.nomb_creterio = '' # nombre del criterio
        self.desc_criterio = '' # descripcion del criterio
        self.objetivo_lograr = '' # objetivo a lograr
        self.porcentage_calificacion = ''  # porcentage de nota del criterio

    def crear_criterios(self):
        pass

    def elim_criterios(self):
        pass

    def modif_criterios(self):
        pass

class criterios_pry():
    #Clase que contiene los criterios evaluados del proyecto
    def __init__(self):
        self.id_criterios_pry = 0 # identificador unico
        self.id_proyecto = 0 # identificador del proeycto
        selt.objetivo_logrado = False # si logro el objetivo

    def crear_app_ges_pry(self):
        pass

    def elim_app_ges_pry(self):
        pass

    def modif_app_ges_pry(self):
        pass



"""
Clases de la Aplicación Gestión de Proyectos
"""

class app_ges_pry():
    #Clase que contiene los objetos de la App Gestión de Proyectos
    def __init__(self):
        self.id_ges_pry = 0 # identificador unico para App Gestión de Proyectos
        self.id_mod_pry-- = 0 # Identificador único ddel modulo proyecto
        self.nomb_ges_pry  = '' # nombre de la App Gestión de Proyectos
        self.desc_ges_pry  '' # descripcion de la App Gestión de Proyectos
        self.status_ges_pry  = False # estatus de la App Gestión de Proyectos

    def crear_app_ges_pry(self):
        pass

    def elim_app_ges_pry(self):
        pass

    def modif_app_ges_pry(self):
        pass

class inf_ges_pry():
    #Clase que contiene lla informacion de la gestion del proyecto
    def __init__(self):
        self.inf_ges_pry = 0 # identificador unico para App Gestión de Proyectos
        self.Cpto_proy = '' # Conceptualización del Proyecto: Es realizar el marco teórico y coneptual de la o las ideas principaples del proyecto.',
        self.Form_proy = '' # Formulación o diseño del Proyecto: Es la expresión de las características y metodologías de un proyecto, expresando la temporalidad en el cual se realiza.',
        self.Eva_proy = '' # evaluación del Proyecto: Se valora el proyecto de acuerdo a los indicadores construidos y acordados para su medición .',
        self.Eje_proy = '' # Ejecución del Proyecto: Es realizar la gestión y accionesestablecidas en la formulación del proyecto.',
        self.Proy = '' # Es la compilación de de tres momentos de la ejecución de  una idea: Formulación, implementación y evaluación.',

    def crear_inf_ges_pry(self):
        pass

    def elim_inf_ges_pry(self):
        pass

    def modif_inf_ges_pry(self):
        pass

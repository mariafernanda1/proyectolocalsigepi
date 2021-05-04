from django.db import models

"""
Listas únicas, Conjuntos y Diccionarios del Módulo de Proyectos
"""

#tipos de Investigación
TIPO_INV_FIN=[
    #por fuente de financiación:
    ('0','Estatal'), #Recursos Estatales (Públicos)
    ('1','Privada'), #Recursos privados
    ('2','Personal'),#Recursos propios
    ('3','Comunitaria'), #Recursos comunitarios
    ('4','Mixta PUBPRV'), #Recursos Públicos y Privados
    ('5','Mixta PUBPER'), #Recursos Públicos y Personales
    ('6','Mixta PUBCOM'), #Recursos Públicos y Personales
    ('7','Otra') #Otra categoría de clasificación de financiación
    ]

TIPO_INV_INF=[
    #Por fuente de información:
    ('0','Sin Información'), #Sin información sobre las fuentes
    ('1','Primarias'), #Los datos son propios y se toman de forma directa
    ('2','Secundarias'), #Los datos ajenos y se trabaja con fuentes ajenas, no se recolectan datos de forma directa.
    ('3','Estado de la Cuestión'), #Es un tipo de investigación trasnversal qeu apunta a identificar las producciones documentales realizadas hasta la actualidad sobre un tema de investigación.
    ('4','Mixta'), #Los datos son propios en más del 50% de los casos y ajenos en el resto.
    ('5','Minería'), #Se substrae nueva información de cúmulos de datos existentes.
    ('6','Simulación'), #Se generan datos no experimentales para realizar pruebas simuladas de modelos.
    ('7','Otra') #Otra categoría de clasificación de fuente de información
    ]

TIPO_INV_MET=[
    #Por énfasis metodológico:
    ('0','Sin Información'), #Sin información sobre el énfasis metodológico
    ('1','Cualitativa'), #Se fundamenta en métodos cualitativos, estudios de caso, obervación de campo, etnografía, entre otros.
    ('2','Cuantitativa'), #Su énfasis es cuantitativo, estadístico o probabilístico.
    ('3','Mixta CC'), #Utiliza métodos cuantitativos y cualitativos de forma simultánea.
    ('4','Experimental'), #Sus resultados dependen de los experimentos que deben realizarse durante la investigación.
    ('5','Heurística'), #Se concentra en la ocnstrucción de apoyos a la investigación por medio de principios, reglas y estrategias para resolver problemas qeu aún no cunetan con solución.
    ('6','Exploratoria'), #Es la primera investigación que se realiza sobre el tema o desde ese enfoque metodológico.
    ('7','Clínica'), #Es una investigación derivada de una intervención a partir de un diagnóstico con un método ya probado.
    ('8','IAP'), #Los objetivos,la metodología y los resultados se consensúan con las poblaciones que se intervienen desde la investigación.
    ('9','Teórica'), #Su proceso de validación no requiere de evidencias empíricas, sino que ssus resultados se validan por sus premisas lógicas, que permiten explroar nuevas formas de comprensión de los fenómenos.
    ('10','Otra') #Otra categoría de clasificación metodológica.
    ]

TIPO_INV_TMP=[
    #Por énfasis temporal:
    ('0','Sin Información'),  #Sin información sobre el periodo de estudio.
    ('1','Histórica'), #Se busca acercarse a un objeto de estudio desde una continuidad temporal definida por el equipo de investigación.
    ('2','Genealógica'), #Parte de una exploración multicausal, que puede ser determinada ordenando cronológicamente los sucesos que explican y se relacionan para comprender una situación presente.
    ('3','Actual'), #Establece la situación actual de un fenómeno y el concoimiento que se tien hasta el momento en que se realiza.
    ('4','Proyectiva'), #Permite un abordaje temporal donde la investigación tiene previstos objetivos que se logran por medio del proceso de investigación, busca aproximar el resultado a un estado futuro deseado.
    ('5','Prescriptvia'),#Tiene como principal objetivo la optimizacion de procesos, partiendo de caminos metodológicos o procedimentales ya explorados en contextos determinados.
    ('6','Descriptiva'), #Se delimitan los aspectos o variables a estudiar, pero se privilegia la perspectiva subjetiva del investigador sobre la observación realizada, por lo general acompañan investigaciones preeliminares, exploratorias, etnográficas, artísticas o creativas.
    ('7','Prospectiva'), #Su principal preocupación es el modelado de los posibles desarrollos futuros de los fenómenos, tratando de brindar marcos de predictibilidad.
    ('8','Longitudinal'), #Es una investigación que se realiza de forma continua o de forma repetida durante un periodo largo de tiempo, con unas variables iniciales que se mantienen en el tiempo.
    ('9','Transversal'), #Delimita un tiempo determinado para realizar la investigación y puede trabajar multiplicidad de variables.
    ('10','Periódica'), #Es un tipo de investigación que se realiza con un intervalo de tiempo determinado y que tiene unos objtivos definidos por quienes la realizan o financian.
    ('11','Seccional'), #Se puede comprender como una variación de un estudio transversal que se reliza por una sola vez.
    ('12','Otra') #Otra categoría de clasificación temporal
    ]

TIPO_INV_VAR=[
    #Por los tipos de variables:
    ('0','Sin Información'),  #Sin información sobre las variables del estudio.
    ('1','Univariada'), #El objeto de estudio tiene una causalidad definida, determinable y se realiza el seguimiento de una variable central.
    ('2','Multivariada'), #El objeto de estudio no tiene una causalidad bien definida, y se relaciona con un conjunto finito de variables que pueden ser susceptibles de medirse.
    ('3','Correlacional'), #Se conocen als principales variables que intervienen en un fenómeno, pero se busca establecer el peso o la incidencia de las varibles en estudio.
    ('4','Estudio de Caso'), #Permite construir con base en el estudio de casos particulares, la construcción de tendencias o situaciones comunes que brindan correlación y generalización a partir de multiplicidad de estos estudios.
    ('5','Análisis Comparado'), #Desde unidades de análisis hermenéuticas, permite establecer correlaciones que facilitan la clasificación de objetos y fenómenos a partir del estudio de sus regularidades y correlaciones.
    ('6','Poblacional'), #Delimita un tiempo determinado para realizar la investigación y puede trabajar multiplicidad de variables.
    ('7','Muestral'), #Es un tipo de investigación que se realiza con un intervalo de tiempo determinado y que tiene unos objtivos definidos por quienes la realizan o financian.
    ('8','Otra') #Otra categoría de clasificación por variables.
    ]

TIPO_INV_CNT=[
    #Por contextos de investigación:
    ('0','Sin Información'),  #Sin información sobre las variables del estudio.
    ('1','Laboratorio'), #La investigación se realiza en un entorno controlado (Laboratorio).
    ('2','Campo'), #La investigación se debe desarrollar en un entorno no controlado (terreno o en el lugar donde tienen lugar los sucesos)
    ('3','Aplicada'), #Busca construir escenarios de investigación in situ, donde se puedan controlar los procesos que se están investigando.
    ('4','Operaciones o Procesos'), #Son técnicas de investigación para corrección, intervención u optimización de sistemas dinámicos, que permiten mejorar la funcionalidad y la eficiencia de diseños y estándares, se utilizan generalmente en etapas de desarrollo de productos o líneas de producción ya existentes, así como sistemas dinámicos complejos.
    ('5','Diagnóstica'), #La investigación diagnóstica se fundamenta en enfoques probabilíticos y estadísticos, donde la causalidad es múltiple con probabilidades de correlación similares, lo que influye en los tratamientos o las alternativas de solución.
    ('6','Metodológica'), #Son investigaciones que toman como foco de investigación la forma en que se realizan las investigaciones mismas, sus supuestos teóricos, los problemas de medición, o de interpretación de los datos, en general el cómo de las investigaciones.
    ('7','Forense'), #Es una investigación de corte histórico, busca establecer las situaciones más probables y demostrables, basados en evidencias para establecer responsabiliddes e imputaciones, a los posibles resposables de situaciones punibles o sancionables.
    ('8','Otra') #Otra categoría de clasificación de contextos
    ]

TIPO_INV_LOG=[
    #Por énfasis de marco axiológico
    ('0','Sin Información'),  #Sin información sobre el marco axiológico del estudio.
    ('1','Hermenéutica'), #Investigación que concentra sus esfuerzos en logar la mejor interpretación del sentido de los registros, en función de los contextos a los cuales se traduce e interpreta.
    ('2','Ontológica'), #Indaga sobre los problemas de percepción, subjetividad o distorsión de perspectiva por aprte de quienes realizan la investigacion, en el desarrollo del proceso investigativo.
    ('3','Epistemológica'), #Busca establecer el marco conceptual que sirve de paradigma a los planteamientos teóricos y explicativos que sustentan los sujetos investigadores.
    ('4','Holística'), #La investigación holística reconoce la necesidad de establecer el más amplio márgen de integración de las diferentes perspectivas epistemológicas y hermenéuticas en torno al objeto de estudio.
    ('5','Formal'), #Es aquella que se realiza de forma sistemática y ajustada a reglas qeu permiten su replicación, reproducción o desarrollo. También se utiliza en campos de ciencias puras con altos grados de abstracción, mediante métodos lógicos de validación.
    ('6','Informal'), #Es un tipo de investigación qeu debe improvisar de acuerdo a las circusntancias, contextos y posibilidades del investigador o equipo de investigación, para lograr un abordaje del objeto de estudio.
    ('7','Empírica'), #Se establece en contraposición a la especulación teórica, permitiendo presentar aquello que es sustentable exclusivamente a partir de los hechos registrables, contrastables y comprobables a partir de la experiencia o la experimentación.
    ('8','Analítica'), #El analisis es el método de investigación que busca la descomposición de las unidades ya reconocidas, como un todo que se descompone en partes que permitan comprender causalidades con un mayor nivel de precisión y certidumbre.
    ('9','Deductiva'), #La investigación deductiva parte de la premisa de la existencia de una regla general aplicable a la comprensión de un fenómeno, guiando el diseño de los instrumentos y las premisas de la investigación.
    ('10','Inductiva'), #El proceso de investigación inductiva, parte de una condición particular buscando construir a partir de evidencias las generalziaciones posibles hasta que la evidencia contradiga el marco de explicación que se induce a aprtir de esta.
    ('11','Mixta AD'), #Investigación que utiliza el marco Analítico-Deductivo en su planteamiento.
    ('12','Mixta ID'), #Investigación que utiliza el marco Inductivo-Deductivo en su planteamiento.
    ('13','Hipotética'), #Es una investigación qeu utiliza la construcción de hipótesis para su planteamiento explicativo, metodológico o teórico, la cual tiene por objetivo comprobar o refutar la(s) hipótesis planteada.
    ('14','Actuarial'), #Es un tipo de investigación que se concentra en los impactos posibles derivados de als actuaciones de diversos actores o fenomenos causales, tanto para explicar como predecir las situaciones presentes y futuras, a paertir del estudio de los datos pasados. Generalemente permite la construcción de modelos.
    ('15','Factorial'), #Este tipo de investigación se concentra en la determinación de factores que inciden en un determinado fenómeno, desde una perspectiva fundamentalmente estadística. Ha cobrado relevancia con metodologías de minería de datos y big data.
    ('16','Axiológica'), #Es la investigación qeu se concentra en el peso qeu tienen los actores del proceso investigativo en los resultados y sesgos propios de las investigaciones, derivados de la acción humana en el proceso investigativo.
    ('17','Taxonómica'), #La investigación Taxonómica tiene por objetivo lograr la mejor clasificación de lso objetos o fenómenos de estudio, permitiendo encontrar inconsistencias, coincidencias, correlaciones o alternativas en el proceso de clasificación de lso objetos de estudio o los fenomenos estudiados.
    ('18','Conceptual'), #La investigación conceptual fuera del marco de la cognición y la filosofía, hace referencia a explorar modelos de productos que si bien aún no existen podrían entrar a realizarse. Es el paso previo a la construcción de un prototipo.
    ('19','Crítica'), #La investigación crítica tiene por objetivo encontrar las fisuras e incosistencias de un planteamiento teórico o un modelo existente o propuesto. Cumple una función depuradora de los principios lógicos sobre los que operan las soluciones y los modelos científicos.
    ('20','Otra')  #Otra categoría de clasificación por marco axiológico.
    ]

TIPO_INV_CPR=[
    #Por énfasis de campo profesional
    ('0','Sin Información'), #Sin información sobre el campo profesional de la investigacion.
    ('1','Social'),#investigación propia de las ciencias sociales.
    ('2','Educativa'), #Investigación de las ciencias de la Educación.
    ('3','Didáctica'), #Investigación de las ciencias de la Educación.
    ('4','Periodística'), #Investigación propia de profesionales de periodismo.
    ('5','Artística'), #Investigación propia de profesionales de arte, diseño, música.
    ('6','Creativa'), #Es un enfoque de investigación que se concentra en carreras con énfasis creativo, artes plásticas, diseño, arquitectura, literatura, música, ingenierías, comunicación, entre otras.
    ('7','Jurídica'), #Propia de las disciplinas del Derecho, la Ciencia Política, las Ciencias de la Administración, las ciencias económicas, entre otras.
    ('8','Epidemiológica'), #Ciencias de la salud y de la administración.
    ('9','Etnográfica'), #Propia de la Antropología, sociología y ciencias sociales.
    ('10','Lingüística'), #Específica de la Lingüística, la filología, antropología, sociología, comunicación, entre otras.
    ('11','Semiótica'), #Tipo característico de ciencias sociales, artes y ciencias de la comunicación.
    ('12','Genética'), #Investigación propia de las ciencias de la salud, con énfasis en informática.
    ('13','Otra') #Otra categoría de clasificación por campo profesional.
    ]

#Roles en el proceso de investigación.
ROL_INV=[
    ('0','Sin Información'), #Sin información sobre el rol desempeñado
    ('1','Investigador(a) Principal'), #Responsable del proyecto y del equipo de investigación.
    ('2','Investigador(a) Senior'), #Categoría según Colciencias.
    ('3','Investigador(a) Asociado(a)'), #Categoría según Colciencias.
    ('4','Investigador(a) Junior'), #Categoría según Colciencias.
    ('5','Investigador(a) Emérito(a)'), #Categoría según Colciencias.
    ('6','Jóven Investigador(a)'), #Participación en convocatorias orientadas a jóvenes.
    ('7','Auxiliar de Investigación'), #Se participó ena ctividade relacionadas con la investigación.
    ('8','Investigador(a) independiente') #No se ha estado vinculado institucionalmente, pero se cuenta con productos de investigación.
    ]

USO_RED=[
    ('0','frecuente'),
    ('1','moderado'),
    ('2','poco frecuente'),
    ('3','inactivo')
    ]

TIPO_EXTEN=[
    ('0','.Zip'),
    ('1','.Gz'),
    ('2','.ded'),
    ('3','.exe'),
    ('4','otro')
    ]

USO_RED=[
    ('0', 'frecuente'),
    ('1', 'moderado'),
    ('2', 'poco frecuente'),
    ('3', 'inactivo')
    ]

# Create your models here.

# Clases de la Aplicación Registro de Productos de Investigación

"""
Clases de la Aplicación Registro de Productos de Investigación
"""
class usu_inf_inv(models.Model):
    # Clase que almacena y procesa la información de investigación del usuario
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)  # Identificador único de usuario # identificador unico
    rol = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  #Rol que se desempeña actualmente.
    ls_red_div = [] #Listado de redes de divulgación de investigación científica donde se está registrado(a).
    cvlac = "" #URL del CVlac del investigador(a).
    orcid = "" #ID de ORCID del investigador(a).
    ggl = "" #URL Google académico del investigador(a).


class rl_usu_inf_inv_proc_inv(models.Model): #listado de id procesos de investigación realizados
    id_proc = models.ForeignKey(proc_inv, on_delete=models.CASCADE, null=False, blank =False)
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)

class rl_prod_usu(models.Model): #Listado de id productos de investigación realizado
    prod_inv = models.ForeignKey(prod_inv, on_delete=models.CASCADE, null=False, blank =False)
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)


class red_div(models.Model):
    # Clase que almacena el objeto red de divulgación científica o repositorio

    nombre_red = models.CharField('NOmbre de la red ', max_length=60, null=False, blank= False)
    id_usu = models.ForeignKey(usu, on_delete=CASCADE, null=False, blank=False)
    usuario = models.CharField('Nick ', on_delete=CASCADE, null=False, blank=False ) #nick o dirección de usuario
    url = models.URLField('Url de página principal dentro de la red ', max_length=60, null=False, blank=False) #Url de página principal dentro de la red o repositorio.
    uso = models.CharField('Uso de la red ', max_length=1, choices=USO_RED, default=0, null=False, blank=False) #Uso de la red (frecuente:0; moderado:1; poco frecuente:2; inactivo:3)
    pub = models.BooleanField('Acceso público de información de red ', default=False) #Acceso público de información de red

    class Meta:
        verbose_name = 'red_div'
        verbose_name_plural = 'red_divs'

class proc_inv(models.Model):
    #clase que almacena la información de procesos de investigación en los que ha participado un usuario del sistema.
    id_proc = models.AutoField(primary_key = True)  #Identificador único de proceso de investigación.
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
    instit = models.CharField('Nombre de la institucion', max_length= 60, null=False, blank= False) # Nombre de la institucion o entidad donde participó en la investigación
    clas_inv = models.CharField(max_length=1, choices=TIPO_INV_FIN, blank=False, null=False) #clasificación de la investigación según los tipos de clasificación de los diccionarios TIPO_INV_***
    fch_ini = models.DateField('Fecha de inicio', auto_now =False)
    fch_fin = models.DateField('Fecha de fin', auto_now =False)
    certif = models.BooleanField('Posees certificado ', default=True)
    nal = models.CharField('Pais ', max_length=35, null=False, blank= False) #país dónde se realizó la investigación
    ciudad = models.CharField('Ciudad ', max_length=40, null=False, blank= False)
    rol_inv = models.CharField(max_length=1, choices=ROL_INV, null=False, blank=False) #Rol de investigación que se asumió en el proceso, ver diccionario ROL_INV
    id_grup_inv = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank=False) #Identificador del grupo de investigación
    num_intg = models.PositiveSmallIntegerField('#Número de integrantes del equipo de investigación.', default=5 ) #Número de integrantes del equipo de investigación.
    horas = models.PositiveSmallIntegerField('Número de horas semanales dedicadas al proyecto', default=5) #Número de horas semanales dedicadas al proyecto
    ciclos = models.PositiveSmallIntegerField('cuántas veces se dictó el curso', default= 5) #Número de ciclos del curso "cuántas veces se dictó el curso"
    url_prog = models.URLField('Sitio web donde se puede localizar el programa del curso ', max_length=80 null=False, blank=False) #Url del documento o sitio web donde se puede localizar el programa del curso

    class Meta:
        verbose_name = 'proc_inv'
        verbose_name_plural = 'proc_invs'

class prod_inv():
    #clase que almacena la información de procesos de investigación en los que ha participado.

    id_prod = models.AutoField(primary_key = True)#Identificador único de producto de investigación.
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) #Identificador único del usuario que realizó el producto
    tipo = 0 # tipo de producto de investigación, ver Diccionario TIPO_PROD_INV
    pub= models.BooleanField('El producto se encuentra publicado',default=False) #El producto se encuentra publicado
    fch_real = models.DateField('Fecha de realización ', auto_now= False) #Fecha de realización.
    fch_pub = models.DateField('fecha de publicación ', default=False) #Fecha de publicación.
    reg = models.BooleanField('El producto se encuentra registrado en Plataforma de Colciencias ', default= False) #El producto se encuentra registrado en Plataforma de Colciencias.
    colab = models.BooleanField('El producto se realizó en colaboración de otros(as), ', default= False) #El producto se realizó en colaboración de otros(as) Autores(as)
    res_inv = models.BooleanField('El producto es resultado de un proyecto de investigación ', default = False) #El producto es resultado de un proyecto de investigación.
    id_proc_inv = models.ForeignKey(proc_inv, on_delete= CASCADE, null=False, blank=False) #Identificador del proceso de investigación del que es derivado.
    horas = models.PositiveSmallIntegerField('Número total de horas dedicadas al producto ', default=8) #Número total de horas dedicadas al producto.
    url_prod = models.URLField('sitio web donde se puede localizar  ', max_length= 40, null= False, blank=False) #Url del documento o sitio web donde se puede localizar el producto en su verisión digital.
    form = models.CharField(max_length=1, choices=TIPO_EXTEN, null=False, blank=False, default = 0) #Extensión del tipo de dpcumento digital (.pdf;.zip;.exe;.mp4;.docx;.txt;.xml;.json;.csv;.jgp;otro)
    rep_pub = models.BooleanField('El archvio digita ', default= True) #El archvio digita

    class Meta:
        verbose_name = 'prod_inv'
        verbose_name_plural = 'prod_invs'















class usu_inf_inv(models.Model):
    # Clase que almacena y procesa la información de investigación del usuario
    id_usu =  models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) # identificador unico
    rol =  models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False) #Rol que se desempeña actualmente.
    ls_proc_inv = [] #listado de id procesos de investigación realizados
    ls_prod_inv = [] #Listado de id productos de investigación realizados
    ls_red_div = [] #Listado de redes de divulgación de investigación científica donde se está registrado(a).
    cvlac = models.URLField('URL del CVlac del investigador(a)..', null=False, blank=False)  #URL del CVlac del investigador(a).
    orcid = models.CharField('ID de ORCID del investigador(a).', max_length=100, null=False, blank = False)  #ID de ORCID del investigador(a).
    ggl =  models.URLField('URL Google académico del investigador(a)..', null=False, blank=False)  #URL Google académico del investigador(a).

class Meta:
    verbose_name = 'usu_inf_inv'
    verbose_name_plural = 'usu_inf_invs'



class red_div(models.Model):
    # Clase que almacena el objeto red de divulgación científica o repositorio
    nombre_red = models.CharField('Nombre de red.', max_length=100, null=False, blank = False)
    id_usu =  models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
    usuario =models.CharField('Nombre de usuario', max_length=100, null=False, blank = False) #nick o dirección de usuario
    url = models.URLField('Url de página principal dentro de la red o repositorio..', null=False, blank=False)  #Url de página principal dentro de la red o repositorio.
    uso = models.CharField(max_length=1, choices=USO_RED, default='0',null=False, blank = False) #Uso de la red (frecuente:0; moderado:1; poco frecuente:2; inactivo:3)
    pub = models.BooleanField('Acceso público de información de red', default=False) #Acceso público de información de red

class Meta:
    verbose_name = 'red_div'
    verbose_name_plural = 'red_divs'

class proc_inv(models.Model):
    #clase que almacena la información de procesos de investigación en los que ha participado un usuario del sistema.
    id_proc = models.AutoField(primary_key = True) #Identificador único de proceso de investigación.
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
    instit = models.CharField('Nombre de la institucion donde participó en la investigación', max_length=100, null=False, blank = False)  # Nombre de la institucion o entidad donde participó en la investigación
    clas_inv = models.CharField(max_length=1, choices= OJOOOOO, default='0',null=False, blank = False) #clasificación de la investigacion según los tipos de clasificación de los diccionarios TIPO_INV_***
    fch_ini =  models.DateField('fecha de Inicio', auto_now = False)
    fch_fin =  models.DateField('fecha de FIn', auto_now = False)
    certif = models.BooleanField('Certificado', default=False)
    nal =  models.CharField('Pais', max_length=100, null=False, blank = False)  #país dónde se realizó la investigación
    ciudad = models.CharField('Ciudad', max_length=100, null=False, blank = False)
    rol_inv =  models.CharField(max_length=1, choices=ROL_INV, default='0',null=False, blank = False) #Rol de investigación que se asumió en el proceso, ver diccionario ROL_INV
    id_grup_inv = models.ForeignKey(grup_inv, on_delete=models.CASCADE, null=False, blank =False) #Identificador del grupo de investigación
    num_intg = models.PositiveSmallIntegerField('Número de integrantes del equipo de investigación.') #Número de integrantes del equipo de investigación.
    horas =  models.CharField('Número de horas semanales dedicadas al proyecto', max_length=100, null=False, blank = False)  #Número de horas semanales dedicadas al proyecto
    num_cur = models.PositiveSmallIntegerField('cuántas veces se dictó el curso') #Número de ciclos del curso "cuántas veces se dictó el curso"
    url_prog = models.URLField('rl del documento o sitio web', null=False, blank=False) #Url del documento o sitio web donde se puede localizar el programa del curso

class Meta:
    verbose_name = 'proc_inv'
    verbose_name_plural = 'proc_invs'


class prod_inv(models.Model):
    #clase que almacena la información de procesos de investigación en los que ha participado.
    id_prod = models.AutoField(primary_key = True) #Identificador único de producto de investigación.
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) #Identificador único del usuario que realizó el producto
    tipo =  models.CharField(max_length=1, choices=TIPO_PROD_INV 'ojooo', default='0',null=False, blank = False)  # tipo de producto de investigación, ver Diccionario TIPO_PROD_INV
    pub= models.BooleanField('El producto se encuentra publicado', default=False) #El producto se encuentra publicado
    fch_real = models.DateField('Fecha de realización.', auto_now = False) #Fecha de realización.
    fch_pub = models.DateField('Fecha de publicación.', auto_now = False) #Fecha de publicación.
    reg = models.BooleanField('El producto se encuentra registrado en Plataforma de Colciencias.', default=False) #El producto se encuentra registrado en Plataforma de Colciencias.
    colab = models.BooleanField('El producto se realizó en colaboración de otros(as) Autores(as)', default=False) #El producto se realizó en colaboración de otros(as) Autores(as)
    res_inv = models.BooleanField('El producto es resultado de un proyecto de investigación.', default=False) #El producto es resultado de un proyecto de investigación.
    id_proc_inv = 0 #Identificador del proceso de investigación del que es derivado.
    horas = models.CharField('Número de horas semanales dedicadas', max_length=100, null=False, blank = False) #Número total de horas dedicadas al producto.
    url_prod = models.URLField('rl del documento o sitio web', null=False, blank=False) #Url del documento o sitio web donde se puede localizar el producto en su verisión digital.
    form = models.CharField(max_length=1, choices=TIPO_EXTEN, default='0',null=False, blank = False) #Extensión del tipo de dpcumento digital (.pdf;.zip;.exe;.mp4;.docx;.txt;.xml;.json;.csv;.jgp;otro)
    rep_pub = models.BooleanField('El archvio digital se encuentra en repositorio público (True) o Privado (false)', default=True) #El archvio digital se encuentra en repositorio público (True) o Privado (false), los repositorios privados son los que se encuentran en cuentas comerciales como drive,onedrive,mega,dropbox o similares. Los repositorios públicos son los que están destinados a la divulgación científica, o abierta, no requiere de autenticación en el sistema.

class Meta:
    verbose_name = 'prod_inv'
    verbose_name_plural = 'prod_invs'


class tipo_prod_inv(models.Model):
    # Clase que almacena la información de los tipos producciones: ya sea proyecto, revistas, libros,
    #articulos, ponencias etc

    id_prodccuin = models.AutoField(primary_key = True) # identificador unico
    descricion = models.CharField('descricion', max_length=100, null=False, blank = False)  #  descricion


class Meta:
    verbose_name = 'tipo_prod_inv'
    verbose_name_plural = 'tipo_prod_invs'

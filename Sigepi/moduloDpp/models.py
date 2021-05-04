from django.db import models
from administr.models import *

GRADO = [
        (0, 'Central'),
        (1, 'Descentralizada'),
        (2, 'Desconcentrada')
    ]

RAMA_POD = [
    (0, 'Ejecutivo'),
    (1, 'Legislativo'),
    (2, 'Judicial'),
    (3, 'Organismo de Control'),
    (4, 'Organización electoral')
    ]

TIPO_ENT = [
    (0, 'Adscrita'),
    (1, 'Vinculada'),
    (2, 'Cabeza de Sector')
    ]

NIVEL_SEC_PUB = [
    (0,'Central'),
    (1,'Descentralizado'),
    (2,'Desconcentrado')
    ]

NIVEL_TERR = [
    (0, 'Internacional'),
    (1, 'Nacional'),
    (2, 'Regional'),
    (3, 'Departamental'),
    (4, 'Municipal'),
    (5, 'Distrito Especial'),
    (6, 'Distrito Capital'),
    (7, 'Localidad'),
    (8, 'Vereda'),
    (9, 'Corregimiento'),
    (10, 'Intendencia de policia'),
    (11, 'Territorio Comunidad Indígena'),
    (12, 'Territorio Étnico'),
    (13, 'Extraterritorial')
    ]

IDENT_TIPO_OBJ = [
    (0, 'Entidad'),
    (1, 'Sector Jurídico Administrativo'),
    (2, 'Unidad Organizacional')
    ]

NIVEL_TERR_ADM = [
    (0,'Nacional'),
    (1, 'Regional'),
    (2, 'Depeartamental'),
    (3, 'Municipal - Distrital'),
    (4,'Local'),
    (5,'Autonomías Territoriales')
    ]

TIPO_DOC = [
    (0,'Documento convencional'),
    (1, 'Documento no convencional')
    ]

class mod_loz_act(models.Model):
#Actores: Son actores idividuales, coletivos u organizados tanto públicos como privados que influyen o participan de la política pública.
    idAct = models.AutoField(primary_key = True)
    Nom_Act = models.CharField('identifican como actores', max_length=60, null=False, blank = False) #Se identifican como actores a aquellos que pueden hacer presencia y/o\npertenecer a una instancia de debate, de producción de información sobre el\nproblema, o de estabilización de decisiones sobre el mismo. En tales circunstancias se tiende a identifican personas y/o grupos de interes a',
    Act_suest = models.CharField('Actores Supraestatales ', max_length= 50, null = False, blank = False) # Actores Supraestatales: ',
    Act_est = models.CharField('Actores Estatales ', max_length = 50, null = False, blank = False ) # Actores Estatales"El análisis de política pública gravita en buena medida en torno a la manera como concurren en el proceso una diversidad de actores: unos estatales, otros supraestatales; unos mediadores, otros son objeto de la intervención de estado; unos centrados en el diseño de directrices de política, otros ejecutores y evaluadores de procesos.\"',
    Rol = models.CharField('Los actores asumen roles ',  max_length = 2, null=False, blank = False ) # Rol:\"Los actores asumen roles, ponen a circular\nintermediarios (discursos, prácticas, imaginarios, objetos), para establecer quienes\nson y que interes los movilizan: sin embargo, en la interacción es igualmen',
#nota preguntar si roles lo saco de la tabla roles
    class Meta:
        verbose_name = 'mod_loz_act'
        verbose_name_plural = 'mod_loz_acts'

class mod_loz_algrtm_Inst(models.Model):
# Algoritmos Institucionales
    id_algrtm_Inst = models.AutoField(primary_key=True)
    Al_Instcol = models.IntegerField(null = False, blank = False)
#colocarle otro campo
    class Meta:
        verbose_name = 'mod_loz_algrtm_Inst'
        verbose_name_plural = 'mod_loz_algrtm_Insts'
#verificar para que sirve

class mod_loz_auto_adva(models.Model):
#Autonomía Administrativa: Identifica que grado e autonomía maneja dentro de la estructura del Estado, si es central, descentralizada y/o desconcentrada.';
    idAuto_Advo = models.AutoField(primary_key = True)
    Per_jur =  models.IntegerField(null = False, blank = False) #Personería Jurídica: tiene o no ', boolean
    Patr_Aut = models.IntegerField(null = False, blank = False) #Patrimonio Autónomo: Tiene o no', boolean
    #Per_jur =  TINYINT(1) NOT NULL COMMENT #Personería Jurídica: tiene o no ',
    #Patr_Aut = TINYINT(1) NOT NULL COMMENT #Patrimonio Autónomo: Tiene o no',
    Grad =  models.IntegerField(null = False, blank = False, choices = GRADO, default = 0, max_length=1) #Grado:  si es central, descentralizada y/o desconcentrada.',
#preguntar personeria juridica tiene o no
    class Meta:
        verbose_name = 'mod_loz_algrtm_Inst'
        verbose_name_plural = 'mod_loz_algrtm_Insts'

class mod_loz_norma(models.Model):
# Normas: Son todas las normas, leyes, decretos, actos administrativos, sentencias y demás que regulan la política asignando o modificando las funciones de las Entidades o Unidades Organizacionales.';
    id_norma = models.AutoField(primary_key = True)
    Sec =  models.CharField('Sector al cual pertenece la entidad ', max_length=60, null = False, blank = False) #Sector: Sector al cual pertenece la entidad a la cual',
    Ram_pod = models.IntegerField(null = False, blank = False, choices = RAMA_POD, default = 0)#Rama del Poder: Es la rama a la cual pertenece la ejecución de la norma.',
    Niv_Terial = models.IntegerField(null = False, blank = False, choices = NIVEL_TERR, default = 0) #Nivel Territorial: Es el nivel que contempla la norma para su aplicación y cumplimiento.',

    class Meta:
        verbose_name = 'mod_loz_norma'
        verbose_name_plural = 'mod_loz_normas'


class mod_loz_sect_juradm(models.Model):
# Entidad que referencia los sectores Jurídico Administrativos, conforme se van creando o modificando en la estructura administrativa del Estado Colombiano.';
    id_sector_juradm = models.AutoField(primary_key = True)  #Identificador del Sector Jurídico Administrativo.',
    nom_sector_juradmin = models.CharField('Nombre del sector Jurídico administrativo' , max_length=45, null = False, blank = False) #Nombre del sector Jurídico administrativo, tal y como aprece en la norma que lo crea o modifica',
    fecha_ini = models.DateField('Fecha de Inicio', auto_now = False)
    fecha_fin = models.DateField('Fecha de Fin', auto_now = False)


    class Meta:
        verbose_name = 'mod_loz_sect_juradm'
        verbose_name_plural = 'mod_loz_sect_juradms'


class mod_loz_ent_est(models.Model):
# Entidad Estatal: Es una unidad con personerìa jurìdica que pertenece a la estructura administrativa del Estado'
    id_ent =  models.AutoField(primary_key = True)
    nom_ent =  models.CharField('Nombre de la Entidad', null = False, blank= False, max_length = 70) #Nombre de la Entidad: Es el Nombre completo y oficial de la Entidad de acuerdo a la norma ue la crea y/o modifica.',
    sigla_ent = models.CharField('Sigla de la Entidad', null = False, blank= False, max_length = 40) #Sigla de la Entidad: Es la sigla completa y oficial de la Entidad de acuerdo a la norma ue la crea y/o modifica.',
    rama_pod = models.IntegerField(null = False, blank = False, choices = RAMA_POD, default = 0, max_length = 1) #Rama del Poder: Es la rama a la cual pertenece la ejecución de la norma.',
    tipo_ent = models.IntegerField(null = False, blank = False, choices = TIPO_ENT, default = 0, max_length = 1)  # Es el tipo de vinculación legal y reglamentaria que tiene la entidad con el Estado.',
    niv_sec_pub = models.IntegerField(null = False, blank = False, choices = NIVEL_SEC_PUB, default = 0, max_length = 1) #nivel del Sector Público: Es el  nivel o sector al cual pertenece la entidad este puede ser: Central; Descentralizado; Desconcentrado.',
    niv_trtrial = models.IntegerField(null = False, blank = False, choices = NIVEL_TERR, default = 0, max_length = 2) #Nivel Territorial: Es el nivel que contempla la norma para el campo funcional de la entidad.',
    fecha_ini =  models.DateField('Fecha de creación de la Entidad', auto_now = False)  #Fecha de creación de la Entidad.',

    class Meta:
        verbose_name = 'mod_loz_algrtm_Inst'
        verbose_name_plural = 'mod_loz_algrtm_Insts'

class rl_entidad_norma(models.Model):
    id_norma = models.ForeignKey(mod_loz_norma, on_delete=models.CASCADE, null=False, blank =False)
    id_entidad = models.ForeignKey(mod_loz_ent_est, on_delete=models.CASCADE, null=False, blank =False) #identificador de la Entidad que emite la norma que agrega, modifica o elimina funciones a una Entidad o Unidad Organizacional',

    class Meta:
        verbose_name = 'rl_entidad_norma'
        verbose_name_plural = 'rl_entidad_normas'

class mod_loz_func(models.Model):
# Entidad que identifica las funciones asignadas a una entidad o a una unidad organizacional a partir de una disposición normativa, de diferente tipo o nivel de jerarquía, dependiendo de la instancia que emite la norma.';
    id_func =  models.AutoField(primary_key = True)  #Identificador de función. Una función es tomada literalmente de la norma que la asigna a una Entidad o una Unidad Organizacional. ',
    id_obj =  models.ForeignKey(mod_loz_ent_est, on_delete=models.CASCADE, null=False, blank =False) #Identificador de la entidad Estatal, o la UNidad organizacional a la que se le asigna funciones.',
    id_norma = models.ForeignKey(mod_loz_norma, on_delete=models.CASCADE, null=False, blank =False)
    cont_func = models.CharField('Transcribir (Sin Modificaciones) el contenido de la función. ', max_length=500, null = False, blank = False) #Transcribir (Sin Modificaciones) el contenido de la función.',
    tipo_obj_rel = models.IntegerField(null = False, blank = False, choices = IDENT_TIPO_OBJ, default = 0, max_length = 1) #Identificador del tipo de objeto al que se le asignan o modifican funciones. Este identificador nos debe remitir a la tabla de la cual se obtiene el identificador del objeto a relacionar el conjunto de funciones.',

    class Meta:
        verbose_name = 'mod_loz_func'
        verbose_name_plural = 'mod_loz_funcs'


class mod_loz_uo(models.Model):
# Unidad Organizacional: Es la unidad que pertenece a la organización administrativa de la Entidad. Su nominación, objeto, funciones y modificaciónes son establecidos por norma legal.';
    id_uo =  models.AutoField(primary_key = True) #identificador de Unidad Organizacional',
    nom_uo =  models.CharField('Nombre de la Unidad Organizacional:' , max_length=125, null = False, blank = False) #Nombre de la Unidad Organizacional: Es el nombre oficial y completo de la unidad establecido por norma jurídica',
    sigla_uo =  models.CharField('Sigla de la Unidad Organizacional:' , max_length=25, null = False, blank = False)  #Sigla de la Unidad Organizacional: Es la sigla oficial y completo de la unidad establecido por norma jurídica',
    id_ent = models.ForeignKey(mod_loz_ent_est, on_delete=models.CASCADE, null=False, blank =False)  #Identificador de la entidad a la cual pertenece o se vincula la Unidad Organizacional.',
    id_sec_juradm = models.ForeignKey(mod_loz_sect_juradm, on_delete=models.CASCADE, null=False, blank =False)  #identificados del Sector Jurídico Administrativo.  apartir de este se accede al Nombre completo y oficial del sector Jurídico Administrativo',
    norma_crea = models.ForeignKey(mod_loz_norma, on_delete=models.CASCADE, null=False, blank =False)  #Norma: Norma que crea la Unidad Organizacional y le asigna funciones',

    class Meta:
        verbose_name = 'mod_loz_uo'
        verbose_name_plural = 'mod_loz_uos'

class Pro(models.Model):
    idPro = models.IntegerField(primary_key = True)
    desc_pro = models.CharField(max_length= 50, null = False, blank = False)
#    idPro = INT(11) NOT NULL,
#preguntar por esta tabla
    class Meta:
        verbose_name = 'mod_loz_algrtm_Inst'
        verbose_name_plural = 'mod_loz_algrtm_Insts'

class Proy(models.Model):
# Proyectos: Son todos los proyectos relacionados con la política pública
    idProy = models.AutoField(primary_key = True)
    Nom_Proy = models.CharField('Nombre completo y oficial del Proy :' , max_length=88, null = False, blank = False) #Nombre completo y oficial del Proy de acuerdo al acto administrativo o norma que lo crea',
    Tip_acc =  models.CharField('Tipo de acción :' , max_length=100, null = False, blank = False) #Tipo de acción: que se busca adelantar con la intervención planeada',
    Pobl = models.CharField('Poblacion:' , max_length=90, null = False, blank = False) #Poblacion: Cuál es la población que se pretende intervenir',
    Niv_trial = models.IntegerField(null = False, blank = False, choices = NIVEL_TERR, default = 0) #Nivel Territorial: es la unidad geográfica de división política del  territorio.',
    Nom_UO = models.CharField('Nombre de la Unidad Organizacional:' , max_length=60, null = False, blank = False) #Nombre de la Unidad Organizacional: Lozano, 2009, pág. 114)',
    Nom_Ent = models.CharField('Nombre de la Entidad:' , max_length=60, null = False, blank = False) #Nombre de la Entidad: Ent a la cual pertenece la UO encargada de ejecutar el proyecto (Lozano, 2009, pág. 114)',
    Per = models.CharField('Periodo de tiempo ' , max_length=60, null = False, blank = False) #Periodo de tiempo (rango mes-año). (Lozano, 2009, pág. 114)',
    MV = models.IntegerField(null = False, blank = False) #Monto del Proyecto. Valor Total (Lozano, 2009, pág. 114)',
    Obj_proy = models.CharField('Objetivos que orientan el proyecto.' , max_length=200, null = False, blank = False) #Objetivos que orientan el proyecto. En los casos que se presente señalar objetivos generales y específicos. (Lozano, 2009, pág. 115)',
#pregutar si tomo id de pry de la tabla proyectos
    class Meta:
        verbose_name = 'Proy'
        verbose_name_plural = 'Proys'

class Ref_doc(models.Model): # relacionada con saber
#Referenciación Documental: Es una entidad que permite identificar y referenciar tanto la información teórica y Normativa
    idRef_doc = models.AutoField(primary_key = True)
    Tip_Doc = models.IntegerField(null = False, blank = False, choices = TIPO_DOC, default = 0, max_length = 1) #Tipo documental: Identifique uno de estos dos tipos documentales. (Documento\nconvencional para aquellos que están publicados. Documento no convencional para\naquellos que no están publicados: manuscritos, fotocopias, dactilografías, etc.).\nCuando el documento es convencional y se trata de una publicación seriada\n(Anuarios, periódicos, diarios oficiales, revistas, almanaques, etc.) identifíquel',
    Cl_Doc = models.CharField('Clase documental' , max_length=45, null = False, blank = False) #Clase documental: Identifique si se trata de un documento independiente que\nconstituye una unidad en sí y no esta contenido en otros documentos, por ejemplo:\nlibro, capítulo de libro, ensayo, ponencia, informe, proyecto, diario de campo, artícu',
    Tt_Gral = models.CharField('Título general' , max_length=45, null = False, blank = False) #Título general: Coloque el título general del documento del cual toma la información.\n(Ej. El rey Lear). Si el documento trae subtitulo; escriba el título coloque dos puntos y\nescriba el subtítulo (Ej. Teoría crítica del sujeto: Ensayos de Psicoanálisis y materialismo\nhistórico).\nSi el documento hace parte de una publicación seriada, coloque aquí el t',
    Tt_esp = models.CharField('Título Específico:' , max_length=45, null = False, blank = False) #Título Específico: Cuando el documento estudiado hace parte de una publicación\nseriada o esta ubicado como parte de un libro (Capítulo, ponencia, artículo, excurso,\netc.), se coloca el título de documento en este campo y el título del libro que lo c',
    Au_Gral = models.CharField('Autor (es) generales:' , max_length=45, null = False, blank = False)#Autor (es) generales: Coloque el nombre del autor: Primer apellido y Segundo apellido,\nPrimer nombre y Segundo nombre. (Ej. Lamas Cardo, Ernesto Raúl.) Si hay más de dos\nautores separe cada uno de ellos con punto y coma. (Ej. Negri, Tomi; Hardt, Michael.).\nSi hay más de tres autores se toma el nombre del primero y se escribe después del\npunto seguido [et al]. (Ej. Lamas Cardo, Ernesto Raúl. [et al]. Si se trata ',
    Au_eps = models.CharField('Autor (es) específicos:' , max_length=45, null = False, blank = False)#Autor (es) específicos: Coloque el nombre del autor y/o autores que elaboraron el\ndocumento con los mismos criterios establecidos en el campo No.5. Si el documento\nestudiado no esta contenido en una publicación seriada, pero si es parte (capítulo,\nponencia, artículo, excurso, etc.) de un documento que lo contiene (libro), se coloca el\nautor del libro en el campo No.5 y el autor del capítulo, artículo o ponencia en éste\ncampo. Si se trata del mismo autor se coloca el mismo nombre en los dos camp',
    Pag_Vol = models.CharField('Páginas y o volúmenes' , max_length=45, null = False, blank = False) #Páginas y o volúmenes: Si se trata de un documento que esta contenido en una\npublicación seriada, o esta contenido en un libro se coloca la información de la siguiente\nmanera: Año de la publicación, número, volumen y rango de páginas (Ej. Año 3 Vol.5\nNo.17. [pp. 140-170]), (Ej. Año3 Vol.5. No17 Separata [pp.23-67]). Cuando no es\npublicación seriada se coloca Volumen, si es necesario y páginas (Ej. V.3, 3',

    class Meta:
        verbose_name = 'Ref_doc'
        verbose_name_plural = 'Ref_docs'

class rel_histo_v_obj(models.Model):
     #Tabla de relación histórica entre objetos. Establece el conjunto de relaciones historicas que se vinculan a cada Entidad o Unidad Organizacional (Objetos de relación) desde el análisis histórico. A partir de esta tabla se saca la herencia organizacional.';
    id_rel_histo_obj = models.AutoField(primary_key = True) #id de vínculo entre una relación histórica de un objeto con un objeto.',
    id_obj = models.ForeignKey(mod_loz_ent_est, on_delete=models.CASCADE, null=False, blank =False) #Identificador de la Entidad o de la Unidad Organizacional (objetos de relación).',
    #id_histo = INT NOT NULL COMMENT #Identificador de la historia que contiene una relación de precedencia-descendencia del objeto (Entidad o UO) seleccionada.',
    id_histo = models.CharField('Historico :' , max_length=45, null = False, blank = False)
    id_usuario = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) #Identificador del usuario autrizado para registrar la relación.',
 # PRIMARY KEY (`id_rel_histo_obj`, `id_usuario`))
 #preguntar esta tabla
#VERIFICAR LA TABLA
    class Meta:
        verbose_name = 'mod_loz_algrtm_Inst'
        verbose_name_plural = 'mod_loz_algrtm_Insts'

class rel_jrquia_v_obj(models.Model): #revisar
     #Tabla de relación entre objeto jerarquías. Establece el conjunto de relaciones jerárquicas que se vinculan a cada Entidad o Unidad Organizacional (Objetos de relación) desde el modelo de análisis de Alejandro Lozano. A partir de esta tabla se saca la estructura organizacional.';
    id_rel_jrquia_obj = models.AutoField(primary_key = True) #id de la relación jerarquía-objeto.',
    id_obj = models.ForeignKey(mod_loz_ent_est, on_delete=models.CASCADE, null=False, blank =False) #Identificador de la Entidad o de la Unidad Organizacional (objetos de relación).',
    #id_rel_jrquia = INT NOT NULL COMMENT #Identificador de la jerarquía que contiene una relación jerárquica del objeto (entida o UO) seleccionada.',
    id_rel_jrquia = models.CharField('Identificador de la jerarquía:' , max_length=60, null = False, blank = False)
    id_usuario = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) #Identificador del usuario que autoriza el registro de la relación.',
#ID USUARIO VERIFICAR SI LO TOMO DE USUARIO
    class Meta:
        verbose_name = 'rel_jrquia_v_obj'
        verbose_name_plural = 'rel_jrquia_v_objs'

class U_GP(models.Model):
    # 'Unidad Geopolítica: Estable la delimitación geográfica del territorio de acuerdo a las autonomías de poder territorial establecidas por el Estado';

    idUn_Geopol = models.AutoField(primary_key = True)
    Sec_jur_advo = models.CharField('Sector Jurìdico Admimnistrativo' , max_length=50, null = False, blank = False) #Sector Jurìdico Admimnistrativo:Es el Sector que normativamente se asigna a la entidad, es el ente jurídico quien asigna las disposiciones. ',
#    idEnt =  #Entidad: Es una unidad con personerìa jurìdica que pertenece a la estructura administrativa del Estado', #listado de entidades publicas, relaciona con la entidad que esta en la base de datos
    idEnt = models.CharField('entidad publica' , max_length=50, null = False, blank = False)
    Nv_Trial = models.IntegerField(null = False, blank = False, choices = NIVEL_TERR, default = 0) #Nivel Territorial: Es la división político administrativa del estado. List: Nacional; Regional; Depeartamental; Municipal - Distrital; Local; Autonomías Territoriales.',
#preguntar si ident es entidad estatal
# preguntar si unidad territorial es igual que nivel territorial
    class Meta:
        verbose_name = 'mod_loz_algrtm_Inst'
        verbose_name_plural = 'mod_loz_algrtm_Insts'


class Sec_Jur_Advo(models.Model): #'Sector Jurídico - Administrativo';

    idSec_Jur_Adv = models.AutoField(primary_key = True)
    Nom_Sec_Jur_Advo = models.CharField('Nombre del Sector Jurídico Administrativo:' , max_length=60, null = False, blank = False) #Nombre del Sector Jurídico Administrativo: Es el Nombre completo y oficial del sector Jurídico Administrativo',
    Sig_Sec_Jur_Advo = models.CharField('Sigla del Sector Jurídico Administrativo' , max_length=60, null = False, blank = False) #Sigla del Sector Jurídico Administrativo: Es la sigla completa y oficial del sector Jurídico Administrativo',
    idAct = models.ForeignKey(mod_loz_act, on_delete=models.CASCADE, null=False, blank =False) #Identificador de Actorees: Son los actores que tiene relación o vinculo con el sector',
    idEnt_Est = models.ForeignKey(mod_loz_ent_est, on_delete=models.CASCADE, null=False, blank =False)
    idU_GP = models.ForeignKey(U_GP, on_delete=models.CASCADE, null=False, blank =False)

    class Meta:
        verbose_name = 'Sec_Jur_Advo'
        verbose_name_plural = 'Sec_Jur_Advos'


class Un_Trial(models.Model):
#Unidad Territorial: Es un ente autnomo del estado con personería jurídica y recursos propios, y autonomía administrativa.';
    idUn_Trial = models.AutoField(primary_key = True)
    Un_Trialcol = models.IntegerField(null = False, blank = False)
    #agregue otro campo para descripcion
    desc_Trial = models.CharField('Descripcion ', null=False, blank = False, max_length = 100)

    class Meta:
        verbose_name = 'mod_loz_algrtm_Inst'
        verbose_name_plural = 'mod_loz_algrtm_Insts'

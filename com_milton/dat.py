#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado: 31-10-2020
Última Modificación: 1-11-2020
@author: Milton Castro
Versión:1.0
Programa para la Evaluación de proyectos de investigación.
Librería de estructuras de datos
Se detallan y desarrollan los Objetos de datos requeridos para la evaluación.
"""
import sqlite3

class app_bd():
    # Clase que almacena la información aplicaciones activas por usuario.
    # no se avanza en esta versión
    pass

class inv_bd():
    # Clase que almacena la información de los investigadores vinculados a los proyectos.
    # no se avanza en esta versión
    pass

class grup_bd():
    # Clase que almacena la información de los grupos de investigación vinculados a los proyectos.
    # no se avanza en esta versión
    pass

class instit_bd():
    # Clase que almacena la información de las instituciones que registran grupos de investigación vinculados a los proyectos.
    # no se avanza en esta versión
    pass

class lst_proy():
    # Clase que maneja el listado de proyectos
    pass

class inf_proy():
    # Clase que almacena la información del proyecto. (versión inicial contrato USTA)
    def __init__(self):
        self.id_pry = 0 # identificador único del proyecto.
        self.cod_pry = '' # Código de identificación del proyecto.
        self.nm_arch = '' # Nombre del archivo del proyecto.
        self.url_arch = '' # Url del archivo del proyecto.
        self.id_und_adm = 0 # Identificador de la Unidad Administrativa que se liga al proyecto.
        self.tit_pry = '' # Título del proyecto.
        self.id_inv_pr = 0  # Identificador del investigador(a) principal.
        self.id_gr = 0 # Identificador del grupo que presenta la propuesta.
        self.num_inv = 1 # Número de investigadores(as) involucrados en el proyecto.
        self.prom_frm = 0 # Nivel de formación promedio del grupo 0:Profesional; 1:esp.; 2:Maestría; 3. Doctorado.
        self.camp_usta = '' #Campo de acción dentro de la Uiversidad.
        self.foco = '' # Foco temático de la propuesta de investigación.
        self.enf = '' # Enfoque temático de la propuesta de investigación.
        self.conv = '' # Convenio propuesto o previsto para la realización de la investigación.
        self.dur = 0 # Duración del proyecto valores dentro de un rango.
        self.und_dur = 0 # unidad de medida del rango de tiempo, 0:seg; 1:min; 2:horas; 3:meses; 4:años.
        self.geo = '' # Aŕea geográfica que abarca el proyecto.
        self.resu = '' # Resumen del proyecto.
        self.url_ap = '' # Url de la imágen del árbol de problemas.
        self.url_ao = '' # Url de la imágen del árbol de objetivos.
        self.pobl_bnd = 0 #Tamaño de la ppoblación beneficiaria directa del proyecto.
        self.pobl_bni = 0 #Tamaño de la ppoblación beneficiaria indirecta del proyecto.
        self.obj_gen = '' # Objetivo general del proyecto.
        self.obj_esp = '' # Objetivos específicos del proyecto.
        self.reg_pry = [] # Lista de las variables del proyecto.
        self.ls_pry = [] # Lista de Registros de proyectos en la BD.

    def crear_pry(self):
        pass

    def elim_pry(self):
        pass

    def modif_pry(self):
        pass

    def leer_ls_pry():
        pass

    def sel_pry():
        pass

    def impr_pry():
        pass

    def import_pry_cvs():
        pass

    def import_pry_xls():
        pass

    def export_pry_cvs():
        pass

    def gbd_pry():
        # Guardar cambios del registro de proyecto en la Base de Datos
        pass


class prm_ev():
    # Clase que almacena y procesa la información de los parámetros de evaluación.

    def __init__(self):
        self.id_var = 0 # Identificador único de la Variable de evaluación.
        self.ord = 0 # órden de la variable (primer, segundo, tercer, ...)
        self.nom_v ='' # Nombre de la variable.
        self.desc_ ='' # Descripción de la variables.
        self.rng_ct = 0 # Id del rango de medición o valoración cuantitativo de la variable.
        self.rng_cl = 0 # Id del rango de medición o valoración cualitativo de la variable.
        self.icn = 0 # Identificador del ícono con el que se representa la variable
        self.sup = 0 # Identificador de la variable superior( si no es de primer orden)
        self.p_abs = 0 # Porcentaje del peso total de la variable
        self.p_rel = 0 # Porcentaje del peso relativo de la variable cuando se acumula, en un orden diferene al primer.
        self.p_pnd = 0 # Valor ponderado de la variable cunado no es de primer orden y no se acumula.
        self.p_tip = 0 # Tipo de peso calculado 0:NA; 1:abs; 2:rel; 3:pnd.
        self.reg = False # la variable es registrada sí:True; No:False.
        self.req = False # La variable es requerida Sí:True; No:False.
        self.ls_crit = [] # listado de criterios que permiten asignar valor.
        self.valor_ev = 0 # valor asignado a la variable por el evaluador
        self.valor_aut = 0 # valor asignado automaicamente según los criterios preestabelcidos.
        self.reg_prm = [] # fila o Registo del parámetro, Lista con el conjunto de variables de cada paŕametro de evaluación.
        self.ls_prm = [] # listado de variables registradas en al base de datos-

    def crear_prm(self):
        pass

    def elim_prm(self):
        pass

    def modif_prm(self):
        pass

    def leer_ls_prm():
        pass

    def sel_prm():
        pass

    def impr_prm():
        pass

    def gbd_prm():
        # Guardar cambios del registro en lla Base de Datos
        pass

class dic_exp():
    # Clase que procesa el diccionario de expresiones para la construcción
    # de oraciones que acompañan la evaluación.
    # tipo de expresión: conector, admiración, descripción, valoración, correlación,
    # referencia, sugenrencias otros.
    def __init__(self):
        self.id_exp = 0 #Identificador de la expresión registrada
        self.tipo_exp = 0 # identificador de los tipos de expresiones utilizadas.
        self.cont_exp = '' # Contenido propio de la expresión.
        self.tam_exp = 0 # Tamaño de la expresión 0:corta; 1:media; 2:larga; 3:extendida.
        self.ind_frec = 0 # indicador de frecuencia de utilización.
        self.id_alt = [] # Identificadores de expresiones alternativas por orden de pertinencia y frecuencia.
        self.reg_exp = [] # Registro completo de la expresión, con todas su variables.
        self.ls_exp = [] # Listado de expresiones en la base de datos.

    def crear_exp():
        pass

    def elim_exp(self):
        pass

    def modif_exp(self):
        pass

    def leer_ls_exp():
        pass

    def sel_exp():
        pass

    def impr_exp():
        pass

    def gbd_exp():
        # Guardar cambios del registro en lla Base de Datos
        pass

class rng_cc():
    #Clase para la equivalencia y correlación de rangos cualitatitivos
    #con rangos cuantitativos
    def __init__(self):
        self.id_rng = 0 #Identificador del rango registrada
        self.tipo_rng = 0 # identificador de los tipos de rangos utilizados.
        self.nom_rng = '' # Nombre del rango registado.
        self.tam_rng = 0 # Tamaño del rango, 0:indeterminado; otro valor diferente de cero cuando son elmeenos finitos.
        self.val_ini = 0 # Valor inicial del rango cuando es numérico.
        self.val_dx = 1 # Valor de la variacione entre valores del rago, 0: infinito o cualquier tamaño.
        self.val_fin = 1 # Valor final o máximo del rango cuando es numérico.
        sefl.val_cl = [] # Elementos del conjuntom ordenado de valores que puede asumir el rango.
        self.reg_rng = [] # Registro comleto de las variables del rango.
        self.ls_exp = [] # Listado de registos de rangos en la base de datos.

    def crear_rng():
        pass

    def elim_rng(self):
        pass

    def modif_rng(self):
        pass

    def leer_ls_rng():
        pass

    def sel_rng():
        pass

    def impr_rng():
        pass

    def transf_rng():
        #Transformar un rango a otro rango.
        pass

    def rord_rng():
        # Reordenar un rango discreto y cualitativo.
        pass

    def sum_elm_rng():
        # Suma o añade un elemeto al conjunto de un rango ordenado de corte cualitativo.
        pass

    def qt_elm_rng():
        # Quita o sustrae un elemeto del conjunto de un rango ordenado de corte cualitativo.
        pass

    def gbd_rng():
        # Guardar cambios del registro en lla Base de Datos
        pass


class db():
    # Clase para manejar, acceder y modificar los datos en la BD SQLite

    # Código SQL para la creación y lectura de la tabla de proyectos
    CREAR_TB_PRM_EV = """
        CREATE TABLE IF NOT EXISTS 'prm_ev' (
            'id_var'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            'ord'	INTEGER NOT NULL DEFAULT 0,
            'nom_v'	TEXT NOT NULL,
            'desc'	TEXT,
            'rng_ct'	INTEGER DEFAULT 0,
            'rng_cl'	INTEGER DEFAULT 0,
            'icn'	INTEGER DEFAULT 0,
            'sup'	INTEGER DEFAULT 0,
            'p_abs'	REAL DEFAULT 0,
            'p_rel'	REAL DEFAULT 0,
            'p_pnd'	REAL DEFAULT 0,
            'p_tip'	INTEGER DEFAULT 0,
            'reg'	INTEGER DEFAULT 0,
            'req'	INTEGER DEFAULT 0
        );
        """
    #insertar un nuevo registro en la tabla prm_ev
    INS_PRM_EV = """
        INSERT INTO
        """
    SEL_PRMS = "SELECT * FROM 'prm_ev'"

    CREAR_TB_PRY = """
        CREATE TABLE IF NOT EXISTS 'inf_pry' (
        'id_pry' INTEGER PRIMARY KEY AUTOINCREMENT,
        'cod_pry' TEXT,
        'nm_arch' TEXT,
        'url_arch' TEXT,
        'id_und_adm' INTEGER DEFAULT 0,
        'tit_pry' TEXT,
        'id_inv_pr' INTEGER DEFAULT 0,
        'id_gr' INTEGER DEFAULT 0,
        'num_inv' INTEGER DEFAULT 1,
        'prom_frm' INTEGER DEFAULT 0,
        'camp_usta' TEXT,
        'foco' TEXT,
        'enf' TEXT,
        'conv' TEXT DEFAULT 'Sin convenio',
        'dur' INTEGER,'und_dur' INTEGER DEFAULT 3,
        'geo' TEXT,
        'resu' TEXT,
        'url_ap' TEXT,
        'url_ao' TEXT,
        'pobl_bnd' INTEGER DEFAULT 0,
        'pobl_bni' INTEGER DEFAULT 0,
        'obj_gen' TEXT,
        'obj_esp' TEXT
        )
        """
    #insertar un nuevo registro en la tabla inf_pry
    INS_PRY = """
        INSERT INTO 'inf_pry'(
            'cod_pry',
            'nm_arch',
            'url_arch',
            'id_und_adm',
            'tit_pry',
            'id_inv_pr',
            'id_gr',
            'num_inv',
            'prom_frm',
            'camp_usta',
            'foco',
            'enf',
            'conv',
            'dur',
            'und_dur',
            'geo',
            'resu',
            'url_ap',
            'url_ao',
            'pobl_bnd',
            'pobl_bni',
            'obj_gen',
            'obj_esp'
            ) VALUES(
                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
            );
        """
    SEL_PYRS = "SELECT * FROM 'inf_pry'"

    def conectar_bd(dir_bd):
        # Conexión con la base de datos, si no existe la crea.
        # dir_db es la dirección con el nombre de la bd
        return sqlite3.connect(dir_bd)

    def crear_tabla(conector,tabla):
        # Crea una tabla a partir de secuencias ya definidas
        # conector es un parámetro de una variable de conección a la bd SQLite
        # tabla es una secuencia de comandos SQL para crear una determinada tabla.
        with conector:
            conector.execute(tabla)

    def ins_nv_pry(INS_PRY, conector,fl_inf_pry):
        #Insertar un nuevo registro en la tabla inf_pry
        # conector es un parámetro de una variable de conección a la bd SQLite
        #fl_inf_pry Lista que contiene las variables de información de proyecto
        fp = fl_inf_pry
        with conector:
            conector.execute(INS_PRY,(fp[1],fp[2],fp[3],fp[4],fp[5],fp[6],fp[7],
                                      fp[8],fp[9],fp[10],fp[11],fp[12],fp[13],
                                      fp[14],fp[15],fp[16],fp[17],fp[18],fp[19],
                                      fp[20],fp[21],fp[22],fp[23])
                             )

    def sel_regs(self, conector, tod_reg):
        # Obtiene la información de todos los registros de la tabla.
        # conector es un parámetro de una variable de conección a la bd SQLite
        # tod_reg es una secuencia de comandos SQL para seleccionar todos los registros de una tabla
        with conector:
            conector.execute(tod_reg).fetchall()

    def sel_reg(self, conector, reg):
        # Obtiene la información de todos los registros de la tabla.
        # conector es un parámetro de una variable de conección a la bd SQLite
        # reg es una secuencia de comandos SQL para seleccionar un registros de una tabla, según un criterio determinado
        with conector:
            conector.execute(tod_reg).fetchall()

    def ct_inf_pry(cursor):
        # Función que crea la Tabla inf_pry en la base de datos
        cursor.execute(
            """
            CREATE TABLE 'inf_pry' (
            	'id_pry'	INTEGER PRIMARY KEY AUTOINCREMENT,
            	'cod_pry'	TEXT,
            	'nm_arch'	TEXT,
            	'url_arch'	TEXT,
            	'id_und_adm'	INTEGER DEFAULT 0,
            	'tit_pry'	TEXT,
            	'id_inv_pr'	INTEGER DEFAULT 0,
            	'id_gr'	INTEGER DEFAULT 0,
            	'num_inv'	INTEGER DEFAULT 1,
            	'prom_frm'	INTEGER DEFAULT 0,
            	'camp_usta'	TEXT,
            	'foco'	TEXT,
            	'enf'	TEXT,
            	'conv'	TEXT DEFAULT 'Sin convenio',
            	'dur'	INTEGER,
            	'und_dur'	INTEGER DEFAULT 3,
            	'geo'	TEXT,
            	'resu'	TEXT,
            	'url_ap'	TEXT,
            	'url_ao'	TEXT,
            	'pobl_bnd'	INTEGER DEFAULT 0,
            	'pobl_bni'	INTEGER DEFAULT 0,
            	'obj_gen'	TEXT,
            	'obj_esp'	TEXT,
            	'Field25'	INTEGER
            );
            """
        )

    def ct_prm_ev(cursor):
        # Función que crea la Tabla prm_ev paŕametro de evaluación en la base de datos
        cursor.execute(
            """
            CREATE TABLE 'prm_ev' (
            	'id_var'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            	'ord'	INTEGER NOT NULL DEFAULT 0,
            	'nom_v'	TEXT NOT NULL,
            	'desc'	TEXT,
            	'rng_ct'	INTEGER DEFAULT 0,
            	'rng_cl'	INTEGER DEFAULT 0,
            	'icn'	INTEGER DEFAULT 0,
            	'sup'	INTEGER DEFAULT 0,
            	'p_abs'	REAL DEFAULT 0,
            	'p_rel'	REAL DEFAULT 0,
            	'p_pnd'	REAL DEFAULT 0,
            	'p_tip'	INTEGER DEFAULT 0,
            	'reg'	INTEGER DEFAULT 0,
            	'req'	INTEGER DEFAULT 0
            );
            """
        )

    def ct_dic_exp(cursor):
        # Función que crea la Tabla dic_exp diccionario de expresiones en la base de datos
        cursor.execute(
            """
            CREATE TABLE 'prm_ev' (
            	'id_var'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            	'ord'	INTEGER NOT NULL DEFAULT 0,
            	'nom_v'	TEXT NOT NULL,
            	'desc'	TEXT,
            	'rng_ct'	INTEGER DEFAULT 0,
            	'rng_cl'	INTEGER DEFAULT 0,
            	'icn'	INTEGER DEFAULT 0,
            	'sup'	INTEGER DEFAULT 0,
            	'p_abs'	REAL DEFAULT 0,
            	'p_rel'	REAL DEFAULT 0,
            	'p_pnd'	REAL DEFAULT 0,
            	'p_tip'	INTEGER DEFAULT 0,
            	'reg'	INTEGER DEFAULT 0,
            	'req'	INTEGER DEFAULT 0
            );
            """
        )

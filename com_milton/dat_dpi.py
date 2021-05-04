#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado: 06-05-2021
Última Modificación: 08-04-2021
Modificado por: Milton castro
Hora:5:00 am

Módulo DPI de Diagnóstico y Planeación Institucional
Contiene el modelo de datos para las aplicaciones:
    -DPI
        -Registro de Instrumentos de Planeación
        -Capacidades Institucionales
        -Mapas de Procesos
        -Gestión de Infraestructuras
        -Herramientas de Diagnóstico
"""

"""
Clases del Módulo DPI
"""
class mod_dpi():
    #Clase que contiene los objetos del módulo proyectos de SIGEPI
    pass


"""
Clases de la Aplicación Registro de Instrumentos de Planeación
"""
class app_reg_pry():
    #Clase que contiene los objetos de la App Registro de Proyectos

    pass

"""
Clases de la Aplicación Capacidades Institucionales
"""

class app_cap_dpi():
    #Clase que contiene los objetos de la App Capacidades Institucionales
    pass

"""
Clases de la Aplicación Mapas de Procesos
"""
class app_mp_dpi():
    #Clase que contiene los objetos de la App Mapas de Procesos
    pass




"""
Código en SQL que debe convertirse a clases



-- -----------------------------------------------------
-- Table `Pro_Inst`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Pro_Inst` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Pro_Inst` (
  `idPro_Inst` INT(11) NOT NULL,
  PRIMARY KEY (`idPro_Inst`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Procesos Institucionales';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Ref`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ref` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Ref` (
  `idRef` INT(11) NOT NULL,
  `idAct` VARCHAR(10) NOT NULL COMMENT 'Identificador de Actores que realizan la representaciòn de la polìtica pública.',
  `Nom_Ref` VARCHAR(100) NOT NULL COMMENT 'Nombre del Referencial',
  `Nom_PP` VARCHAR(100) NOT NULL COMMENT 'Nombre de  la Política pública.',
  PRIMARY KEY (`idRef`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Referenciales ';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Serv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Serv` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Serv` (
  `idServ` INT(11) NOT NULL,
  `Nom_ent` INT(11) NOT NULL COMMENT 'Nombre conpleto y oficial de la entidad que presta el servicio',
  `Tip_serv` VARCHAR(200) NOT NULL COMMENT 'Tipo de Servicio: Es el tipo dde servicio que presta la entidad a la  ciudadanía y/o a otras entidades tanto públicas como privadas.',
  `Nom_serv` INT(70) NOT NULL COMMENT 'Nombre del Servicio: Es el Nombre del serivicio  que presta la entidad',
  `Nv_Trial` VARCHAR(1) NOT NULL COMMENT 'Nivel Territorial: Es el nivel en que la entidad debe atender a las demandas.',
  PRIMARY KEY (`idServ`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Servicios: Son los servicios que tiene en la oferta institucional la Entidad';

SHOW WARNINGS;



"""

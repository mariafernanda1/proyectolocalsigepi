#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado: 06-05-2021
Última Modificación: 08-04-2021
Modificado por: Milton castro
Hora:5:00 am

Módulo Tableros de Control
Contiene el modelo de datos para las aplicaciones:
    -Teblero de control
        -variables
        -Indicadores
        -Representación de Datos
        -Análisis de Datos
        -Visualización Datos
        -Abstracción de datos
        -Publicación de datos
        -Fuentes de Datos
        -Alimentación
        -Herramientas de Registro
        -Herramientas de Almacenamiento
        -Herramientas de Consulta
"""

"""
Clases del Módulo Tableros de Control
"""
class mod_tc():
    #Clase que contiene los objetos del Módulo Tableros de Control TACON
    pass


"""
Clases de la Aplicación Variables
"""
class app_var_tc():
    #Clase que contiene los objetos de la App Variables

    pass

"""
Clases de la Aplicación Indicadores
"""

class app_ind_tc():
    #Clase que contiene los objetos de la App Indicadores
    pass



"""
Código en SQL que debe convertirse a clases


-- -----------------------------------------------------
-- Table `Mod_Tc_Herr`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_Herr` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_Herr` (
  `id_herr` INT NOT NULL COMMENT 'Herramienta de medición del indicador',
  `Nom_herr` VARCHAR(45) NOT NULL COMMENT 'Nombre de la herramienta',
  `Des_herr` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_herr`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_Indc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_Indc` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_Indc` (
  `id_ind` INT NOT NULL COMMENT 'Nombre del Indicador',
  `nom_ind` VARCHAR(45) NOT NULL COMMENT 'Identificador del  Indicador',
  `per_seg` DECIMAL(10,0) NOT NULL COMMENT 'Periodo de Seguimiento en días.',
  `fecha_ini` DATE NOT NULL COMMENT 'Fecha inicial de registro del dato del indicador',
  `fecha_ult` DATE NOT NULL COMMENT 'Fecha del último registro del indicador',
  `vigente` TINYINT(1) NOT NULL COMMENT 'Variable que define si el indicador se encuentra vigente o si  ha sido descartado o descontinuado para las labores de seguimiento.',
  `id_uo` INT NOT NULL COMMENT 'Unidad organizacional responsable de la producción  del indicador.',
  `tipo` VARCHAR(45) NOT NULL COMMENT 'Tipo de indicador',
  `doc_tec` VARCHAR(45) NOT NULL COMMENT 'Url del documento técnico que soporta el indicador.',
  `Mod_Tc_Herr_id_herr` INT NOT NULL,
  PRIMARY KEY (`id_ind`))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `id_uo` ON `Mod_Tc_Indc` (`id_uo` ASC);

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_Inst`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_Inst` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_Inst` (
  `id_Inst` INT NOT NULL,
  `id_norma` INT NULL,
  `id_ent` INT NOT NULL,
  `id_uo` INT NOT NULL,
  `nom_inst` VARCHAR(45) NOT NULL COMMENT 'nombre completo del instrumento',
  `sig_inst` VARCHAR(45) NOT NULL COMMENT 'Sigla del instrumento (si la tiene)',
  `doc_inst` VARCHAR(45) NOT NULL COMMENT 'Documento creado por la entidad que establezca, caracteririce, contenga los instrumentos.',
  `Mod_Tc_Var_id_var` INT NOT NULL,
  `Mod_Tc_ls_tip_Inst_id_ls_tip_Inst` INT NOT NULL,
  PRIMARY KEY (`id_Inst`))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `id_ent` ON `Mod_Tc_Inst` (`id_ent` ASC);

SHOW WARNINGS;
CREATE INDEX `id_ent` ON `Mod_Tc_Inst` (`id_ent` ASC);

SHOW WARNINGS;
CREATE INDEX `id_norma` ON `Mod_Tc_Inst` (`id_norma` ASC);

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_ls_Cnal`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_ls_Cnal` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_ls_Cnal` (
  `id_Mod_Tc_ls_Cnal` INT NOT NULL COMMENT 'Identificador para determina el nivel de confidencialidad de la información a ser ingresada',
  `Nom_Cnal` VARCHAR(45) NULL COMMENT 'Nombre de la confiencialidad',
  `Desc_cnal` VARCHAR(45) NULL COMMENT 'Breve descripción de la confidencial',
  PRIMARY KEY (`id_Mod_Tc_ls_Cnal`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_ls_Impt`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_ls_Impt` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_ls_Impt` (
  `id_ls_Impt` INT NOT NULL COMMENT 'Identificador de importancia del proceso',
  `nom_imp` VARCHAR(45) NOT NULL COMMENT 'Nombre de la clasificación de importancia',
  `descr` VARCHAR(45) NOT NULL COMMENT 'Descripción de la clasificación de importancia del proceso',
  PRIMARY KEY (`id_ls_Impt`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_ls_Riesg`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_ls_Riesg` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_ls_Riesg` (
  `id_ls_Riesg` INT NOT NULL COMMENT 'Identificador del riesgo',
  `nom_riesg` VARCHAR(45) NOT NULL COMMENT 'Nombre del riesgo',
  `descrip_riesg` VARCHAR(45) NOT NULL COMMENT 'Descripción del tipo de riesgo',
  `Mod_Tc_Procs_id_Procs` INT NOT NULL,
  `Mod_Tc_ls_Cnal_id_Mod_Tc_ls_Cnal` INT NOT NULL,
  PRIMARY KEY (`id_ls_Riesg`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_ls_tip_Inst`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_ls_tip_Inst` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_ls_tip_Inst` (
  `id_ls_tip_Inst` INT NOT NULL,
  `tip` VARCHAR(45) NOT NULL COMMENT 'Clasificación del tipo de instrumento.',
  PRIMARY KEY (`id_ls_tip_Inst`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_Norm`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_Norm` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_Norm` (
  `id_Norm` INT NOT NULL COMMENT 'Identificador de la norma que rige un determinado proceso o instrumento.',
  `nom_norm` VARCHAR(45) NOT NULL COMMENT 'Nombre de la norma.',
  `fecha_vig` DATETIME NOT NULL COMMENT 'Fecha en que entró en vigencia la norma.',
  `vigente` TINYINT(1) NOT NULL COMMENT 'Establece si la norma está vigente o no.',
  `id_ent` INT NOT NULL COMMENT 'Entidad que produce la norma',
  `url` VARCHAR(45) NOT NULL COMMENT 'Enlace o URL al documento de la norma',
  PRIMARY KEY (`id_Norm`))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `id_ent` ON `Mod_Tc_Norm` (`id_ent` ASC);

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_Procs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_Procs` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_Procs` (
  `id_Procs` INT NOT NULL COMMENT 'Identificador del proceso',
  `noma_proc` VARCHAR(45) NOT NULL COMMENT 'Nombre del Proceso. Identificador único del proceso',
  `id_norma` INT NOT NULL COMMENT 'Norma que justifica el establecimiento del proceso',
  `proc_padre` DECIMAL(10,0) NOT NULL COMMENT 'Proceso padre. Si el proceso es un sub proceso entonces tiene un proceso padre.',
  `vl_ini_rang_dura` DECIMAL(10,0) NOT NULL COMMENT 'Valor mínimo del rango de duración del proceso en mención.',
  `vl_fin_rang_dura` DECIMAL(10,0) NOT NULL COMMENT 'Valor máximo del rango de duración del proceso en mención.',
  `unid_rang` VARCHAR(45) NOT NULL COMMENT 'Unidad de tiempo en que se mide el rango que dura el proceso.',
  `respon_prin` VARCHAR(45) NOT NULL COMMENT 'Rol responsable principal del proceso.',
  `respon_sec` VARCHAR(45) NOT NULL COMMENT 'Rol responsable secundario del proceso.',
  `impotancia` VARCHAR(45) NOT NULL COMMENT 'Importancia del proceso o sub proceso0, dentro del proceso global',
  `Mod_Tc_Procscol` VARCHAR(45) NOT NULL,
  `Mod_Tc_Procscol1` VARCHAR(45) NOT NULL,
  `riesgo` VARCHAR(45) NOT NULL COMMENT 'Tipos de riesgos asociados al fallo o no realización del proceso.',
  PRIMARY KEY (`id_Procs`))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `id_norma` ON `Mod_Tc_Procs` (`id_norma` ASC);

SHOW WARNINGS;
CREATE INDEX `id_proc` ON `Mod_Tc_Procs` (`id_Procs` ASC);

SHOW WARNINGS;
CREATE INDEX `id_proc` ON `Mod_Tc_Procs` (`id_Procs` ASC);

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_Procs_has_Mod_Tc_Indc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_Procs_has_Mod_Tc_Indc` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_Procs_has_Mod_Tc_Indc` (
  `Mod_Tc_Procs_id_Procs` INT NOT NULL,
  `Mod_Tc_Indc_id_ind` INT NOT NULL,
  PRIMARY KEY (`Mod_Tc_Procs_id_Procs`, `Mod_Tc_Indc_id_ind`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_rel_proc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_rel_proc` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_rel_proc` (
  `id_rel_proc` INT NOT NULL COMMENT 'Identificador de relación entre procesos',
  `id_proc_ant` INT NOT NULL COMMENT 'Identificador del proceso anterior (si tiene)',
  `id_proc_act` INT NOT NULL COMMENT 'Identificador del proceso actual',
  `id_proc_sig` INT NOT NULL COMMENT 'Identificador del proceso siguiente (si tiene)',
  PRIMARY KEY (`id_rel_proc`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_Roles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_Roles` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_Roles` (
  `id_roles` INT NOT NULL COMMENT 'Identificador del rol',
  `nom_rol` VARCHAR(45) NOT NULL COMMENT 'Nombre del rol.',
  `equipo` VARCHAR(45) NOT NULL COMMENT 'Equipo de trabajo al que se articula el Rol',
  `vigente` TINYINT(1) NOT NULL COMMENT 'El rol se encuentra vigente o ya no hace parte de la estructura organizacional.',
  `id_uo` INT NOT NULL COMMENT 'Dependencia a la que se adscribe el rol determinado.',
  `fecha_creac` DATE NOT NULL COMMENT 'fecha de creación y entrada en funcionamiento del rol',
  `fecha_fin` DATE NOT NULL,
  `mod_loz_uo_id_uo` INT NOT NULL,
  PRIMARY KEY (`id_roles`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Mod_Tc_Var`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mod_Tc_Var` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Mod_Tc_Var` (
  `id_var` INT NOT NULL COMMENT 'Identificador de variable',
  `nom_var` VARCHAR(45) NOT NULL COMMENT 'Nombre de la variable',
  `tipo_var` VARCHAR(45) NOT NULL COMMENT 'Tipo de variable',
  `desc_var` VARCHAR(45) NOT NULL COMMENT 'Descripción de la variable',
  `frec_reg` DECIMAL(10,0) NOT NULL COMMENT 'Frecuencia de registro (Cada cuánta cantidad de tiempo debe registrarse).',
  `fecha_ini` DATE NOT NULL COMMENT 'Fecha inicial del registro de esta variable.',
  `fecha_fin` DATE NOT NULL COMMENT 'Fecha final en que se dejó de registrar.',
  `requerida` TINYINT(1) NOT NULL COMMENT 'Especifica si la variable es requerida para labores de seguimiento o de reporte, o si no es requerida.',
  `independiente` TINYINT(1) NOT NULL COMMENT 'Es una variable independiente o es dependiente de otra(s)',
  `id_Inst` INT NOT NULL COMMENT 'El instrumento en el cual se registra la variable.',
  PRIMARY KEY (`id_var`))
ENGINE = InnoDB;

SHOW WARNINGS;



"""

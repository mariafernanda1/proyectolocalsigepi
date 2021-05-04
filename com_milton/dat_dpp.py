"""
Código en SQL que debe convertirse a clases



-- -----------------------------------------------------
-- Table `mod_loz_act`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mod_loz_act` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mod_loz_act` (
  `idAct` INT(11) NOT NULL,
  `Nom_Act` VARCHAR(60) NOT NULL COMMENT '\"Se identifican como actores a aquellos que pueden hacer presencia y/o\npertenecer a una instancia de debate, de producción de información sobre el\nproblema, o de estabilización de decisiones sobre el mismo. En tales circunstancias se tiende a identifican personas y/o grupos de interes a',
  `Act_suest` VARCHAR(50) NOT NULL COMMENT 'Actores Supraestatales: ',
  `Act_est` VARCHAR(50) NOT NULL COMMENT 'Actores Estatales: \"El análisis de política pública gravita en buena medida en torno a la manera como concurren en el proceso una diversidad de actores: unos estatales, otros supraestatales; unos mediadores, otros son objeto de la intervención de estado; unos centrados en el diseño de directrices de política, otros ejecutores y evaluadores de procesos.\"',
  `Rol (lista)` VARCHAR(2) NOT NULL COMMENT 'Rol:\"Los actores asumen roles, ponen a circular\nintermediarios (discursos, prácticas, imaginarios, objetos), para establecer quienes\nson y que interes los movilizan: sin embargo, en la interacción es igualmen',
  PRIMARY KEY (`idAct`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Actores: Son actores idividuales, coletivos u organizados tanto públicos como privados que influyen o participan de la política pública.';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `mod_loz_algrtm_Inst`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mod_loz_algrtm_Inst` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mod_loz_algrtm_Inst` (
  `id_algrtm_Inst` INT(11) NOT NULL,
  `Al_Instcol` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id_algrtm_Inst`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Algoritmos Institucionales';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `mod_loz_auto_adva`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mod_loz_auto_adva` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mod_loz_auto_adva` (
  `idAuto_Advo` INT(11) NOT NULL,
  `Per_jur` TINYINT(1) NOT NULL COMMENT 'Personería Jurídica: tiene o no ',
  `Patr_Aut` TINYINT(1) NOT NULL COMMENT 'Patrimonio Autónomo: Tiene o no',
  `Grad (lista)` VARCHAR(2) NOT NULL COMMENT 'Grado:  si es central, descentralizada y/o desconcentrada.',
  PRIMARY KEY (`idAuto_Advo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Autonomía Administrativa: Identifica que grado e autonomía maneja dentro de la estructura del Estado, si es central, descentralizada y/o desconcentrada.';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `mod_loz_ent_est`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mod_loz_ent_est` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mod_loz_ent_est` (
  `id_ent` INT NOT NULL,
  `nom_ent` VARCHAR(70) NOT NULL COMMENT 'Nombre de la Entidad: Es el Nombre completo y oficial de la Entidad de acuerdo a la norma ue la crea y/o modifica.',
  `sigla_ent` VARCHAR(40) NOT NULL COMMENT 'Sigla de la Entidad: Es la sigla completa y oficial de la Entidad de acuerdo a la norma ue la crea y/o modifica.',
  `rama_pod` ENUM('Ejecutivo', 'Legislativo', 'Judicial', 'Organismo de Control', 'Organización electoral') NOT NULL COMMENT 'Rama del Poder: Es la rama a la cual pertenece la ejecución de la norma.',
  `tipo_ent` ENUM('Adscrita', 'Vinculada', 'Cabeza de Sector') NOT NULL COMMENT 'Tipo de Entidad: Es el tipo de vinculación legal y reglamentaria que tiene la entidad con el Estado.',
  `niv_sec_pub` ENUM('Central', 'Descentralizado', 'Desconcentrado') NOT NULL COMMENT 'nivel del Sector Público: Es el  nivel o sector al cual pertenece la entidad este puede ser: Central; Descentralizado; Desconcentrado.',
  `id_sec_juradm` INT NOT NULL COMMENT 'identificador del Sector Jurídico Administrativo: a partir de este se obtiene el Nombre completo y oficial del sector Jurídico Administrativo, al cual pertenece la Entidad.',
  `niv_trtrial` ENUM('Internacional', 'Nacional', 'Regional', 'Departamental', 'Municipal', 'Distrito Especial', 'Distrito Capital', 'Localidad', 'Vereda', 'Corregimiento', 'Intendencia de policia', 'Territorio Comunidad Indígena', 'Territorio Étnico', 'Extraterritorial') NOT NULL COMMENT 'Nivel Territorial: Es el nivel que contempla la norma para el campo funcional de la entidad.',
  `fecha_ini` DATE NULL COMMENT 'Fecha de creación de la Entidad.',
  PRIMARY KEY (`id_ent`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Entidad Estatal: Es una unidad con personerìa jurìdica que pertenece a la estructura administrativa del Estado';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `mod_loz_func`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mod_loz_func` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mod_loz_func` (
  `id_func` INT(11) NOT NULL COMMENT 'Identificador de función. Una función es tomada literalmente de la norma que la asigna a una Entidad o una Unidad Organizacional. ',
  `id_obj` INT NOT NULL COMMENT 'Identificador de la entidad Estatal, o la UNidad organizacional a la que se le asigna funciones.',
  `id_norma` INT NOT NULL,
  `cont_func` VARCHAR(500) NOT NULL COMMENT 'Transcribir (Sin Modificaciones) el contenido de la función.',
  `tipo_obj_rel` ENUM('Entidad', 'Sector Jurídico Administrativo', 'Unidad Organizacional') NULL COMMENT 'Identificador del tipo de objeto al que se le asignan o modifican funciones. Este identificador nos debe remitir a la tabla de la cual se obtiene el identificador del objeto a relacionar el conjunto de funciones.',
  PRIMARY KEY (`id_func`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Entidad que identifica las funciones asignadas a una entidad o a una unidad organizacional a partir de una disposición normativa, de diferente tipo o nivel de jerarquía, dependiendo de la instancia que emite la norma.';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `mod_loz_norma`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mod_loz_norma` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mod_loz_norma` (
  `id_norma` INT NOT NULL,
  `id_entidad` INT NOT NULL COMMENT 'identificador de la Entidad que emite la norma que agrega, modifica o elimina funciones a una Entidad o Unidad Organizacional',
  `Sec` VARCHAR(60) NOT NULL COMMENT 'Sector: Sector al cual pertenece la entidad a la cual',
  `Ram_pod (lista)` VARCHAR(1) NOT NULL COMMENT 'Rama del Poder: Es la rama a la cual pertenece la ejecución de la norma.',
  `Niv_Terial(lista)` VARCHAR(1) NOT NULL COMMENT 'Nivel Territorial: Es el nivel que contempla la norma para su aplicación y cumplimiento.',
  PRIMARY KEY (`id_norma`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Normas: Son todas las normas, leyes, decretos, actos administrativos, sentencias y demás que regulan la política asignando o modificando las funciones de las Entidades o Unidades Organizacionales.';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `mod_loz_sect_juradm`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mod_loz_sect_juradm` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mod_loz_sect_juradm` (
  `id_sector_juradm` INT NOT NULL COMMENT 'Identificador del Sector Jurídico Administrativo.',
  `nom_sector_juradmin` VARCHAR(45) NOT NULL COMMENT 'Nombre del sector Jurídico administrativo, tal y como aprece en la norma que lo crea o modifica',
  `fecha_ini` DATE NOT NULL,
  `fecha_fin` DATE NULL DEFAULT NULL,
  `id_norma` INT NULL,
  PRIMARY KEY (`id_sector_juradm`))
ENGINE = InnoDB
COMMENT = 'Entidad que referencia los sectores Jurídico Administrativos, conforme se van creando o modificando en la estructura administrativa del Estado Colombiano.';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `mod_loz_uo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mod_loz_uo` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mod_loz_uo` (
  `id_uo` INT NOT NULL COMMENT 'identificador de Unidad Organizacional',
  `nom_uo` VARCHAR(125) NOT NULL COMMENT 'Nombre de la Unidad Organizacional: Es el nombre oficial y completo de la unidad establecido por norma jurídica',
  `sigla_uo` VARCHAR(25) NOT NULL COMMENT 'Sigla de la Unidad Organizacional: Es la sigla oficial y completo de la unidad establecido por norma jurídica',
  `id_ent` INT NOT NULL COMMENT 'Identificador de la entidad a la cual pertenece o se vincula la Unidad Organizacional.',
  `id_sec_juradm` INT NOT NULL COMMENT 'identificados del Sector Jurídico Administrativo.  apartir de este se accede al Nombre completo y oficial del sector Jurídico Administrativo',
  `norma_crea` INT NOT NULL COMMENT 'Norma: Norma que crea la Unidad Organizacional y le asigna funciones',
  `norma_mdf` INT NULL DEFAULT NULL COMMENT 'Norma que Modifica la Unidad organizacional',
  PRIMARY KEY (`id_uo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Unidad Organizacional: Es la unidad que pertenece a la organización administrativa de la Entidad. Su nominación, objeto, funciones y modificaciónes son establecidos por norma legal.';

SHOW WARNINGS;



-- -----------------------------------------------------
-- Table `Pro`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Pro` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Pro` (
  `idPro` INT(11) NOT NULL,
  PRIMARY KEY (`idPro`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Programas';

SHOW WARNINGS;


-- -----------------------------------------------------
-- Table `Proy`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Proy` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Proy` (
  `idProy` INT(11) NOT NULL,
  `Nom_Proy` VARCHAR(80) NOT NULL COMMENT 'Nombre completo y oficial del Proy de acuerdo al acto administrativo o norma que lo crea',
  `Tip_acc` VARCHAR(100) NOT NULL COMMENT 'Tipo de acción: que se busca adelantar con la intervención planeada',
  `Pobl` VARCHAR(90) NOT NULL COMMENT 'Poblacion: Cuál es la población que se pretende intervenir',
  `Niv_trial (lista)` VARCHAR(1) NOT NULL COMMENT 'Nivel Territorial: es la unidad geográfica de división política del  territorio.',
  `Nom_UO` VARCHAR(60) NOT NULL COMMENT 'Nombre de la Unidad Organizacional: Lozano, 2009, pág. 114)',
  `Nom_Ent` VARCHAR(60) NOT NULL COMMENT 'Nombre de la Entidad: Ent a la cual pertenece la UO encargada de ejecutar el proyecto (Lozano, 2009, pág. 114)',
  `Per` VARCHAR(20) NOT NULL COMMENT 'Periodo de tiempo (rango mes-año). (Lozano, 2009, pág. 114)',
  `MV` INT(15) NOT NULL COMMENT 'Monto del Proyecto. Valor Total (Lozano, 2009, pág. 114)',
  `Obj_proy` VARCHAR(200) NOT NULL COMMENT 'Objetivos que orientan el proyecto. En los casos que se presente señalar objetivos generales y específicos. (Lozano, 2009, pág. 115)',
  PRIMARY KEY (`idProy`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Proyectos: Son todos los proyectos relacionados con la 	política pública';

SHOW WARNINGS;


-- -----------------------------------------------------
-- Table `Ref_doc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ref_doc` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Ref_doc` (
  `idRef_doc` INT(11) UNSIGNED NOT NULL,
  `Tip_Doc (lista)` VARCHAR(2) NOT NULL COMMENT '\"Tipo documental: Identifique uno de estos dos tipos documentales. (Documento\nconvencional para aquellos que están publicados. Documento no convencional para\naquellos que no están publicados: manuscritos, fotocopias, dactilografías, etc.).\nCuando el documento es convencional y se trata de una publicación seriada\n(Anuarios, periódicos, diarios oficiales, revistas, almanaques, etc.) identifíquel',
  `Cl_Doc` VARCHAR(45) NOT NULL COMMENT '\"Clase documental: Identifique si se trata de un documento independiente que\nconstituye una unidad en sí y no esta contenido en otros documentos, por ejemplo:\nlibro, capítulo de libro, ensayo, ponencia, informe, proyecto, diario de campo, artícu',
  `Tt_Gral` VARCHAR(45) NOT NULL COMMENT '\"Título general: Coloque el título general del documento del cual toma la información.\n(Ej. El rey Lear). Si el documento trae subtitulo; escriba el título coloque dos puntos y\nescriba el subtítulo (Ej. Teoría crítica del sujeto: Ensayos de Psicoanálisis y materialismo\nhistórico).\nSi el documento hace parte de una publicación seriada, coloque aquí el t',
  `Tt_esp` VARCHAR(45) NOT NULL COMMENT '\"Título Específico: Cuando el documento estudiado hace parte de una publicación\nseriada o esta ubicado como parte de un libro (Capítulo, ponencia, artículo, excurso,\netc.), se coloca el título de documento en este campo y el título del libro que lo c',
  `Au_Gral` VARCHAR(45) NOT NULL COMMENT '\"Autor (es) generales: Coloque el nombre del autor: Primer apellido y Segundo apellido,\nPrimer nombre y Segundo nombre. (Ej. Lamas Cardo, Ernesto Raúl.) Si hay más de dos\nautores separe cada uno de ellos con punto y coma. (Ej. Negri, Tomi; Hardt, Michael.).\nSi hay más de tres autores se toma el nombre del primero y se escribe después del\npunto seguido [et al]. (Ej. Lamas Cardo, Ernesto Raúl. [et al]. Si se trata ',
  `Au_eps` VARCHAR(45) NOT NULL COMMENT '\"Autor (es) específicos: Coloque el nombre del autor y/o autores que elaboraron el\ndocumento con los mismos criterios establecidos en el campo No.5. Si el documento\nestudiado no esta contenido en una publicación seriada, pero si es parte (capítulo,\nponencia, artículo, excurso, etc.) de un documento que lo contiene (libro), se coloca el\nautor del libro en el campo No.5 y el autor del capítulo, artículo o ponencia en éste\ncampo. Si se trata del mismo autor se coloca el mismo nombre en los dos camp',
  `Pag_Vol` VARCHAR(45) NOT NULL COMMENT '\"Páginas y o volúmenes: Si se trata de un documento que esta contenido en una\npublicación seriada, o esta contenido en un libro se coloca la información de la siguiente\nmanera: Año de la publicación, número, volumen y rango de páginas (Ej. Año 3 Vol.5\nNo.17. [pp. 140-170]), (Ej. Año3 Vol.5. No17 Separata [pp.23-67]). Cuando no es\npublicación seriada se coloca Volumen, si es necesario y páginas (Ej. V.3, 3',
  PRIMARY KEY (`idRef_doc`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Referenciación Documental: Es una entidad que permite identificar y referenciar tanto la información teórica y Normativa';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `rel_histo_v_obj`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rel_histo_v_obj` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `rel_histo_v_obj` (
  `id_rel_histo_obj` INT NOT NULL COMMENT 'id de vínculo entre una relación histórica de un objeto con un objeto.',
  `id_obj` INT NOT NULL COMMENT 'Identificador de la Entidad o de la Unidad Organizacional (objetos de relación).',
  `id_histo` INT NOT NULL COMMENT 'Identificador de la historia que contiene una relación de precedencia-descendencia del objeto (Entidad o UO) seleccionada.',
  `id_usuario` INT NOT NULL COMMENT 'Identificador del usuario autrizado para registrar la relación.',
  PRIMARY KEY (`id_rel_histo_obj`, `id_usuario`))
ENGINE = InnoDB
COMMENT = 'Tabla de relación histórica entre objetos. Establece el conjunto de relaciones historicas que se vinculan a cada Entidad o Unidad Organizacional (Objetos de relación) desde el análisis histórico. A partir de esta tabla se saca la herencia organizacional.';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `rel_jrquia_v_obj`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rel_jrquia_v_obj` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `rel_jrquia_v_obj` (
  `id_rel_jrquia_obj` INT NOT NULL COMMENT 'id de la relación jerarquía-objeto.',
  `id_obj` INT NOT NULL COMMENT 'Identificador de la Entidad o de la Unidad Organizacional (objetos de relación).',
  `id_rel_jrquia` INT NOT NULL COMMENT 'Identificador de la jerarquía que contiene una relación jerárquica del objeto (entida o UO) seleccionada.',
  `id_usuario` INT NULL COMMENT 'Identificador del usuario que autoriza el registro de la relación.',
  PRIMARY KEY (`id_rel_jrquia_obj`))
ENGINE = InnoDB
COMMENT = 'Tabla de relación entre objeto jerarquías. Establece el conjunto de relaciones jerárquicas que se vinculan a cada Entidad o Unidad Organizacional (Objetos de relación) desde el modelo de análisis de Alejandro Lozano. A partir de esta tabla se saca la estructura organizacional.';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Sec_Jur_Advo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sec_Jur_Advo` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Sec_Jur_Advo` (
  `idSec_Jur_Advo` INT(11) NOT NULL,
  `Nom_Sec_Jur_Advo` VARCHAR(60) NOT NULL COMMENT 'Nombre del Sector Jurídico Administrativo: Es el Nombre completo y oficial del sector Jurídico Administrativo',
  `Sig_Sec_Jur_Advo` VARCHAR(50) NOT NULL COMMENT 'Sigla del Sector Jurídico Administrativo: Es la sigla completa y oficial del sector Jurídico Administrativo',
  `idAct` VARCHAR(2) NOT NULL COMMENT 'Identificador de Actorees: Son los actores que tiene relación o vinculo con el sector',
  `idEnt_Est` VARCHAR(2) NOT NULL,
  `idU_GP` VARCHAR(45) NULL,
  PRIMARY KEY (`idSec_Jur_Advo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Sector Jurídico - Administrativo';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `U_GP`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `U_GP` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `U_GP` (
  `idUn_Geopol` INT(11) NOT NULL,
  `Sec_jur_advo` VARCHAR(50) NOT NULL COMMENT 'Sector Jurìdico Admimnistrativo:Es el Sector que normativamente se asigna a la entidad, es el ente jurídico quien asigna las disposiciones. ',
  `idEnt` VARCHAR(2) NOT NULL COMMENT 'Entidad: Es una unidad con personerìa jurìdica que pertenece a la estructura administrativa del Estado',
  `Nv_Trial (lista)` VARCHAR(2) NOT NULL COMMENT 'Nivel Territorial: Es la división político administrativa del estado. List: Nacional; Regional; Depeartamental; Municipal - Distrital; Local; Autonomías Territoriales.',
  PRIMARY KEY (`idUn_Geopol`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Unidad Geopolítica: Estable la delimitación geográfica del territorio de acuerdo a las autonomías de poder territorial establecidas por el Estado';

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Un_Trial`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Un_Trial` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Un_Trial` (
  `idUn_Trial` INT(11) NOT NULL,
  `Un_Trialcol` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idUn_Trial`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Unidad Territorial: Es un ente autnomo del estado con personería jurídica y recursos propios, y autonomía administrativa.';

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



"""

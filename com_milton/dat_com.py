
"""
Código en SQL que debe convertirse a clases

-- -----------------------------------------------------
-- Table `mod_com_msj`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mod_com_msj` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mod_com_msj` (
  `idMensaje` INT NOT NULL,
  `idUsuario` INT NOT NULL,
  `Mensaje` VARCHAR(256) NULL DEFAULT NULL,
  `Fechayhora` DATETIME NULL DEFAULT NULL,
  `generador` INT NULL DEFAULT NULL,
  `destinatario` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idMensaje`))
ENGINE = InnoDB;

SHOW WARNINGS;



"""

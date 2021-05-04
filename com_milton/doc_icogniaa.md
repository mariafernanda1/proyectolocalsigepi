<!--
Autor: Milton Castro
Creado: 17-03-2021
Actualizado:08-04-2021

Documentación técnica de la plataforma Icogniaa.
Del Aplicativo del Sistema de Gestión y Evalaución de Proyectos de Investigación SIGEPI.
Del Aplicativo Sistema de Aprendizaje Basado en Evidencias y Registros SABER.
Del Aplicativo Tablero de Control Seguimiento de Proyectos de Inversión TACON.

-->
Documentación técnica de la plataforma Icogniaa
===========

#Introducción
información del documento

    Creado jueves 2 de Abril 06:23:11 2020
    Sistema de Aprendiaje Badaso en Evidencias y Registros- SABER
    Módulo de Aplicación principal.
    @author: Milton O. Castro Ch.

# 1. Plataforma Icogniaa

## 1.1. Presentación Plataforma Icogniaa

## 1.2. Fundamentación

## 1.3. Base Tecnológica

## 1.4. Metodología

## 1.5. Módulos de desarrollo

### 1.5.1. App Kivy

### 1.5.2. App Django

## 1.6. Resultados

## 1.7. Pendientes


# 2. Aplicativo del Sistema de Gestión y Evalaución de Proyectos de Investigación SIGEPI

# 2. Plataforma Icogniaa

## 2.1. Presentación Plataforma Icogniaa

## 2.2. Fundamentación

## 2.3. Base Tecnológica

## 2.4. Metodología

## 2.5. Módulos de desarrollo

### 2.5.1. App Kivy

### 2.5.2. App Django

## 2.6. Resultados

## 2.7. Pendientes

# 3. Aplicativo Sistema de Aprendizaje Basado en Evidencias y Registros SABER

## 3.1. Presentación SaberApp

En este archivo aparecen las referencias y los diccionarios de datos, los tipos de metadatos con la información y el formato que se requiere para el modelo de escritura de la metodología SABER Sistema de Aprendizaje Basado en Evidencias y Registros, que vengo desarrollando hace algunos años (2016).

El sistema cuenta con unas unidades de registros que permiten articular el sistema en su conjunto, estas unidades son: Definiciones; Conceptos; Notas; Autores(as); Obras: Reseñas,Referencias y Citas; Teorías; Enfoques y Sistemas Teóricos.


## 3.2. Fundamentación: Unidades Básicas de SABER

### 3.2.1. Definiciones

Plantilla de definición simple. Una definición es un contenido corto que se sustrae de algún medio y se registra para su posterior utilización. Se caracteriza por no ser propia de quien está escribiendo o elaborando algún texto, contrario a los conceptos.

formato
Fechas: dd-mm-aaaa;
revision: número de modificaciones;
abc: letra para búsqueda;
cod: código único;
lect: número de veces que ha sido leido;
Etiquetas: Palabras que facilitan la búsqueda. Las etiquetas se separan con (;)

Plantilla de definición en md

    # def:0 revision:0 fecha_modif:01-01-2021 fechaCrea:01-01-2021 abc:a cod:0 lect:0
        encabezado:
        id_autor:
        id_obra:
        etiquetas:
    Contenido:
    >
    ***

    ***


### 3.2.2. Conceptos

Un Concepto es un contenido corto que es propio de quien escribe y se registra para su posterior utilización. Se caracteriza por ser una definición propia no debe ser de otro autor, contrario a las Definiciones.

formato
Fechas: dd-mm-aaaa;
revision: número de modificaciones;
abc: letra para búsqueda;
cod: código único;
lect: número de veces que ha sido leído;
las etiquetas se separan con (;)

Plantilla de Concepto simple en md.

    #concepto:0 revision:0 fecha_modif:01-01-2021 fechaCrea:01-01-2021 abc:a cod:0 lect:0
        encabezado:
        autor:
        id_autor:
        id_fuente:
        etiquetas:
    Contenido:
    >
    ***

    ***

### 3.2.3. Notas

Las notas son la base de la producción textual, son las unidades básicas de lo que se convertirá en un texto más elbaorado posteriormente, cuando de forma progresiva vayan adquiriendo formas más complejas, creciendo en tamaño y complejidad.

Plantilla de Nota Simple en md.

    # nota:0 revision:0 aaaa:2021 mes:01-01-2021 abc:a cod:0 lect:0 tipotx:nota
        titulo:
        autor:
        id_autor:
        id_obra:
        etiquetas:
        num_pal:
        meta:
        fecha_ini:
        fecha_fin:
        avance:0%[----------]100%
    ***
    Contenido:

    ***


### 3.2.4. Autores(as)

En SABER los autores son unidades hermenéuticas que permiten crear mapas referenciales del conocimiento, es importante identificar su teoría en el trasegar de su trayectoria.Las referencias de Autor(a), son uno de los componentes básicos del modelo de referencia y construcción discursiva centrales para la metodología SABER. La construcción de definiciones, teorías y obras se ligan a estas personas (sus autores y autoras), por lo cual son una referencia obligatoria en la trayectoria de evolución del conocimiento humano.

Plantilla de Autor(a) en md.

    # autor:0 revision:0 id_autor:0 abc:a cod:0 lect:0 tipotx:ref_autor
        nombres:
        apellidos:
        id_autor:
        fecha_nac:
        fecha_fall:
        pais:
        id_autor_ref:
        etiquetas:
    ***
    Trayectoria:
    ***
    Enlaces de Referencia:
    - [Obra 1](#id_obra1)
    - [Obra 2](#id_obra2)
    - [Obra 3](#id_obra3)
    - [Biografía](https://bigrafiaejemplo.com)
    - [Documental](https://videoejemplo.com)
    - [Infografía](https://infoejemplo.com)

    ***

### 3.2.5. Obras

En SABER las obras son unidades hermenéuticas que permiten crear mapas referenciales del conocimiento. Un(a) autor(a) aparece para el sistema social de conocimiento a partir de sus obras. Las referencias de obra, son uno de los componentes básicos del modelo de referencia y construcción discursiva centrales para la metodología SABER.

Plantilla de Obra en md.

    # obra:0 año:2021 revision:0 id_obra:0 abc:a cod:0 lect:0 id_autor:0 tipotx:ref_obra
        titulo:
        autor:
        id_autor:
        autores_sec:[id_autor],[id_autor]
        fecha_pub:
        editorial:
        ciudad:
        pais:
        isbn:
        id_bibtex:
        id_autor_reg:
        url:
        etiquetas:
    ***
    Descripción:
    ***
    Resumen:
    ***
    Enlaces de Referencia:
    - [Autor 1](#id_autor1)
    - [Autor 2](#id_autor2)
    - [Autor 3](#id_autor3)
    - [Versión original](https://versionejemplo.com)
    - [Reseña](https://reseñaejemplo.com)
    - [Video](https://videoejemplo.com)
    - [Infografía](https://infoejemplo.com)


    ***

### 3.2.6. Citas

La cita constituye un elemento básico para el ejercicio de análisis discursivo. Se busca capturar la idea del(la) autor(a) o su definición particular, en el desarrollo de su argumento.La cita es la transcripción fiel del texto, es decir sin ningún tipo de modificación al texto original del(la) autor(a). Se realizará la captura de información en un entrecomillado enunciando el número de página o páginas que contienen el texto referenciado.

Plantilla de cita en md.

    # cita:0 año:2021 revision:0 id_obra:0 abc:a cod:0 lect:0 tipotx:cita
        autor:
        id_autor:
        id_obra:
        pag_ini:
        pag_fin:
        id_bibtex
        fecha_reg:
        id_autor_reg:
        conc_central:
        etiquetas:
    ***
    Contenido:
    ***
    Enlaces de Referencia:
    - [Autor](#id_aut)
    - [obra](#id_obra)


    ***

### 3.2.7. Teorías

Las teorías agrupan un conjunto de ideas sobre un determinado fenómeno, su pretensión fundamental es explicar y presentar en ejercicios de relaciones lógicas de causalidad, que se traducen en capacidades predictivas en sucesiones de eventos determinables. Las teorías permiten el acercamiento epistémico de un fenómeno, la construcción de nuevo conocimiento se encuentra por lo general en la comprensión de diferentes formas de explicar la realidad y la búsqueda de nuevas formas de entender los fenómenos. Los(as) investigadores(as) constantemente buscan apoyarse en marcos teóricos, como sistemas de referencia válidos para ubicar sus ejercicios de investigación, especialmente si se pretende validar en una comunidad científica dada.

Plantilla de Teoría en md.

    # teoria:0 año:2021 revision:0 id_obra:0 abc:a cod:0 lect:0 tipotx:teoria
        nombre_teoria:
        id_teo:
        id_autor:
        id_obra:
        fecha_de_reg:
        id_autor_edit:
        id_autor_reg:
        conc_central:
        disciplina:
        etiquetas:
    ***
    Descripción:
    ***
    Historia:
    ***
    Estado del Arte:
    ***
    Hitos:
    ***
    Enlaces de Referencia:
    - [Autor(a) 1](#id_autor)
    - [Autor(a) 2](#id_autor)
    - [Autor(a) 3](#id_autor)
    - [Editor(a) Registro 1](#id_autor)
    - [Colaborador(a) Registro 2](#id_autor)
    - [Colaborador(a) Registro 3](#id_autor)
    - [Obra 1](#id_obra1)
    - [Obra 2](#id_obra2)
    - [Obra 3](#id_obra3)
    - [Biografía](https://bigrafiaejemplo.com)
    - [Documental](https://videoejemplo.com)
    - [Infografía](https://infoejemplo.com)


    ***

### 3.2.8. Sistemas Teóricos

Los sistemas teóricos son comprendidos desde la metodología SABER, como circuitos que se construyen desde las teorías como componentes individuales, que se van transformando a partir de la delimitación de sus tipos de interacción, en dispositivos integrados con mayor funcionalidad y operatividad. A manera de tablero de control de un vehículo, cada componente y medidor, permiten operar el conjunto de funcionalidades habilitadas para cada vehículo. En este sentido, su estandarización es más reducida, pues dependerá de las necesidades de cada equipo de investigación, quienes los crearán de acuerdo a sus necesidades. Por su grado de flexibilidad y complejidad deben presentarse como documentación necesaria para facilitar los marcos de comprensión de los proyectos de investigación.

Plantilla de Sistema Teórico en md.

    # sisteo:0 año:2021 revision:0 id_obra:0 abc:a cod:0 lect:0 tipotx:ref_sisteo
        nombre_sistema:
        id_autor:
        id_obra:
        fecha_de_reg:
        id_autor_edit:
        id_autor_reg:
        conc_central:
        disciplina:
        etiquetas:
        num_pal:
        meta:
        fecha_ini:
        fecha_fin:
        avance:0%[----------]100%
    ***
    Descripción:
    ***
    Historia:
    ***
    Estado del Arte:
    ***
    Hitos:
    ***
    Enlaces de Referencia:
    - [Autor(a) 1](#id_autor)
    - [Autor(a) 2](#id_autor)
    - [Autor(a) 3](#id_autor)
    - [Editor(a) Registro 1](#id_autor)
    - [Colaborador(a) Registro 2](#id_autor)
    - [Colaborador(a) Registro 3](#id_autor)
    - [Obra 1](#id_obra1)
    - [Obra 2](#id_obra2)
    - [Obra 3](#id_obra3)
    - [Biografía](https://bigrafiaejemplo.com)
    - [Documental](https://videoejemplo.com)
    - [Infografía](https://infoejemplo.com)

    ***

## 3.3. Base Tecnológica

## 3.4. Metodología

## 3.5. Módulos de desarrollo

### 3.5.1. App Kivy

### 3.5.2. App Django

## 3.6. Resultados

## 3.7. Pendientes


# 4. Aplicativo Tablero de Control Seguimiento de Proyectos de Inversión TACON

## 4.1. Presentación

## 4.2. Fundamentación

## 4.3. Base Tecnológica

## 4.4. Metodología

## 4.5. Módulos de desarrollo

### 4.5.1. App Kivy

### 4.5.2. App Django

## 4.6. Resultados

## 4.7. Pendientes

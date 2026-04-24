![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-complete-success)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey)
![Repo Size](https://img.shields.io/github/repo-size/SleekVoidAI/creador_estructura_quincenal)
![Last Commit](https://img.shields.io/github/last-commit/SleekVoidAI/creador_estructura_quincenal)

CREADOR DE ESTRUCTURA QUINCENAL - PYTHON

DESCRIPCIÓN:

Este proyecto implementa un script automatizado para la creación de estructuras de carpetas organizadas por año y quincena.

El sistema calcula automáticamente la quincena en curso (o utiliza una fecha proporcionada) y genera una carpeta principal con el formato definido, dentro de la cual se crean múltiples subcarpetas configurables.

Este tipo de automatización es útil para organizar procesos periódicos, flujos de trabajo administrativos y gestión estructurada de archivos.


FUNCIONALIDADES PRINCIPALES:

Cálculo automático de quincena (01 a 24)  
Generación de carpeta principal con formato configurable  
Creación automática de subcarpetas internas  
Soporte para configuración dinámica de subcarpetas  
Uso de fecha actual o personalizada  
Automatización de estructura de directorios  


TECNOLOGÍAS UTILIZADAS:

Python  
pathlib  
dataclasses  
datetime  
typing  


FLUJO DEL PROCESO:

Obtención de la fecha actual (o personalizada)  
Cálculo de la quincena correspondiente  
Construcción del nombre de la carpeta principal  
Creación de la carpeta en el directorio base  
Generación automática de subcarpetas internas  
Impresión de la ruta generada  


ESTRUCTURA GENERADA:

Ejemplo:

C:/Users/Usuario/Documents/  
Q_2026_08/  
Subcarpeta 1/  
Subcarpeta 2/  
Subcarpeta 3/  
Subcarpeta 4/  
Subcarpeta 5/  
Subcarpeta 6/  


CONFIGURACIÓN:

Las subcarpetas se definen mediante una lista:

SUBCARPETAS = [
    "Subcarpeta 1",
    "Subcarpeta 2",
    "Subcarpeta 3",
    "Subcarpeta 4",
    "Subcarpeta 5",
    "Subcarpeta 6"
]

La ruta base se configura en:

salida = Path("RUTA_DE_SALIDA")


EJECUCIÓN:

Ejecutar desde la terminal:

python creador_estructura_quincenal.py


DEPENDENCIAS:

No requiere librerías externas.


NOTAS:

El script crea carpetas solo si no existen (no sobrescribe)  
La estructura es totalmente configurable  
Se puede adaptar para otros esquemas de organización temporal  
Evitar usar rutas sensibles en repositorios públicos  


AUTOR:

Jorge Fernando Ortiz Bravo

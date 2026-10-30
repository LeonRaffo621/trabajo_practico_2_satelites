Trabajo integrador 2 parte 1 Satelites
Estudiante:Leon Muñoz Raffo 

Este sistema permite procesar registros de satélites en formato JSON, calcular sus 
posiciones geográficas en tiempo real, clasificar sus órbitas y corroborar si se encuentra 
dentro de determinada zona

Preparacion previa:

1) Crear el entorno virtual

2) Activar el entorno virtual:
.venv\Scripts\activate

3) pip install -r requirements.txt

Ejecucion:
El programa principal se ejecuta desde la terminal, se le entrega una ruta de un archivo JSON 
junto al tipo de consulta deseada.

Consulta de Resumen:
Agrupa los satélites por su tipo de órbita (LEO, MEO, GEO, HEO) y calcula estadísticas de altitud.

python main.py ruta/a/satelites.json resumen
(python consultar_satelites.py datos/satelites.json resumen)

Consulta de Zona:
Filtra los satélites que se encuentran dentro de un cuadrante geográfico delimitado por longitud mínima, 
latitud mínima, longitud máxima y latitud máxima.

python main.py ruta/a/satelites.json zona <lon_min> <lat_min> <lon_max> <lat_max>
(python consultar_satelites.py datos/satelites.json zona -75.0 -55.0 -50.0 -20.0)


Ejecución de Pruebas y Cobertura:
Para validar el correcto funcionamiento y comprobar el porcentaje de código examinado, 
ejecuta los siguientes comandos:

probar los tests convencionales:
  pytest

probar los tests con reporte de cobertura en la terminal:
  pytest --cov=.

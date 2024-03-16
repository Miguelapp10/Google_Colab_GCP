# Subir Hojas sheet a un dataset en GCP

Este script en Python realiza varias tareas relacionadas con la manipulación de datos e integración con los servicios de Google, principalmente Google Sheets y BigQuery. Vamos a describir qué hace cada parte del script:

Configuración de Autenticación de Google:

auth.authenticate_user(): Esta línea inicia el proceso de autenticación para que el usuario pueda acceder a los servicios de Google.
creds, _ = default(): Esta línea obtiene las credenciales para los servicios de Google.
Integración con Google Sheets:

El script utiliza la biblioteca gspread para conectarse a Google Sheets.
Accede a hojas de cálculo específicas (diciembre, enero24, febrero24, marzo24) de un documento de Google Sheets.
Para cada hoja de cálculo, obtiene todos los valores, los convierte en DataFrames de Pandas y los almacena en variables (diciembre, enero24, febrero24, marzo24).
Integración de Datos:

Concatena los DataFrames obtenidos de diferentes meses (diciembre, enero24, febrero24, marzo24) en un solo DataFrame (resultado_union) usando pd.concat().
Configuración de BigQuery y Carga de Datos:

Configura la autenticación para BigQuery usando la herramienta de línea de comandos gcloud.
Especifica el ID del proyecto (project_id) y los IDs del conjunto de datos y tabla (dataset_id, table_id) para BigQuery.
Carga el DataFrame concatenado (resultado_union) en una tabla de BigQuery usando la función to_gbq().
Acciones Adicionales:

Argumentos de la función to_gbq():
destination_table: Especifica la tabla de destino en BigQuery.
project_id: Especifica el ID del proyecto.
if_exists: Especifica la acción a tomar si la tabla ya existe (en este caso, reemplaza la tabla existente).
En resumen, este script está diseñado para obtener datos de Google Sheets de diferentes meses, concatenarlos en un DataFrame y luego cargar estos datos combinados en una tabla de BigQuery para su posterior análisis o procesamiento.

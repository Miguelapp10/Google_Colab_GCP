#!pip install google-colab google-cloud-bigquery
#!pip install gspread-pandas
#!pip install gspread

from google.colab import auth
from google.colab import files
from google.cloud import bigquery
import pandas as pd


auth.authenticate_user()

import gspread as gs
import gspread_dataframe as gd
from google.auth import default
creds, _ = default()

gc = gs.authorize(creds)
import os
# conectar el sheet
sheet = gc.open_by_key('ENLACE_ARCHIVO_SHEETS')
diciembre = sheet.worksheet('diciembre')
# Obtener todos los valores de la hoja de trabajo
diciembre = diciembre.get_all_values()
# Convierta los datos a un Pandas DataFrame
diciembre = pd.DataFrame(diciembre[1:], columns=diciembre[0])

enero24 = sheet.worksheet('enero24')
# Obtener todos los valores de la hoja de trabajo
enero24 = enero24.get_all_values()
# Convierta los datos a un Pandas DataFrame
enero24 = pd.DataFrame(enero24[1:], columns=enero24[0])

febrero24 = sheet.worksheet('febrero24')
# Obtener todos los valores de la hoja de trabajo
febrero24 = febrero24.get_all_values()
# Convierta los datos a un Pandas DataFrame
febrero24 = pd.DataFrame(febrero24[1:], columns=febrero24[0])

marzo24 = sheet.worksheet('marzo24')
# Obtener todos los valores de la hoja de trabajo
marzo24 = marzo24.get_all_values()
# Convierta los datos a un Pandas DataFrame
marzo24 = pd.DataFrame(marzo24[1:], columns=marzo24[0])

# Realiza la unión de los DataFrames
#enero, febrero, marzo,abril,mayo,junio,julio,agosto,setiembre,octubre,noviembre,
resultado_union = pd.concat([diciembre,enero24,febrero24,marzo24], ignore_index=True)

# Configuración de la autenticación para BigQuery
project_id = ''  # Reemplaza con tu ID de proyecto en Google Cloud
!gcloud config set project {project_id}
# Configuración del dataset y la tabla en BigQuery
dataset_id = '' # Nombre de dataset
table_id = '' # Nombre de la tabla

# Cargar el DataFrame en BigQuery
resultado_union.to_gbq(destination_table=f'{dataset_id}.{table_id}', project_id=project_id, if_exists='replace')
# Cargar el DataFrame en BigQuery
#resultado_union.to_gbq(destination_table=f'{project_id}.{dataset_id}.{table_id}', if_exists='replace')

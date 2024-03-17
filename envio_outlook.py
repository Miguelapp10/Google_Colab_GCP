#!pip install google-colab google-cloud-bigquery
!pip install xlsxwriter
#!pip install pyautogui
#!pip install smtplib
!pip install Openpyxl

from google.colab import auth
from google.colab import files

auth.authenticate_user()

import gspread as gs
import gspread_dataframe as gd
from google.auth import default
creds, _ = default()

gc = gs.authorize(creds)

from google.cloud import bigquery
import pandas as pd
import numpy as np
from datetime import datetime, timedelta,timezone

# Ingresa el ID de tu proyecto de Google Cloud
project_id = 'PROJECT_ID'

# Configura la conexión a BigQuery
client = bigquery.Client(project=project_id)

# Ejemplo de consulta
query = """
SELECT  *  FROM `UBICACION_TABLA` 
"""
# Ejecutar la consulta
result = client.query(query)

# Convertir los resultados en un DataFrame de Pandas
DATA = result.to_dataframe()

# Create a pivot table
pivot_table_1 = pd.pivot_table(DATA,
                             values=['ID'],
                             index=['ESTADO'],
                             columns=['Año_mes'],
                             aggfunc={'ID': 'count'},
                             margins=True,
                             margins_name='Total'
                             ).rename(columns={'ID': 'Cantidad'}
                                      ).rename_axis(columns={'ESTADO': 'ESTADO'})

# Rellenar los valores NaN con ''
pivot_table_1.fillna('', inplace=True)

# Create HTML representation of the styled pivot table
html_table_1 = pivot_table_1.to_html(classes='styled-table', escape=False)

# Print the head of the pivot table
print(pivot_table_1.head())
###############################################################################################################################################################################################
import time
import datetime
##import pyautogui
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import math  # Necesario para verificar NaN
import os

# Obtener la fecha actual y calcular la semana correspondiente
today = datetime.date.today()
week_number = today.strftime("%V")

# Definir el nombre del archivo Excel con el formato deseado
nombre_archivo = f"Pendientes_W{week_number}.xlsx"
# Escribir los DataFrames en un archivo Excel
with pd.ExcelWriter(nombre_archivo) as writer:
    # Escribir 'DATA' en una hoja llamada 'DATA'
    DATA.to_excel(writer, sheet_name='DATA', index=False)

# Obtener el libro de trabajo y las hojas
    workbook = writer.book
    DATA_sheet = writer.sheets['DATA']

    # Formato para los títulos de fondo de color naranja
    header_format = workbook.add_format({'bg_color': '#FFA500', 'bold': True})

    # Aplicar formato a los títulos en DATA
    for col_num, value in enumerate(DATA.columns.values):
        DATA_sheet.write(0, col_num, value, header_format)

    # Aplicar filtros en DATA
    DATA_sheet.autofilter(0, 0, len(DATA.index), len(DATA.columns) - 1)

    # Establecer el ancho de la columna en 30 en DATA
    DATA_sheet.set_column(0, len(DATA.columns) - 1, 30)

# Calcular el total de CANTIDAD en los DataFrames
TOTAL_CANTIDAD = DATA.shape[0]

# Calcular la suma de precios en los DataFrames
SUMA_PRECIO = DATA['Precio'].sum()

# Configuración
email_usuario = 'miguelapp101197@gmail.com'
contrasena = 'contraseña'
asunto_base = f"DETALLE {today.year} - WEEK {week_number} - {today}"

# Establecer la conexión con el servidor SMTP de Outlook
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()

# Iniciar sesión en el servidor SMTP
server.login(email_usuario, contrasena)

# Configurar el mensaje
msg = MIMEMultipart()
msg['From'] = email_usuario
msg['To'] = 'miguelapp101197@gmail.com'
msg['Subject'] = asunto_base
msg['CC'] = 'miguelapp101197@gmail.com'

# Darle un nivel de importancia al correo electrónico (en este caso, Alto)
msg.add_header('Importance', 'High')

# Crear el cuerpo del correo en formato HTML
mensaje_html = f"""
<html>
  <head>
    <style>
      .styled-table th {{
        background-color: orange;
        font-weight: bold;
      }}
    </style>
  </head>
  <body>
    <p>Estimado .....!</p>
    <p>CANTIDAD: {TOTAL_CANTIDAD} Y valorizado S/.{SUMA_PRECIO}.</p>
    <p><span style="font-size: 16px"><u><strong> Estado de ID </strong></u></span><br></p>
    {html_table_1}
  </body>
</html>
"""

# Adjuntar el cuerpo del correo en formato HTML
msg.attach(MIMEText(mensaje_html, 'html'))

# Adjuntar el archivo Excel al correo electrónico
filename = nombre_archivo
attachment = open(nombre_archivo, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

# Enviar el correo electrónico
server.sendmail(email_usuario,msg['To'], msg.as_string())

# Cerrar la conexión con el servidor SMTP
server.quit()

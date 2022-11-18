#Inserción de datos simulados en influxdb
from datetime import datetime
import random
from random import randint
import pandas as pd
from influxdb import InfluxDBClient

#Generar el cliente de influx
client = InfluxDBClient(host='localhost', port=8086)

#Seleccionar la base de datos en la que queremos escribir.
client.switch_database('simulacion')

#Coger el tiempo actual hasta minutos.
tiempo = datetime.now().strftime("%Y-%m-%d %H:%M")

#Generar una lista que simule los datos a insertar.
lista = [tiempo, randint(0, 100), round(random.uniform(0.00, 155.55), 2)]

#Generar el dataframe con toda la información.
df = pd.DataFrame([lista], columns=["Timestamp", "Entero", "Flotante"])

#Hacer un for que lea el dataframe y escriba todas las líneas en la base de datos.
for row in df.iterrows():
    fieldvalue=row[1]
    json_body=[
            {
                "measurement":"simulacion",
                "time": fieldvalue[0],
                "fields": {
                    "Entero": fieldvalue[1],
                    "Flotante": fieldvalue[2]
                }
            }
        ]
    client.write_points(json_body)

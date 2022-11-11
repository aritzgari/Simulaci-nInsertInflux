#Simulacion de datos creados por una maquina
from datetime import datetime
import random
from random import randint
import pandas as pd
from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('simulacion')

tiempo = datetime.now().strftime("%Y-%m-%d %H:%M")

lista = [tiempo, randint(0, 100), round(random.uniform(0.00, 155.55), 2)]

df = pd.DataFrame([lista], columns=["Timestamp", "Entero", "Flotante"])

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

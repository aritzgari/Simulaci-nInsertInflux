#Simulacion de datos creados por una maquina
import pandas as pd
from influxdb import InfluxDBClient

path = "/home/aritz/Scripts/simulacion.csv"

client=InfluxDBClient(host='localhost',port=8086)
client.switch_database('simulacion')

df=pd.read_csv(path, sep=';')
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
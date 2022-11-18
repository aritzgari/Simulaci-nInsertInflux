#Simulacion de datos creados por una maquina
import pandas as pd
from influxdb import InfluxDBClient

#Generar cliente influx.
client = InfluxDBClient(host='localhost', port=8086)

#Seleccionar la base de datos concreta con la información.
client.switch_database('simulacion')

#Hacer una query para seleccionar la información relevante.
result = client.query('SELECT * FROM "simulacion"')

#Coger solo la información.
points = list(result.get_points(measurement='simulacion'))

#Generar un dataframe con la información.
df=pd.DataFrame.from_dict(points)

print(df)
#Simulacion de datos creados por una maquina
import pandas as pd
from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)

client.switch_database('simulacion')

result = client.query('SELECT * FROM "simulacion"')

points = list(result.get_points(measurement='simulacion'))

df=pd.DataFrame.from_dict(points)

print(df)
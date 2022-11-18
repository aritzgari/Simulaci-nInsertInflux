#Subir datos obtenidos de plc a base de datos influxDB.
import pandas as pd
from influxdb import InfluxDBClient

#generar cliente influx.
client = InfluxDBClient(host='localhost', port=8086)

#Seleccionar la base de datos con la información.
client.switch_database('plc')

#Leer el csv con los datos.
datos = pd.read_csv(
    "/home/aritz/Scripts/DatosPLC.csv", sep=",", engine="python")

#Poner nombre a las columnas del dataframe.
datos.columns = ['Activar', 'Salida', 'Real', 'Entero', 'Time']

# Cambiar tipo de dato object a datetime.
datos['Time'] = pd.to_datetime(datos['Time'], unit="ms")

#Cambiar el tipo de dato para que no use los milisegundos.
datos['Time'] = datos['Time'].astype('datetime64[s]')

#Pasar los datos a un json para enviarlos luego a escribir en la base de datos.
for row in datos.iterrows():
    fieldvalue=row[1]
    json_body=[
            {
                "measurement":"plc",
                "time": fieldvalue[4],
                "fields": {
                    "EntradaNode": fieldvalue[0],
                    "Salida": fieldvalue[1],
                    "Real": fieldvalue[2],
                    "Entero": fieldvalue[3]
                }
            }
        ]
    client.write_points(json_body)

#Cerrar la conexión después de ejecutar.
client.close()

#Eliminar la información del csv para que no ocupe espacio.
df = pd.DataFrame()
df.to_csv('/home/aritz/Scripts/DatosPLC.csv')

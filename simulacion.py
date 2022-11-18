#Simulacion de datos creados por una maquina ahora en DESUSO
from random import randint
import random
import pandas as pd
from datetime import datetime
import os.path


#Declaración de la ubicación del archivo.
output_path = "/home/aritz/Scripts/simulacion.csv"

#Coge el tiempo actual al minuto
tiempo = datetime.now().strftime("%Y-%m-%d %H:%M")

#Generar una lista con variables aleatorios
lista = [tiempo, randint(0, 100), round(random.uniform(0.00, 155.55), 2)]

#Generar el dataframe con la lista anterior
df = pd.DataFrame([lista], columns=["Timestamp","Entero", "Flotante"])

#Comprobar si existe el archivo o no para continuarlo o crearlo.
if os.path.isfile(output_path):
	df.to_csv(output_path, mode='a', sep=';', index=False, header=False)
else:
	df.to_csv(output_path, mode='a', sep=';', index=False)
	

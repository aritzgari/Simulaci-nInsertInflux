#Simulacion de datos creados por una maquina ahora en DESUSO
from random import randint
import random
import pandas as pd
from datetime import datetime, timedelta
import os.path


#Coge el tiempo actual y le resta los microsegundos
output_path = "/home/aritz/Scripts/simulacion.csv"

tiempo = datetime.now().strftime("%Y-%m-%d %H:%M")

lista = [tiempo, randint(0, 100), round(random.uniform(0.00, 155.55), 2)]

df = pd.DataFrame([lista], columns=["Timestamp","Entero", "Flotante"])

if os.path.isfile('/home/aritz/Scripts/simulacion.csv'):
	df.to_csv('/home/aritz/Scripts/simulacion.csv', mode='a', sep=';', index=False, header=False)
else:
	df.to_csv('/home/aritz/Scripts/simulacion.csv', mode='a', sep=';', index=False)
	

import pandas as pd

# Importar datos del csv
data_teorico = pd.read_csv(r"C:\Users\DAVID\Desktop\UNIVERSIDAD\Data ingeniero.csv")

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico():
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]']
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]']
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion



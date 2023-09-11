from data.data import * # importamos todos los datos de data
from BD.baseDatos import * # importamos todos los datos de la base de Datos
from sklearn.linear_model import LinearRegression # importamos la librería para poder visualizar las regresiones lineales 
from grafica.grafica import * # importamos todos los datos de grafica
import pandas as pd # importamos la libreria pandas
# Todas las anteriores importaciones corresponden a los archivos que creamos anteriormente o librerías importadas 
#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico()# Se traen los datos de esfuerzo y deformación

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos() # Se obtienen los datos de la base de datos y se almacenan en la lista data_list
data_real = pd.DataFrame(data_list) # Creamos un DataFrame pandas a partir de los datos que ya tenemos
data_real_fit = data_real
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1) # se llaman los datos y se almacenan en X y Y
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1)
x_lim = data_real['Esfuerzo[kN]'].iloc[-1] # se obtienen los límites maximos para la gráfica
y_lim = data_real['Deformacion[mm]'].iloc[-1]
model = LinearRegression() # Se crea el modelo de regresión líneal
model.fit(X, y)
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1)#Se realiza una predicción usando el modelo de regresión lineal para una carga de 3000 kN y se almacena en la variable prediccion
print('la predicción a 1000 kN es de: ', prediction ,'mm') # mostramos el resultado de lo anterior


dataRealEsfuerzo = data_real['Esfuerzo[kN]']# Se almacenan los datos de Esfuerzo
dataRealDeformacion = data_real['Deformacion[mm]'] # Se almacenan los datos de Deformación

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) # Se genera una gráfica sin predicciones
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) # Se genera una gráfica con predicciones
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model) # Se genera una gráfica con una predicción específica a 3000 kN y se utiliza el modelo de regresión lineal para la predicción


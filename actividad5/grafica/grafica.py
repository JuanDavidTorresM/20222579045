import matplotlib.pyplot as plt
import numpy as np



def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
    
    
    plt.figure(figsize=(15, 6))
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red')
    plt.xlabel('Esfuerzo [kN]')
    plt.ylabel('Deformación [mm]')
    plt.title('Gráfica 2: teórico versus real [ZOOM]')
    plt.xlim(0, x_lim)
    plt.ylim(0, y_lim)
    plt.grid()
    plt.gca().invert_yaxis()
    plt.show()

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model):
  plt.figure(figsize=(15, 6))
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m')
  plt.scatter(	3000 , prediction, color='green')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN')
  plt.xlim(0, 3000)
  plt.ylim(0, 45)
  plt.grid()
  plt.gca().invert_yaxis()
  plt.show()

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
  plt.figure(figsize=(15, 6))
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 1: teórico versus real')
  plt.grid()
  plt.gca().invert_yaxis()
  plt.show()
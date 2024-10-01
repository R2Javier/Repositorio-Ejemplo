#Cambio para repositorio ejemplo

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, io
#<-------------
#aqui comentario
imagen = io.imread(r'F:\ARCHIVOS HDD\Materias\6to semestre\Procesamiento de imagenes\gatito_electrostatico.jfif')
#imagen = data.astronaut()
parte = imagen[0:50,0:50,:]
plt.figure(0)
plt.imshow(imagen)
plt.figure(1)
plt.imshow(parte)


hr = np.zeros(256) #histograma rojos
hv = np.zeros(256) #histograma verdes
ha = np.zeros(256) #histograma azules
filas = imagen.shape[0]
columnas=imagen.shape[1]
capas = imagen.shape[2]

for i in range(0,filas,1):  #Con los 2 puntitos marcas el fin de un ciclo
    for j in range(0,columnas,1):   #para decirle que el for esta dentro de otro, debo dar un tab, un "desplazamiento"
        posR=imagen[i,j,0]
        posV=imagen[i,j,1]
        posA=imagen[i,j,2]
        hr[posR]=hr[posR]+1
        hv[posV]=hv[posV]+1
        ha[posA]+=1        
plt.figure(2)
plt.plot(hr)
plt.figure(3)
plt.plot(hv)
plt.figure(4)
plt.plot(ha)
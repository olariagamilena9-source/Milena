from PIL import Image  
import matplotlib.pyplot as plt
import numpy as np

Imagen= Image.open("scooby_doo.jpg")
Imagen= Imagen.convert("L") 
m= np.array(Imagen)       
dimensiones= np.shape(m)  

plt.imshow(m, cmap="gray") 
plt.show()

filas, columnas= m.shape
aux= 1

for i in range(filas):
    for j in range(columnas// 2): 
        ind_op= columnas-1- j  
        aux= m[i][j]
        m[i][j]= m[i][ind_op]
        m[i][ind_op]= aux
            
plt.imshow(m, cmap="gray")
plt.show()
import matplotlib.pyplot as plt
import numpy as np
# plt.ion()

background = plt.imread('mos.png')  # Leemos la imagen que queremos usar de fondo, lo que escribáis entre comillas es la ruta a la imagen
x = np.arange(background.shape[1])  # Definimos valores de x
y = np.random.rand(background.shape[0]) * background.shape[0]  # Definimos valores de y
plt.plot(x, y)  # Dibujamos la serie
plt.imshow(background, alpha = 0.25)  # Creamos el fondo con una transparencia del 0.10 (1 es opaco y 0 es transparente)
plt.show()
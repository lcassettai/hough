import cv2 as opencv
import numpy as np

# Obtenemos la imagen del motor
imagen = opencv.imread('motor.png')

# Convertimos la imagen a escala de grises
imagen_gris = opencv.cvtColor(imagen,opencv.COLOR_BGR2GRAY)

# Aplicamos la detección de bordes por Canny 
bordes = opencv.Canny(imagen_gris,200,300,None, 3)

# Aplicamos la tranfromada de Hough para detección de rectas
lineas = opencv.HoughLines(bordes, 1, np.pi / 180, 150, 0, 0)

if lineas is not None:
    # Recorrer los resultados
    for i in range(0, len(lineas)):
        # Obtener los valores de rho (distacia)
        rho = lineas[i][0][0]
		# y de theta (ángulo)
        theta = lineas[i][0][1]
		# guardar el valor del cos(theta)
        a = np.cos(theta)
		# guardar el valor del sen(theta)
        b = np.sin(theta)
		# guardar el valor de r cos(theta)
        x0 = a*rho
		# guardar el valor de r sen(theta), todo se está haciendo de forma paramétrica
        y0 = b*rho
		# Ahora todo se recorrerá de -1000 a 1000 pixeles
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        
		# Superponemos las lineas encontradas en la imagen original
        opencv.line(imagen,(x1,y1),(x2,y2),(0,0,255),2)

# Mostramos la imagen original con todas las líneas encontradas
opencv.imshow('Transformada de Hough - Rectas', imagen)
opencv.waitKey(0)
opencv.destroyAllWindows()
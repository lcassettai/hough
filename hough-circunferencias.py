import cv2 as opencv
import numpy as np 
  
# Obtenemos la imagen del motor
imagen = opencv.imread('motor.png', opencv.IMREAD_COLOR) 

# Convertimos la imagen a escala de grises
imagen_gris = opencv.cvtColor(imagen, opencv.COLOR_BGR2GRAY) 

# Aplicamos la tranfromada de Hough para detección de círculos
circulos_detectados = opencv.HoughCircles(imagen_gris, opencv.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 70, maxRadius = 78) 
  
# Verificamos que la la funcion haya encontrado algun circulo
if circulos_detectados is not None: 
    # Convertir los parámetros el círculo a, b, y r en enteros de 16 bits
    circulos_detectados = np.uint16(np.around(circulos_detectados)) 
  
    # Recorremos todos los circulos detectados con el radio indicado
    for circulo in circulos_detectados[0, :]: 
        a, b, r = circulo[0], circulo[1], circulo[2] 
  
        # Dibujar la circunferencia
        opencv.circle(imagen, (a, b), r, (0, 0, 255), 2) 
        
        # Mostrar los datos de las circunferencias
        print("Centro ({:}, {:}), radio = {:}".format(a, b, r))
  
        # Dibujar un círculo pequeño alrededor del centro
        opencv.circle(imagen, (a, b), 1, (0, 255, 0), 3)
		# Ir mostradndo las circunferencias detectadas

opencv.imshow("Transformada de Hough - circunferencias", imagen) 
opencv.waitKey(0)         
opencv.destroyAllWindows()
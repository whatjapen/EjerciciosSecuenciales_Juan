#Ejercicio 12
#Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
#Hecho el 03/11/2026
#Por: Juan Agea Rodríguez
#Importo la libreria math
import math
x1, y1 = float(input("x1: ")), float(input("y1: "))
x2, y2 = float(input("x2: ")), float(input("y2: "))
print("Distancia:", math.hypot(x2 - x1, y2 - y1))  # Pitágoras
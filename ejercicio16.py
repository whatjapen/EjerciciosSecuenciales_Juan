#Ejercicio 16
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en qué tiempo (minutos) alcanzará el vehículo más rápido al otro.
#Hecho el 03/11/2026
#Por: Juan Agea Rodríguez
d = float(input("Distancia (km): "))
v1 = float(input("Velocidad del de atrás (km/h): "))
v2 = float(input("Velocidad del de adelante (km/h): "))
print("Minutos:", d / (v1 - v2) * 60)

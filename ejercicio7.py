#Ejercicio 6
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
#Hecho el 27/10/2026
#Por: Juan Agea Rodríguez
mins=int(input("Minutos: "))
horas=mins//60
resto=mins%60
print(mins,"minutos son",horas,"horas y",resto,"minutos")
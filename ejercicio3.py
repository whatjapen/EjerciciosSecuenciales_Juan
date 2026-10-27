#Ejercicio 3
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
#Hecho el 27/10/2026
#Por: Juan Agea Rodríguez
#Hipotenusa con catetos
#Pedir catetos
a = float(input("Cateto a: "))
b = float(input("Cateto b: "))
#Teorema de pitagoras
c=pow((a**2+b**2),1/2)
print (c)
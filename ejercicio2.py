#Ejercicio 2
#Calcular el perímetro y área de un rectángulo dada su base y su altura.
#Hecho el 27/10/2026
#Por: Juan Agea Rodríguez
# Area rectagulo
    # Pregunta por base
base=int(input("Dime la base: "))
# Pregunta por altura
altura=int(input("Dime la altura: "))
# Hace la operación y lo guarda en la variable "area"
area=(base*altura)
# Hace la operación y lo guarda en la variable "Perimetro"
perimetro=2*(base+altura)
# Si es incompatible da error
if base<=0 or altura<=0:
    print ("error")
# Muestra la variable
else:
    print ("Area",area)
    print("Perimetro", perimetro)
#Ejercicio 14
#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.
#Hecho el 03/11/2026
#Por: Juan Agea Rodríguez
numero = int(input("Número de 2 cifras: "))
print("Invertido:", numero % 10 * 10 + numero // 10)  # unidad pasa a decena
#Ejercicio 19
#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
#Hecho el 03/11/2026
#Por: Juan Agea Rodríguez
ok = int(input("Correctas: "))
mal = int(input("Incorrectas: "))
print("Nota:", ok * 5 - mal)  # en blanco = 0, no se cuenta

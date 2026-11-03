#Ejercicio 15
#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuánto valen al final las dos variables.
#Hecho el 03/11/2026
#Por: Juan Agea Rodríguez
A, B = input("A: "), input("B: ")
A, B = B, A  # cambio directo
print("A =", A, "B =", B)
#Ejercicio 20
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
#Hecho el 03/11/2026
#Por: Juan Agea Rodríguez
m2 = int(input("Monedas de 2€: "))
m1 = int(input("Monedas de 1€: "))
m50 = int(input("Monedas de 50c: "))
m20 = int(input("Monedas de 20c: "))
m10 = int(input("Monedas de 10c: "))
cent = m2 * 200 + m1 * 100 + m50 * 50 + m20 * 20 + m10 * 10  #en centimos
print(cent // 100, "euros y", cent % 100, "céntimos")
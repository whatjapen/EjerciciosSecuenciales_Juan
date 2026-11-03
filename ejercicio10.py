#Ejercicio 10
#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes  promedio de sus tres calificaciones parciales, 30% de la calificación del examen final y 15% de la calificación de un trabajo final.
#Hecho el 03/11/2026
#Por: Juan Agea Rodríguez
p1, p2, p3 = float(input("Parcial 1: ")), float(input("Parcial 2: ")), float(input("Parcial 3: "))
ex = float(input("Examen final: "))
tr = float(input("Trabajo final: "))
print("Nota final:", (p1 + p2 + p3) / 3 * 0.55 + ex * 0.30 + tr * 0.15)
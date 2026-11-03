#Ejercicio 17
#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
#Hecho el 03/11/2026
#Por: Juan Agea Rodríguez
hh, mm, ss = int(input("Horas: ")), int(input("Minutos: ")), int(input("Segundos: "))
t = int(input("Segundos de viaje: "))

#hh * 3600: horas a segundos (1 hora = 3600 s).
#mm * 60: minutos a segundos.
#(asi sucesivamente)

s = hh * 3600 + mm * 60 + ss + t  #86400 s. Si pasa de un día, vuelve a 0
print("Llegada:", s // 3600 % 24, "h", s // 60 % 60, "min", s % 60, "s")

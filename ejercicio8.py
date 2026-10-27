#Ejercicio 8
#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
#Hecho el 27/10/2026
#Por: Juan Agea Rodríguez
sueldo=int(input("sueldo: "))
ventas=int(input("ventas: "))
comision=0.10*ventas
final=comision+sueldo
print ("Sueldo base: ", sueldo)
print ("tiene ", final, "sumandole las comisiones")
print ("% en comisiones: ", comision)
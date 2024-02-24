"""
Ejercicio #2.

Realice un programa que le solicite al usuario el nombre, y dos valores numericos.
El programa debera mostrar en pantalla el resultado de las siguientes operaciones matematicas.
-Suma.
-Resta.
-Multiplicacion.
-Division.
-Division Entera.
-Potencia.

"""

nombreUsuario=input("Digite su nombre: ")

A=float(input("Digite el primer numero: "))
B=float(input("Digite el segundo numero: "))

print(nombreUsuario, "El resultado de las opersciones es: \n")

print("Suma = ", A + B,"\n")
print("Resta = ", A - B,"\n")
print("Multiplicacion = ", A * B,"\n")
print("Division = ", A / B,"\n")
print("Division entera = ", A // B,"\n")
print("Potencia = ", A ** B,"\n")

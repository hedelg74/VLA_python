"""
Ejercicio #3.

Desarrolle un programa que calcule el total a pagar por la compra de un producto.
Debe solicitar al usuario el precio unitario de un producto y la cantidad que desea comprar,
si la compra es al menos 12 unidades aplique un 20% de descuento.
"""

producto="Camisa"
descuento=0.0

precio=float(input(f"Digite el precio de la {producto}= "))
cantidad=int(input("Digite la cantidad= "))

if cantidad>=12:
    descuento=0.20

totalPagar=precio-(precio*descuento)
print("Total a pagar= ", totalPagar)

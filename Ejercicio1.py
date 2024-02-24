"""
Ejercicio #1

Realice un programa que solicite al cliente el nombre, nombre del articulo y su precio.
Este programa debera tener la capacidad de recibir dos articulos.
Al final debera mostrar el nombre del cliente, los articulos, precios y monto total a pagar.
"""

nombreCliente=input("Digite su nombre: ")

articuloUno=input("Digite el nombre del primer articulo:")
precioArticuloUno=int(input("Digite su precio:"))

articuloDos=input("Digite el nombre del segundo articulo:")
precioArticuloDos=int(input("Digite su precio:"))

totalpagar=precioArticuloUno + precioArticuloDos


print("\nNombre del Cliente:",nombreCliente,"\n" )

print("Descripcion      Precio\n")
print("---------------------------------------")

print(f"{articuloUno}      {precioArticuloUno}")
print(f"{articuloDos}      {precioArticuloDos}")
print()
print("---------------------------------------")

print(f"Total a pagar             {totalpagar}")

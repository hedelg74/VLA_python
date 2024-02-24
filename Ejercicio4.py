
"""
Ejercicio #4.
    Desarrolle un programa que muestre el monto a pagar por una compra.
    Debe tomar en cuenta que si el monto total es superior a $1000,
    debe aplicarse un 15% de descuento.
"""



monto=float(input("Monto de la compra: "))
descuento=0.0

if monto > 1000 :
    descuento=0.15

totalPagar=monto-(monto*descuento)
print("Total a pagar: ",totalPagar )



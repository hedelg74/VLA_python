"""
    Ejercicio #5.

    Desarrolle un programa que muestre el monto a pagar por una compra.
    Debe tomar en cuenta que si el monto es superior a $1000, debe
    aplicarle un descuento de un%15.
"""


monto=float(input("Monto de la compra: "))
descuento=0.15
totalPagar=0
if monto > 1000 :
    totalPagar=monto-(monto*descuento)
else:totalPagar=monto

print("Total a pagar: ",totalPagar )




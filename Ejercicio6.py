"""
    Ejercicio #6.

    Desarrolle un programa que muestre el precio de la entrada al Parque Nacional
    Manuel Antonio, tome en cuenta que un adulto mayor costarricense para 1600 colones
    y los ninos no pagan.
"""




valorEntrada=1600
print("BIENVENDO AL PARQUE MANUEL ANTONIO.","\n")

print("Valor de la entrada.", valorEntrada,"\n")



tipoCliente=int(input("Digite 1 para adulto mayor o 2 para ninos: "))

if tipoCliente==1:
    print("Adulto mayor - Precio entrada: ", valorEntrada)
elif tipoCliente==2: 
    entrada=0
    print("Ninos - Precio entrada", entrada)
else: print("Tipo cliente no valido, intente de nuevo.")

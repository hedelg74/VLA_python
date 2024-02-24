"""
    Ejercicio #7.

    Para comprender con mas detalles el tema  de los operadores relacionales y condicionales, realizaremos
    un programa que permita al usuario seleccionar cual operacion desea realizar entre ellas agregaremos:
    -Suma
    -Resta
    -Multiplicacion
    -Division
    -Division entera
    -Potencia
"""


def main():

    a=int(input("Digite el valor de A: "))
    b=int(input("Digite el valor de B: "))

    print("SUMA=1, RESTA=2, MULTIPLICACION=3, DIVISION=4, DIVISION ENTERA=5, POTENCIA=6.\n")
    operacion = int(input("Que tipo operacion deseas: "))

    if operacion==1:
        print("Suma = ", a+b)
    elif operacion==2:
        print("Resta = ", a-b)
    elif operacion==3:
        print("Multiplicacion = ", a*b)
    elif operacion==4:
        print("Division  = ", a/b)
    elif operacion==5:
        print("Division entera = ", a//b)
    elif operacion==6:
        print("Potencia = ", a**b)
    else:
        print("Operacion No Valida, intente de nuevo.")
    


if __name__=="__main__":
    main()

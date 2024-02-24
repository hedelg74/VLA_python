"""
    Ejercccio #8.

    El operador logico "OR" nos da la oportunidad de trabajar con dos valores comparativos.
    Imaginemos que en una empresa hay dos personas (Saul y David),
    que son los encargados para poder visualizar los registros de la compania. La seccion de las
    credenciales les va permitir solo a estos solo a estos dos ususarios poder ingresar. Podemos afirmar
    si Saul o David digitan su nombre, preguntarles por la contrasena unica, si introducen bien la
    contrasena unica tendran acceso a la informacion. Como podran ver tambien haremos uso de un "if" anidado.
    A continuacion haremos este ejercicio.
    
"""


def main():
    usuarioUno="David"; usuarioUnoPwd="123"; usuarioUnoPin="K1"
    usuarioDos="Saul"; usuarioDosPwd="456"; usuarioDosPin="K2"
    
    nombre=input("Digite su nombre: ")

    if nombre == usuarioUno or nombre == usuarioDos:
        contrasena=input("Digite su contrasena: ")
        if (nombre == usuarioUno and contrasena == usuarioUnoPwd) or (nombre == usuarioDos and contrasena == usuarioDosPwd): 
            pin=input("Digite su Pin: ")
            if (nombre ==  usuarioUno and contrasena == usuarioUnoPwd and pin==usuarioUnoPin) or (nombre ==  usuarioDos and contrasena == usuarioDosPwd and pin==usuarioDosPin):
                print("Acceso a la informacion concedido.")
            else: print("Pin invalido, intente de nuevo.")
        else:print("Contrasena invalida, intente de nuevo.")
  
    else: print("Usted no tiene los privilegios para ingresar.") 

    

if __name__=="__main__":
    main()

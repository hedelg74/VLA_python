def main():
    """Laboratotio 1"""
    import sys
    import time
    import os
    
    def validar_menu(n_items,descripcion):
        while True:
            try:
                opcion=int(input(f"\nElige {descripcion}: "))
            except ValueError:
                print("Debes digitar una opcion valida.")
                continue

            if opcion > n_items:
                print("Debes digitar una opcion valida.")
                continue
            else: break

        return opcion

    def menu_login():
        print("\nPERFILES.")
        print("--------------------------")
        print("1. Administrador.")
        print("2. Personal Almacen.")
        print("3. Cliente/Proveedor.")
        print("4. Salir.")

        opcion=validar_menu(4,"un perfil")
        return opcion
        
    def menu_principal():
        print("""\nSISTEMA DE INVENTARIO.
--------------------------
        1. Agregar.
        2. Eliminar.
        3. Actualizar.
        4. Imprimir.
        5. Mantenimiento Usuarios.
        6. Salir.""")

        opcion=validar_menu(6,"una opcion")
        return opcion

    def menu_mantenimiento_usuarios():
        print("""\nMANTENIMIENTO USUARIOS.
-----------------------
        1. Agregar.
        2. Actualizar.
        3. Imprimir.
        4. Salir.""")

        opcion=validar_menu(4,"una opcion")    
        return opcion
    
    def menu_actualizar_usuario():
        print("""\nACTUALIZAR CREDENCIALES DE USUARIO.
-----------------------
        1. Clave.
        2. Pin.
        3. Rol.
        4. Estado.
        5. Salir.""")
        opcion=validar_menu(5,"una opcion")
        return opcion


    usuarios=[["Jose","J123","1546","adm","Activo"],["Ramon","R456","1245","per","Inactivo"],["Carlos","C789","5623","clp","Inactivo"]]
    
    articulos=[["0001","Arroz","Kgs",20,2500],["0002","Frijoles","Kgs",15,750],["0003","Azucar","Kgs",25,3500],
               ["0004","Leche","Lts",20,2500],["0005","Aceite","Lts",35,1800],["0006","Lechuga","Kgs",20,2500],
               ["0007","Harina","Kgs",50,1200],["0008","Jugo Naranja","Lts",50,2500],["0009","Tomate","Kgs",150,2550],
               ["0010","Zanahoria","Kgs",200,450],["0011","Queso Turrialba","Kgs",125,4500],["0012","Vino Tinto","Lts",20,8000]]

    def validar_usuario(nombre,clave,pin,rol):

        for user in usuarios:
            if nombre== user[0]:
                if clave == user[1]:
                    if pin == user[2]:
                        if rol == user[3]:
                            if user[4]=="Activo":
                                return True
                            else:
                                print("\nSu cuenta esta inactiva, consulte al administrador.\n")
                                return False
                
        else:
            print("\nCredenciales no coinciden, intente de nuevo.\n")
            return False
    
    def agregar_articulo(rol):
        if rol=="adm" or rol=="per":
            codigo=generar_codigo()
            descripcion=input("Digite la descripcion del articulo: ")
            unidad=input("Digite su unidad de medida: ")
            existencia=float(input("Digite su existencia: "))
            precio=float(input("Digite su precio: "))

            articulos.append([codigo,descripcion,unidad,existencia,precio])

            print(f"\nEl articulo {codigo}, {descripcion} ha sido agregado con exito.")
        else: print(f"\nNo tienes los permisos para agregar articulos.")  

    def agregar_usuario():
    
        nombre=input("Digite el nombre usuario:")
        clave=input("Digite la clave alfanumerica:")
        pin=input("Digite el pin de usuario (0000):")
        rol=input("Digite el rol de usuario (Aministrador=adm, Personal=per, Cliente/Proveedor=clp): ")
        estado=input("Digite el pin de usuario (Activo/Inactivo):")
        usuarios.extend([nombre,clave,pin,rol])
        print(f"\nUsuario {nombre} ha sido agregado")
     
    def generar_codigo():
        temp_codigos=[]
        for articulo in articulos:
            temp_codigos.append(int(articulo[0]))

        max_cod=str(max(temp_codigos)+1)
        codigo_formato=max_cod.zfill(4)
        
        return codigo_formato
            
    def eliminar_articulo():
        print("\nELIMINAR ARTICULO.")
        print("-----------------------------")
        codigo=input("\nDigite el codigo del articulo (0000): ")
        for articulo in articulos:
            if codigo in articulo:
                desc_temp=articulo[1]
                articulos.remove(articulo)
                print(f"Articulo {codigo} {desc_temp} ha sido eliminado.\n")
                break
        else:
            print("No existe el articulo, intente de nuevo.\n")

    def actualizar_articulo():
        print("\nACTUALIZAR ARTICULO.")
        print("-----------------------------")
        codigo=input("\nDigite el codigo del articulo (0000): ")
        for articulo in articulos:
            if codigo in articulo:

                print(f"Articulo {articulo[0],articulo[1],articulo[2],articulo[3],articulo[4]}.\n")
                existencia=float(input("Digite su existencia: "))
                articulo[3]=existencia

                print("\nExistencia acutalizada")
                print(f"Articulo {articulo[0],articulo[1],articulo[2],articulo[3],articulo[4]}.\n")
                
                break
        else:
            print("No existe el articulo, intente de nuevo.\n")
            
    def actualizar_usuario():
        print("\nACTUALIZAR USUARIO.")
        print("-----------------------------")
        nombre=input("\nDigite el nombre de usuario: ")
        opcion=None
        for usuario in usuarios:
            if nombre in usuario:
                print(f"Usuario {usuario[0],usuario[1],usuario[2],usuario[3],usuario[4]}.\n")
                while opcion!=5:
                    
                    opcion=menu_actualizar_usuario()
                    
                    if opcion==1:
                        clave=input("Digite la clave alfanumerica:")
                        usuario[1]=clave
                    elif opcion==2:
                        pin=input("Digite el pin de usuario (0000):")
                        usuario[2]=pin
                    elif opcion==3:
                        rol=input("Digite el rol de usuario (Aministrador=adm, Personal=per, Cliente/Proveedor=clp): ")
                        usuario[3]=rol
                    elif opcion==4:
                        estado=input("Digite el pin de usuario (Activo/Inactivo):")
                        usuario[4]=estado
                        
                    print("\nUsuario actualizado")
                    print(f"{usuario[0],usuario[1],usuario[2],usuario[3],usuario[4]}.\n")
                
               
        else:
            print("No existe el usuario, intente de nuevo.\n")
       
    def imprimir_articulos():
        print("\nLISTADO DE ARTICULOS.")
        print("_" * 80)
        print("{:5} {:20} {:10} {:13} {}".format("Codigo","Descripcion","Unidad","Cantidad","Precio"))
        print("=" * 80)
        for articulo in articulos:
            print(f"{articulo[0]:8} {articulo[1]:20} {articulo[2]:8} {articulo[3]:8.2f} {articulo[4]:12.2f}")
            print("-" * 80)
            
    def imprimir_usuarios():
        print("\nLISTADO DE USUARIOS.")
        print("_" * 80)
        print("{:5} {:20} {:10} {:13} {}".format("Nombre","Clave","Pin","Rol","Estado"))
        print("=" * 80)
        for usuario in usuarios:
            print(f"{usuario[0]:8} {usuario[1]:20} {usuario[2]:8} {usuario[3]:8} {usuario[4]:12}")
            print("-" * 80)    
      
    opcion=None
    rol=None

    while opcion!=4:
        opcion=menu_login()
            
        if opcion==1: rol="adm"
        elif opcion==2: rol="per"
        elif opcion==3: rol="clp"
        elif opcion==4: break
            
        nombre=input("\nDigite su usuario: ")
        clave=input("Digite su clave: ")
        pin=input("Digite su pin: ")

        if validar_usuario(nombre,clave,pin,rol):
            while opcion!=6:
                opcion=menu_principal()

                if opcion==1:
                    agregar_articulo(rol)
                elif opcion==2:
                    eliminar_articulo()
                elif opcion==3:
                    actualizar_articulo()
                elif opcion==4:
                    imprimir_articulos()
                elif opcion==5:
                    if rol=="adm":
                        while opcion!=4:
                            opcion=menu_mantenimiento_usuarios()
                            if opcion==1:
                                agregar_usuario()
                            elif opcion==2:
                                actualizar_usuario()
                            elif opcion==3:
                                imprimir_usuarios()
                    else: pirn("Solo administradores pueden acceder a este modulo.")
                elif opcion==6:
                    sys.exit()            
            

        

   


if __name__=="__main__":
    main()

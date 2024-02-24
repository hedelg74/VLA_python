def main():
    nombreUsr="Henry"
    usuarioPwd="123"
    usuarioPin="A"

    nombre=input("Digite su nombre de usuario: ")
    print(type(nombre))

    if nombre == nombreUsr:
        contrasena=input("Digite contrasena: ")
        print(type(contrasena))
        if contrasena == usuarioPwd:
            pin=input("Digite su Pin: ")
            print(type(usuarioPin))
            if pin == usuarioPin:
                print("\nMENU PRINCIPAL.")
                print("------------------------")
                print("1. NUTRICION.\n")
                print("2. CASINO.\n")
                print("3. REPUESTOS.\n")

                modulo=int(input("Elija el modulo deseado: "))
                print(type(modulo))

                if modulo==1:
                    print("MODULO NUTRICION.\n")
                    print("------------------------")
                    print("1. LUNES.\n")
                    print("2. MARTES.\n")
                    print("3. MIERCOLES.\n")
                    print("4. JUEVES.\n")

                    dia=int(input("Elija el dia de la semana: "))
                    print(type(dia))
                    
                    if dia==1:
                        print("Dieta para hoy LUNES es: Avena y frutas tropicales.")
                    elif dia==2:
                        print("Dieta para hoy MARTES es: Yogurt y frutas frescas.")
                    elif dia==3:
                        print("Dieta para hoy MIERCOLES es: Cafe y galletas saladas.")
                    elif dia==4:
                        print("Dieta para hoy JUEVES es: Barra energetica y jugo de naranja.")
                    else:print("Dia no valido, intente de nuevo.")                    
                            
                elif modulo==2:
                    print("\nMODULO CASINO.")
                    print("\nCapitales del mundo.")
                    
                    print("------------------------")
                    print("1. CAPITAL DE SIGAPUR?\n")  #5 Singapur
                    print("2. CAPITAL DE CHINA?\n")    #1 Pekin
                    print("3. CAPITAL DE INDIA?\n")    #4 Nueva Delhi
                    print("4. CAPITAL DE SUDAFRICA?\n")#3 Pretoria
                    print("5. CAPITAL DE FELIPINAS?\n")#2 Manila

                    print("Elige una capital:")    
                    print("PEKIN=1, MANILA=2, PRETORIA=3, NUEVA DELHI=4, SINGAPUR=5.\n")    

                    reto=int(input("Seleccione su reto: "))
                    print(type(reto))
                    
                    retosResueltos=0
                    retoUno=False
                    retoDos=False
                    retoTres=False
                    retoCuatro=False
                    retoCinco=False
                    repite=False
                    while reto>=1 and reto<=5:
                        respuesta=int(input(f"Respuesta del reto #{reto} es: "))
                        print(type(respuesta))
                         
                        if reto==1 and retoUno==False:
                            if respuesta==5: 
                                retoUno=True
                                retosResueltos=retosResueltos + 1
                            else: repite=True
                        elif reto==2 and retoDos==False:
                            if respuesta==1:
                                retoDos=True
                                retosResueltos=retosResueltos + 1
                            else: repite=True
                            
                        elif reto==3 and retoTres==False:
                            if respuesta==4:
                                retoTres=True
                                retosResueltos=retosResueltos + 1
                            else: repite=True
                            
                        elif reto==4 and retoCuatro==False:
                            if respuesta==3:
                                retoCuatro=True
                                retosResueltos=retosResueltos + 1
                            else: repite=True
                            
                        elif reto==5 and retoCinco==False:
                            if respuesta==2:
                                retoCinco=True
                                retosResueltos=retosResueltos + 1
                            else: repite=True
                           
                        if repite==True:
                            repite=False
                            print("Realice de nuevo el reto #",reto)
                            continue
                        elif retosResueltos<5:
                            print("Retos resueltos= ",retosResueltos)
                            resuelto=False
                            while resuelto==False:
                                reto=int(input("Seleccione otro reto: "))
                                if reto==1 and retoUno==True: resuelto=True 
                                elif reto==2 and retoDos==True: resuelto=True 
                                elif reto==3 and retoTres==True: resuelto=True
                                elif reto==4 and retoCuatro==True: resuelto=True
                                elif reto==5 and retoCinco==True: resuelto=True
                                else: break    
                                if resuelto==True:
                                    print(f"Reto #{reto} ha sido resuelto.")
                                    resuelto=False
                        else:
                            print("Retos resueltos= ",retosResueltos)
                            print("Siguiente Nivel.")
                            break
                    
                elif modulo==3:
                    print("\nMODULO REPUESTOS.")
                    
                    print("------------------------")
                    print("1. REPUESTOS PARA EL MOTOR.\n")  
                    print("2. REPUESTOS ACCESORIOS.\n")    
                    print("3. REPUESTOS PARA LIMPIEZA DEL AUTO.\n") 
                    print("4. REPUESTOS PARA LOS FRENOS.\n")
  
                    tipo=int(input("Escoja el tipo de repuesto: "))
                    print(type(tipo))

                    subTotal=0
                    totalPagar=0
                    descuento=0
                    proceder=True
                    
                    if tipo==1:
                        descuento=0.15
                        
                        print("1. PISTON.\n")  
                        print("2. ANILLO.\n")    
                        print("3. EMPAQUE\.n")
                          
                        repuesto=int(input("Escoja el repuesto: "))
                        print(type(repuesto))
                        if repuesto==1:
                            precio=5000
                            item="Piston"
                        elif repuesto==2:
                            item="Anillo"
                            precio=3000
                        elif repuesto==3:
                            item="Empaque"
                            precio=2000
                        else:
                            print("Repuesto no existe, intente de nuevo")
                            proceder=False
                                          
                    elif tipo==2:
                        descuento=0.10
                            
                        print("1. BOTAGUAS.\n")  
                        print("2. LUCES NEON.\n")    
                        print("3. RADIO AM/FM.\n")
                          
                        repuesto=int(input("Escoja el accesorio: "))
                        print(type(repuesto))
                        if repuesto==1:
                            precio=2500
                            item="Botaguas"
                        elif repuesto==2:
                            item="Luces Neon"
                            precio=6000
                        elif repuesto==3:
                            item="Radio am/fm."
                            precio=15000
                        else:
                            print("Accesorio no existe, intente de nuevo")
                            proceder=False

                    elif tipo==3:
                        descuento=0.05
                            
                        print("1. NAIS.\n")  
                        print("2. CHAMPU.\n")    
                        print("3. CERA.\n")
                          
                        repuesto=int(input("Escoja el producto: "))
                        print(type(repuesto))
                        if repuesto==1:
                            precio=5000
                            item="Nais"
                        elif repuesto==2:
                            item="Champu"
                            precio=8000
                        elif repuesto==3:
                            item="Cera"
                            precio=4000
                        else:
                            print("Producto no existe, intente de nuevo")
                            proceder=False
                        
                    elif tipo==4:
                        descuento=0.03
                            
                        print("1. FIBRA.\n")  
                        print("2. MANGUERA.\n")    
                        print("3. DISCO.\n")
                          
                        repuesto=int(input("Escoja el repuesto: "))
                        print(type(repuesto))
                        if repuesto==1:
                            precio=6000
                            item="Fibra"
                        elif repuesto==2:
                            item="Manguera"
                            precio=9000
                        elif repuesto==3:
                            item="Disco"
                            precio=25000
                        else:
                            print("Repuesto no existe, intente de nuevo")
                            proceder=False

                    else:
                        print("Tipo categoria no existe, intente de nuevo")
                        proceder=False

                    if proceder==True:
                        cantidad=int(input("Digite la cantidad: "))
                        print(type(cantidad))
                        subTotal=cantidad*precio
                        totalPagar=subTotal-(subTotal*descuento)
                        descuento=subTotal*descuento
               
                        print("\nDescripcion     Cantidad     Precio     Total")
                        print("---------------------------------------------------")
                        print(f"{item}           {cantidad}           {precio}     {subTotal}")
                        print("---------------------------------------------------")
                        print(f"Descuento                              {descuento}")
                        print(f"Total a pagar                         {totalPagar}")

                else:print("Modulo no valido, intente de nuevo.")                    
            else:print("Pin invalido, intente de nuevo.")                
        else:print("Contrasena invalida, intente de nuevo.")            
    else: print("Nombre de usuario invalido, intente de nuevo.")
    

if __name__=="__main__":
    main()

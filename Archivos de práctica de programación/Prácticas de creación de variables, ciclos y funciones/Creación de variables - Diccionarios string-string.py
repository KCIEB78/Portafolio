# Función para crear diccionarios de entradas string e información gramatical string

def creacion_dss():

    lista_dss = []
    numero_dss = 1
    cancelacion = False

    while not cancelacion:

        while True:
            
            try:
                cant_d = int(input("¿Cuántos diccionarios desea crear? (Solamente números): "))
                print("-" * 100)
                print("Cantidad valida")
                print("-" * 100)
                

            except ValueError:
                print("-" * 100)
                print("Entrada no valida, favor de intentarlo de nuevo")
                print("-" * 100)
                continue

            if cant_d <= 0:
                print("Creación de diccionarios cancelada")
                print("-" * 100)
                break

            elif cant_d > 0:
                
                for i in range(cant_d):
                    
                    entrada_e = input("Escriba la entrada del diccionario: ").strip().capitalize()
                    
                    if entrada_e == "Cancelar":
                        print("-" * 100)
                        print("Creación del diccionario cancelado")
                        print("-" * 100)
                        break
                    
                    inf_gram = input("Escriba la información gramatical de la entrada: ")
                    
                    if inf_gram == "Cancelar":
                        print("-" * 100)
                        print("Creación del diccionario cancelado")
                        print("-" * 100)
                        break

                    lista_dss.append({entrada_e : inf_gram})
                    print("-" * 100)
                    print(f'Lista número {numero_dss} creada exitosamente')
                    print("-" * 100)
                    numero_dss = numero_dss + 1
                    
                break
        
        while True:
            continuar = str(input("¿Desea continuar con la creación de diccionarios? (Si / No): ")).strip().capitalize()

            if continuar == "No":
                print("-" * 100)
                print("Entrada valida - Creación de diccionarios terminada")
                print("-" * 100)
                for index, diccionarios in enumerate(lista_dss, start = 1):
                    print("-" * 100)
                    print(f'El diccionario número {index} contiene: {diccionarios}')
                    print("-" * 100)
                cancelacion = True
                break

            elif continuar == "Si":
                print("-" * 100)
                print("Entrada valida - Se continuará con la creación de diccionarios")
                print("-" * 100)
                break

            else:
                print("-" * 100)
                print("Opción no válida - Favor de ingresar una opción valida")
                print("-" * 100)

    return print("Diccionarios creados en la variable 'lista_dss'")
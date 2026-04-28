# Función para crear listas

list_dict = []
el_list_dict = []
cant_el_list = 1
cancelacion = False
cancelacion2 = False
cancelacion3 = False

print("-" * 100)

while not cancelacion:

    while True:

        try:

            cantidad_list = int(input("¿Cuántos elementos deseas agregar a la lista? (Solamente números): "))
            print("-" * 100)
            print("Cantidad válida")
            print("-" * 100)

        except ValueError:

            print("-" * 100)
            print("Entrada no válida - Favor de intentarlo de nuevo")
            print("-" * 100)
            continue

        if cantidad_list <= 0:

            print("Creación de la lista para el diccionario cancelada")
            print("-" * 100)
            break

        elif cantidad_list > 0:
            
            for i in range(cantidad_list):
                
                tipo_elemento_l = input("¿Qué tipo de dato deseas agregar a la lista? (Str / Int / Float): ").strip().capitalize()
                print("-" * 100)

                if tipo_elemento_l == "Str":

                    list_str = input("Escriba el elemento que desea agregar: ")
                    
                    if list_str == "Cancelar":
                        print("-" * 100)
                        print("Creación del elemento cancelado")
                        print("-" * 100)
                        break

                    list_dict.append(list_str)
                    print("-" * 100)
                    print(f"Elemento número {cant_el_list} agregado exitosamente")
                    print("-" * 100)
                    cant_el_list = cant_el_list + 1

                    break

                elif tipo_elemento_l == "Int":
                    
                    while True:
                        
                        try:
                        
                            list_int = int(input("Escriba cualquier número, excepto el 0: "))
                            print("-" * 100)
                            print("Cantidad válida")
                        
                        except ValueError:

                            print("-" * 100)
                            print("Elemento no válido - Favor de intentarlo de nuevo")
                            print("-" * 100)
                            continue
                            
                        if list_int == 0:

                            print("-" * 100)
                            print("Creación del elemento cancelado")
                            print("-" * 100)
                            break

                        elif list_int > 0 or list_int < 0:

                            list_dict.append(list_int)
                            print("-" * 100)
                            print(f"Elemento número {cant_el_list} agregado exitosamente")
                            print("-" * 100)
                            cant_el_list = cant_el_list + 1
                            break

                elif tipo_elemento_l == "Float":
                
                    while True:
                        
                        try:
                        
                            list_float = float(input("Escriba cualquier número, excepto el 0: "))
                            print("-" * 100)
                            print("Cantidad válida")
                        
                        except ValueError:

                            print("-" * 100)
                            print("Elemento no válido - Favor de intentarlo de nuevo")
                            print("-" * 100)
                            continue

                        if list_float == 0.0:

                            print("-" * 100)
                            print("Creación del elemento cancelado")
                            print("-" * 100)
                            break

                        elif list_float > 0.0 or list_float < 0.0:

                            list_dict.append(list_float)
                            print("-" * 100)
                            print(f"Elemento número {cant_el_list} agregado exitosamente")
                            print("-" * 100)
                            cant_el_list = cant_el_list + 1
                            break

                else:

                    print("Opción no válida - Favor de intentarlo de nuevo")
                    print("-" * 100)

            break

    while True:

        continuar = input("¿Desea continuar agregando elementos a la lista? (Si / No): ").strip().capitalize()

        if continuar == "No":
            
            print("-" * 100)
            print("Entrada valida - Creación de la lista terminada")
            print("-" * 100)
            print(f'''Lista creada en la variable 'list_dict':
            {list_dict}''')
            print("-" * 100)
            cancelacion = True
            break

        elif continuar == "Si":

            print("-" * 100)
            print("Entrada valida - Se continuará agregando elementos a la lista")
            print("-" * 100)
            break

        else:

            print("-" * 100)
            print("Entrada no válida - Favor de ingresar una opción válida")
            print("-" * 100)
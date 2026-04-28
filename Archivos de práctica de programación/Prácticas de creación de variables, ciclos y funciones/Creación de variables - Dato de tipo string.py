# Función para crear diccionarios de datos string

def creacion_dato_string():

    cancelacion = False

    print("-" * 100)

    while not cancelacion:
    
        dato_str = input("Escriba el dato de tipo string: ").strip().capitalize()
        
        if dato_str == "Cancelar":
            
            print("-" * 100)
            print("Creación de la variable cancelada")
            print("-" * 100)
            break

        print("-" * 100)
        print('Creación de de la variable con el dato de tipo string exitosa')
        print("-" * 100)

        
        while True:

            continuar = input("¿Quieres cambiar el dato creado en la variable? (Si / No): ").strip().capitalize()

            if continuar == "No":
                print("-" * 100)
                print("Entrada valida - Variable creada correctamente")
                print("-" * 100)
                print(dato_str)
                print("-" * 100)
                cancelacion = True
                break

            elif continuar == "Si":
                print("-" * 100)
                print("Entrada valida - Cambiando el dato de la variable")
                print("-" * 100)
                break

            else:
                print("-" * 100)
                print("Opción no válida - Favor de ingresar una opción valida")
                print("-" * 100)

    return print("Dato de tipo string creado en la variable 'dato_str'")

creacion_dato_string()
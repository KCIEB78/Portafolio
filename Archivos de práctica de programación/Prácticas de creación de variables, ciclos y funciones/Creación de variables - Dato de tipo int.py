# Función para crear diccionarios de datos string

def creacion_dato_int():

    cancelacion = False

    print("-" * 100)

    while not cancelacion:

        while True:
            
            try:
                
                dato_str = int(input("Escriba el valor que desea definir en la variable: "))
                print("-" * 100)
                print("Entrada válida")
                print("-" * 100)
                break

            except ValueError:

                print("-" * 100)
                print("Dato no válido - Favor de intentarlo nuevamente")
                print("-" * 100)
                continue

            if dato_str == 0:
                print("Creación de la variable cancelada")
                print("-" * 100)
                break

            elif dato_str > 0 or dato_str < 0:
                print("Dato válido - Variable creada correctamente")
                print("-" * 100)


        while True:

            continuar = str(input("¿Desea cambiar el dato de la variable? (Si / No): ")).strip().capitalize()

            if continuar == "No":
                print("-" * 100)
                print("Entrada valida - Creación de la variable terminada")
                print("-" * 100)
                print(dato_str)
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

    return print("Dato de tipo int creada en la variable 'dato_str'")

creacion_dato_int()
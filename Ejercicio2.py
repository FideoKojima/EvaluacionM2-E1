# Números Secuenciales con Saltos

def juego_numeros():
    # Solicitamos y validamos el número inicial
    try:
        numero = int(input("Ingrese un número del 1 al 9: "))
        if numero < 1 or numero > 9:
            raise ValueError("El número debe estar entre 1 y 9")
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"Ingrese números secuenciales, saltando múltiplos de {numero}:")

    # Inicializamos variables para el juego
    numero_esperado = 1
    numero_ingresado = 0

    # Bucle principal del juego
    while numero_ingresado != -1:
        # Saltamos los múltiplos del número inicial
        while numero_esperado % numero == 0:
            numero_esperado += 1

        # Solicitamos el siguiente número al usuario
        try:
            numero_ingresado = int(input(f"Ingrese {numero_esperado}: "))
        except ValueError:
            print(f"Error: Debe ingresar un número entero.")
            continue

        # Verificamos si el número ingresado es correcto
        if numero_ingresado == numero_esperado:
            numero_esperado += 1
        elif numero_ingresado == -1:
            print("Juego terminado.")
        else:
            print(f"Error: Número incorrecto. Debía ingresar {numero_esperado}.")

# Ejecutamos el juego
juego_numeros()
import sys
import datetime

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Dibujar matriz")
        print("2. Juego de números secuenciales")
        print("3. Calculadora de años bisiestos")
        print("4. Reemplazo de letras en frase")
        print("0. Salir")
        
        opcion = input("Seleccione un ejercicio (0-4): ")
        
        if opcion == '1':
            dibujar_matriz()
        elif opcion == '2':
            juego_numeros()
        elif opcion == '3':
            contar_anos_bisiestos()
        elif opcion == '4':
            reemplazar_letras()
        elif opcion == '0':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def dibujar_matriz():
    while True:
        print("\nDibujar Matriz (ingrese '0' para volver al menú principal)")
        filas = input("Ingrese la cantidad de filas: ")
        if filas == '0':
            return
        columnas = input("Ingrese la cantidad de columnas: ")
        if columnas == '0':
            return
        
        try:
            filas = int(filas)
            columnas = int(columnas)
            if filas <= 0 or columnas <= 0:
                raise ValueError("El número de filas y columnas debe ser mayor que 0.")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        for i in range(filas):
            for j in range(columnas):
                if i == 0 or i == filas - 1 or j == 0 or j == columnas - 1:
                    print("+", end="  ")  # Espacio adicional para mejor visualización
                else:
                    print(" ", end="  ")
            print()

def juego_numeros():
    while True:
        print("\nJuego de Números Secuenciales (ingrese '0' para volver al menú principal)")
        numero = input("Ingrese un número del 1 al 9: ")
        if numero == '0':
            return
        
        try:
            numero = int(numero)
            if numero < 1 or numero > 9:
                raise ValueError("El número debe estar entre 1 y 9.")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        print(f"Ingrese números secuenciales, saltando múltiplos de {numero}. Ingrese -1 para terminar la secuencia.")

        numero_esperado = 1
        while True:
            while numero_esperado % numero == 0:
                numero_esperado += 1

            entrada = input(f"Ingrese {numero_esperado}: ")
            if entrada == '0':
                return

            try:
                numero_ingresado = int(entrada)
            except ValueError:
                print(f"Error: Debe ingresar un número entero.")
                continue

            if numero_ingresado == -1:
                print("Secuencia terminada.")
                break
            elif numero_ingresado == numero_esperado:
                numero_esperado += 1
            else:
                print(f"Error: Número incorrecto. Debía ingresar {numero_esperado}.")

def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def contar_anos_bisiestos():
    while True:
        print("\nCalculadora de Años Bisiestos (ingrese '0' para volver al menú principal)")
        anio_actual = datetime.datetime.now().year

        anio_nacimiento = input("Ingrese el año de nacimiento: ")
        if anio_nacimiento == '0':
            return
        anio_muerte = input("Ingrese el año de muerte (o presione Enter si aún vive): ")
        if anio_muerte == '0':
            return

        try:
            anio_nacimiento = int(anio_nacimiento)
            anio_muerte = int(anio_muerte) if anio_muerte else anio_actual
            if anio_nacimiento < 0 or anio_nacimiento > anio_actual:
                raise ValueError("El año de nacimiento debe ser un número positivo y no mayor al año actual.")
            if anio_muerte < anio_nacimiento:
                raise ValueError("El año de muerte debe ser mayor o igual que el año de nacimiento.")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        anos_bisiestos = sum(1 for anio in range(anio_nacimiento, anio_muerte + 1) if es_bisiesto(anio))
        print(f"La persona ha vivido {anos_bisiestos} años bisiestos.")

def validar_palabras(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return False
    return all(a != b for a, b in zip(palabra1, palabra2))

def crear_diccionario_reemplazo(palabra1, palabra2):
    return {a: b for a, b in zip(palabra1, palabra2)}

def reemplazar_letras():
    while True:
        print("\nReemplazo de Letras en Frase (ingrese '0' para volver al menú principal)")
        palabra1 = input("Ingrese la primera palabra: ")
        if palabra1 == '0':
            return
        palabra2 = input("Ingrese la segunda palabra: ")
        if palabra2 == '0':
            return

        palabra1 = palabra1.lower()
        palabra2 = palabra2.lower()

        if not validar_palabras(palabra1, palabra2):
            print("Error: Las palabras deben tener la misma longitud y no coincidir en ninguna posición.")
            continue

        reemplazo = crear_diccionario_reemplazo(palabra1, palabra2)
        frase_original = input("Ingrese la frase a modificar: ")
        if frase_original == '0':
            return

        frase_modificada = ''.join(reemplazo.get(letra.lower(), letra) for letra in frase_original)

        print("Frase original:", frase_original)
        print("Frase modificada:", frase_modificada)

if __name__ == "__main__":
    menu_principal()

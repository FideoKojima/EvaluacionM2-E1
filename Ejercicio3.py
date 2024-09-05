# Cálculo de Años Bisiestos Vividos

# Pedimos al usuario que ingrese dos palabras de igual longitud
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

# Validamos que ambas palabras tengan la misma longitud
if len(palabra1) != len(palabra2):
    print("Error: Las palabras deben tener la misma longitud.")
else:
    # Solicitamos al usuario que ingrese una frase
    frase = input("Ingrese una frase: ")

    # Creamos un diccionario para almacenar las reglas de reemplazo
    reemplazos = {}
    
    # Rellenamos el diccionario con las reglas de reemplazo
    for i in range(len(palabra1)):
        reemplazos[palabra1[i]] = palabra2[i]

    # Creamos una nueva frase reemplazando las letras
    nueva_frase = ""
    for letra in frase:
        # Si la letra está en las reglas de reemplazo, la reemplazamos
        if letra in reemplazos:
            nueva_frase += reemplazos[letra]
        else:
            nueva_frase += letra

    # Mostramos la nueva frase con los reemplazos
    print("Nueva frase:", nueva_frase)

# La variable 'reemplazos' es un diccionario que guarda las reglas de reemplazo entre las dos palabras.
# La variable 'nueva_frase' almacena la frase modificada con las letras reemplazadas.

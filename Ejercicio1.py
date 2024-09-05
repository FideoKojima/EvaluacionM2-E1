# Dibujar una Matriz

# Solicitamos al usuario la cantidad de filas
filas = int(input("Ingrese la cantidad de filas: "))

# Solicitamos al usuario la cantidad de columnas
columnas = int(input("Ingrese la cantidad de columnas: "))

# Este bucle itera por cada fila
for i in range(filas):
    # Inicializamos una pleaca
    fila = "|"
    # Este bucle itera por cada columna en la fila actual
    for j in range(columnas):
        # Agregamos una pleca y  un signo suma a la fila
        fila += "+|"
    # Imprimimos la fila completa
    print(fila)

# En este ejercicio, las variables 'filas' y 'columnas' son importantes porque controlan el tamaño de la matriz.

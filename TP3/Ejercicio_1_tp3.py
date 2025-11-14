"""
    1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento,
    imprimiendo la matriz luego de invocar a cada función:
    
    a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
    teclado.
    
    b. Ordenar en forma ascendente cada una de las filas de la matriz.
    
    c. Intercambiar dos filas, cuyos números se reciben como parámetro.
    
    d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
    
    e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
    
    f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
    parámetro.
    
    g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
    
    h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
    
    i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
    
    j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
    una lista con los números de las mismas.
    
    NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
    sea el valor ingresado.
"""
def cargar_matriz(tamano: int) -> list:
    """
    Carga una matriz de tamaño N x N con números enteros ingresados por el usuario.

    Pre:
        - tamano (int): Tamaño de la matriz (N).
    
    Post:
        - list: Matriz de enteros cargada.
    """
    matriz = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            num = int(input(f'Ingrese un número entero para la fila {i + 1} y columna {j + 1}: '))
            fila.append(num)
        matriz.append(fila)
    return matriz

def copiar_matriz(matriz: list) -> list:
    """
    Crea una copia de la matriz dada.

    Pre:
        - matriz (list): Matriz de enteros.
    
    Post:
        - list: Copia de la matriz.
    """
    return [fila.copy() for fila in matriz]

def ordenar_filas(matriz: list) -> list:
    """
    Ordena en forma ascendente cada una de las filas de la matriz.

    Pre:
        - matriz (list): Matriz de enteros.
    
    Post:
        - list: Matriz con filas ordenadas.
    """
    matriz_copiada = copiar_matriz(matriz)
    for fila in matriz_copiada:
        fila.sort()
    return matriz_copiada

def intercambiar_filas(matriz: list, fila1: int, fila2: int) -> list:
    """
    Intercambia dos filas en la matriz.

    Pre:
        - matriz (list): Matriz de enteros.
        - fila1 (int): Índice de la primera fila (1-indexed).
        - fila2 (int): Índice de la segunda fila (1-indexed).
    
    Post:
        - list: Matriz con filas intercambiadas.
    """
    if fila1 < 1 or fila1 > len(matriz) or fila2 < 1 or fila2 > len(matriz):
        print("ERROR: Las filas a intercambiar están fuera del rango.")
        return matriz
    
    matriz[fila1 - 1], matriz[fila2 - 1] = matriz[fila2 - 1], matriz[fila1 - 1]
    return matriz

def intercambiar_columnas(matriz: list, col1: int, col2: int) -> list:
    """
    Intercambia dos columnas en la matriz.

    Pre:
        - matriz (list): Matriz de enteros.
        - col1 (int): Índice de la primera columna (1-indexed).
        - col2 (int): Índice de la segunda columna (1-indexed).
    
    Post:
        - list: Matriz con columnas intercambiadas.
    """
    for i in range(len(matriz)):
        matriz[i][col1 - 1], matriz[i][col2 - 1] = matriz[i][col2 - 1], matriz[i][col1 - 1]
    return matriz

def transponer_matriz(matriz: list) -> list:
    """
    Transpone la matriz (intercambia filas por columnas).

    Pre:
        - matriz (list): Matriz de enteros.
    
    Post:
        - list: Matriz transpuesta.
    """
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def calcular_promedio_fila(matriz: list, fila: int) -> float:
    """
    Calcula el promedio de los elementos de una fila.

    Pre:
        - matriz (list): Matriz de enteros.
        - fila (int): Índice de la fila (1-indexed).
    
    Post:
        - float: Promedio de la fila.
    """
    return sum(matriz[fila - 1]) / len(matriz[fila - 1])

def calcular_porcentaje_impares(matriz: list, col: int) -> float:
    """
    Calcula el porcentaje de elementos impares en una columna.

    Pre:
        - matriz (list): Matriz de enteros.
        - col (int): Índice de la columna (1-indexed).
    
    Post:
        - float: Porcentaje de elementos impares en la columna.
    """
    total_elementos = len(matriz)
    contador_impares = sum(1 for i in range(total_elementos) if matriz[i][col - 1] % 2 == 1)
    return (contador_impares / total_elementos) * 100

def es_simetrica_principal(matriz: list) -> bool:
    """
    Determina si la matriz es simétrica respecto a su diagonal principal.

    Pre:
        - matriz (list): Matriz de enteros.
    
    Post:
        - bool: True si es simétrica, False en caso contrario.
    """
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def es_simetrica_secundaria(matriz: list) -> bool:
    """
    Determina si la matriz es simétrica respecto a su diagonal secundaria.

    Pre:
        - matriz (list): Matriz de enteros.
    
    Post:
        - bool: True si es simétrica, False en caso contrario.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n - j - 1][n - i - 1]:
                return False
    return True

def columnas_palindromas(matriz: list) -> list:
    """
    Determina qué columnas de la matriz son palíndromos (capicúas).

    Pre:
        - matriz (list): Matriz de enteros.
    
    Post:
        - list: Lista de índices de columnas palíndromas (0-indexed).
    """
    columnas_palindromas = []
    n_filas = len(matriz)
    n_columnas = len(matriz[0])

    for j in range(n_columnas):
        capicua = True
        for i in range(n_filas // 2):
            if matriz[i][j] != matriz[n_filas - i - 1][j]:
                capicua = False
                break
        if capicua:
            columnas_palindromas.append(j)
    
    return columnas_palindromas

def imprimir_matriz(matriz: list) -> None:
    """
    Imprime la matriz formateada.

    Pre:
        - matriz (list): Matriz de enteros.
    
    Post:
        Ninguna.
    """
    print('-' * (4 * len(matriz[0]) + 1))
    for fila in matriz:
        print('|', end='')
        for elemento in fila:
            print(f'{elemento:>2}|', end='')
        print()
    print('-' * (4 * len(matriz[0]) + 1))
    print()

def main() -> None:
    """
    Función principal que ejecuta el programa.

    Pre:
        Ninguna.
    
    Post:
        Imprime resultados de varias operaciones sobre la matriz.
    """
    try:
        tamano = int(input("Ingrese el tamaño de la matriz (N): "))
        matriz1 = cargar_matriz(tamano)
        if not matriz1:
            return

        print('Matriz original:')
        imprimir_matriz(matriz1)

        print('Filas ordenadas:')
        imprimir_matriz(ordenar_filas(copiar_matriz(matriz1)))
        
        fila1 = int(input("Ingrese el índice de la primera fila a intercambiar (1-indexed): "))
        fila2 = int(input("Ingrese el índice de la segunda fila a intercambiar (1-indexed): "))
        print('Intercambiando filas:', fila1, 'y', fila2)
        imprimir_matriz(intercambiar_filas(copiar_matriz(matriz1), fila1, fila2))
        
        col1 = int(input("Ingrese el índice de la primera columna a intercambiar (1-indexed): "))
        col2 = int(input("Ingrese el índice de la segunda columna a intercambiar (1-indexed): "))
        print('Intercambiando columnas:', col1, 'y', col2)
        imprimir_matriz(intercambiar_columnas(copiar_matriz(matriz1), col1, col2))
        
        print('Matriz transpuesta:')
        imprimir_matriz(transponer_matriz(copiar_matriz(matriz1)))
        
        fila_promedio = int(input("Ingrese el índice de la fila para calcular el promedio (1-indexed): "))
        print('Promedio de la fila', fila_promedio, ':', calcular_promedio_fila(matriz1, fila_promedio))
        
        col_porcentaje = int(input("Ingrese el índice de la columna para calcular el porcentaje de impares (1-indexed): "))
        print(f'Porcentaje de impares en la columna {col_porcentaje}: {calcular_porcentaje_impares(matriz1, col_porcentaje):.2f}%')
        
        if es_simetrica_principal(matriz1):
            print('La matriz es simétrica respecto a su diagonal principal.')
        else:
            print('La matriz no es simétrica respecto a su diagonal principal.')
        
        if es_simetrica_secundaria(matriz1):
            print('La matriz es simétrica respecto a su diagonal secundaria.')
        else:
            print('La matriz no es simétrica respecto a su diagonal secundaria.')
        
        print('Columnas palíndromas:', columnas_palindromas(matriz1))
    
    except ValueError:
        print("ERROR: Ingrese un número entero válido.")

if __name__ == "__main__":
    main()


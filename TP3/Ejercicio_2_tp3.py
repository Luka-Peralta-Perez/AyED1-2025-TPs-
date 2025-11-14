"""
    2. Las siguientes matrices responden distintos patrones de relleno. Desarrollar funciones que generen cada una de ellas sin intervención humana y escribir un programa
    que las invoque e imprima por pantalla. El tamaño de las matrices debe establecerse como N x N, donde N se ingresa a través del teclado.

"""
def matriz_a(n: int) -> list:
    
    matriz = [[0] * n for _ in range(n)]
    num_impar = 1
    for i in range(n):
        matriz[i][i] = num_impar
        num_impar += 2
    return matriz

def matriz_b(n: int) -> list:
    
    matriz = [[0] * n for _ in range(n)]
    num = 3 ** (n - 1)
    for i in range(n):
        matriz[i][n - 1 - i] = num
        num //= 3
    return matriz

def matriz_c(n: int) -> list:
    
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            matriz[i][j] = n - i
    return matriz

def matriz_d(n: int) -> list:
    
    matriz = [[(2 ** (n - 1) // (2 ** i))] * n for i in range(n)]
    return matriz

def matriz_e(n: int) -> list:
   
    matriz = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 != 0:
                matriz[i][j] = num
                num += 1
    return matriz

def matriz_f(n: int) -> list:
    
    matriz = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(n):
            if i >= j:
                matriz[i][n - 1 - j] = num
                num += 1
    return matriz

def matriz_g(n: int) -> list:
    
    matriz = [[0] * n for _ in range(n)]
    num = 1
    inicio_fila, fin_fila = 0, n - 1
    inicio_col, fin_col = 0, n - 1

    while inicio_fila <= fin_fila and inicio_col <= fin_col:
        for col in range(inicio_col, fin_col + 1):
            matriz[inicio_fila][col] = num
            num += 1
        inicio_fila += 1

        for fila in range(inicio_fila, fin_fila + 1):
            matriz[fila][fin_col] = num
            num += 1
        fin_col -= 1

        if inicio_fila <= fin_fila:
            for col in range(fin_col, inicio_col - 1, -1):
                matriz[fin_fila][col] = num
                num += 1
            fin_fila -= 1

        if inicio_col <= fin_col:
            for fila in range(fin_fila, inicio_fila - 1, -1):
                matriz[fila][inicio_col] = num
                num += 1
            inicio_col += 1
    return matriz

def matriz_h(n: int) -> list:
    
    matriz = [[0] * n for _ in range(n)]
    num = 1
    for i in range(2 * n - 1):
        if i < n:
            for j in range(i + 1):
                matriz[j][i - j] = num
                num += 1
        else:
            for j in range(i - n + 1, n):
                matriz[j][i - j] = num
                num += 1
    return matriz

def matriz_i(n: int) -> list:
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        matriz[i][i] = i + 1
    return matriz

def imprimir_matriz(matriz: list) -> None:
    for fila in matriz:
        print(fila)

def main() -> None:
    """Función principal que ejecuta el programa."""
    n = int(input("Valor de N (tamaño de la matriz): "))

    print("\nMatriz A:")
    imprimir_matriz(matriz_a(n))

    print("\nMatriz B:")
    imprimir_matriz(matriz_b(n))

    print("\nMatriz C:")
    imprimir_matriz(matriz_c(n))

    print("\nMatriz D:")
    imprimir_matriz(matriz_d(n))

    print("\nMatriz E:")
    imprimir_matriz(matriz_e(n))

    print("\nMatriz F:")
    imprimir_matriz(matriz_f(n))

    print("\nMatriz G:")
    imprimir_matriz(matriz_g(n))

    print("\nMatriz H:")
    imprimir_matriz(matriz_h(n))

    print("\nMatriz I:")
    imprimir_matriz(matriz_i(n))

main()

"""
    3. Desarrollar un programa para rellenar una matriz de N x N con números enteros al
    azar comprendidos en el intervalo [0,N2),
    de tal forma que ningún número se repita. Imprimir la matriz por pantalla.
"""
import random

def generar_matriz_aleatoria(n: int) -> list:
    """
    Genera una matriz de tamaño N x N con números enteros al azar en el intervalo [0, N^2),
    asegurando que no haya números repetidos.

    Pre:
        n > 0

    Post:
        Matriz de tamaño N x N con números únicos en [0, N^2).
    """
    numeros = list(range(n**2))  # Crea una lista con los números únicos
    random.shuffle(numeros)       # Baraja los números para aleatorizarlos
    matriz = [numeros[i*n:(i+1)*n] for i in range(n)]  # Divide la lista en filas para formar la matriz
    return matriz

def imprimir_matriz(matriz: list) -> None:
    """
    Imprime una matriz en formato de tabla.

    """
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

def main() -> None:
    """    
    Funcion principal del programa
    """
    n = int(input("Ingrese el tamaño de la matriz (N): "))
    matriz = generar_matriz_aleatoria(n)
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()

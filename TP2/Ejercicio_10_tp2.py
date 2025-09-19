"""
    10. Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
    elementos de la primera que sean impares. El proceso deberá realizarse utilizando
     función filter(). Imprimir las dos listas por pantalla. 
"""
from random import randint
from typing import List

def num_random() -> List[int]:
    """
    Genera una lista de 100 números aleatorios entre 1 y 100.

    Post:
    - Retorna una lista de números aleatorios.
    """
    return [randint(1, 100) for i in range (100)]
    
def num_impares(numeros: List[int]) -> List[int]:
    """
    Filtra los números impares de una lista.

    Pre:
    - numeros (List[int]): Lista de números enteros.

    Post:
    - Retorna una lista con los números impares.
    """
    return list(filter(lambda x: x % 2 != 0, numeros))
    
def main():
    """
    Función principal para generar números aleatorios y filtrar impares.
    """
    lista_random = num_random()
    impares = num_impares(lista_random)
    
    print(f"Números aleatorios: {lista_random}\n")
    
    print(f"Números impares: {impares}")

if __name__ == "__main__":
    main()
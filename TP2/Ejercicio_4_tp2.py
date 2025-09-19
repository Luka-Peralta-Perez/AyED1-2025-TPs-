"""
    4. Eliminar de una lista de números enteros aquellos valores que se encuentren en
    una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
    resultante. La función debe modificar la lista original sin crear una copia modificada.
"""

from random import randint
from typing import List

def eliminar(lista_original: List[int], lista_eliminar: List[int])-> None:
    """
    Elimina los elementos de lista_eliminar de lista_original.

    Pre:
        - lista_original: Lista de números enteros donde se realizarán las eliminaciones.
        - lista_eliminar: Lista de números enteros que se desean eliminar de lista_original.

    Post:
        - lista_original se modifica directamente para eliminar los elementos que estén en lista_eliminar.
    """
    for elemento in lista_eliminar:
        while elemento in lista_original:
            lista_original.remove(elemento)

def main():
    """
    Programa principal que genera dos listas y llama a la función de eliminación.
    
    Post:
        - Imprime la lista original, la lista de elementos a eliminar y la lista resultante.
    """
    lista_original = [randint(1, 100) for _ in range(10)]
    lista_eliminar = [randint(1, 100) for _ in range(5)]
    
    print(f"La lista original: {lista_original}")
    print(f"Lista de valores que se deben eliminar: {lista_eliminar}")
    
    eliminar(lista_original, lista_eliminar)
    
    print(f"Lista resultante: {lista_original}")

    
if __name__ == "__main__":
    main()
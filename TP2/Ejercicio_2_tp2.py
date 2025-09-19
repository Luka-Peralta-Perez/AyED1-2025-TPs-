"""
    2. Escribir funciones para:
    a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
    a través del teclado.
    
    b. Recibir una lista como parámetro y devolver True si la misma contiene algún
    elemento repetido. La función no debe modificar la lista.
    
    c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
    únicos de la lista original, sin importar el orden.
    Combinar estas tres funciones en un mismo programa.
    
"""
from typing import List
from random import randint

def generar_lista(n: int) -> List[int]:
    
    """
    Genera una lista de N números aleatorios del 1 al 100.

    Pre:
    - n (int): Número de elementos a generar. Debe ser un entero positivo.

    Post:
    - Retorna una lista de números aleatorios entre 1 y 100 si n es positivo;
      de lo contrario, retorna una lista vacía.
    """
    if n <= 0:
        print("ERROR, debe ser un número entero positivo.")
        return []
    lista = [randint(1, 100) for _ in range(n)]
    return lista

def num_repetido(lista: List[int]) -> bool:
    """
    Verifica si la lista contiene elementos repetidos.

    Pre:
    - lista (List[int]): Lista de números enteros.

    Post:
    - Retorna True si hay elementos repetidos, False en caso contrario.
    """
    return len(lista) != len(set(lista))

def lista_unicos(lista: List[int]) -> List[int]:
    """
    Devuelve una nueva lista con los elementos únicos de la lista original.

    Pre:
    - lista (List[int]): Lista de números enteros.

    Post:
    - Retorna una lista con elementos únicos sin importar el orden.
    """
    return list(set(lista))
    
def main()-> None:
    """
    programa principal
    
    """
    try:
        n = int(input("Ingrese un número positivo: "))
    except ValueError:
        print("ERROR: Debe ingresar un número entero válido.")
        return
    
    lista = generar_lista(n)
    
    if not lista:
        return
    print(f"Lista generada: {lista}")
    
    if num_repetido(lista):
        print("La lista contiene elementos repetidos")
    else:
        print("La lista no contiene elementos repetidos")
    
    unicos = lista_unicos(lista)
    print(f"Lista de elementos unicos: {unicos}")
    
if __name__ == "__main__":
    main()
    
    

     
     
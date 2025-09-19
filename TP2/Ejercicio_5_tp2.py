"""
    5. Escribir una función que reciba una lista como parámetro y devuelva True si la lista
    está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
    ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
    además un programa para verificar el comportamiento de la función. 
"""

from typing import List

def lista_ordenada(lista: List[int])-> bool:
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

def main()-> None:
    
    print(lista_ordenada(lista))
    return None
    
lista = [47, 9, 99, 99, 75, 80, 55, 52, 14, 35]

if __name__ == "__main__":
    main()
    
    
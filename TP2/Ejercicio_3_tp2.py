"""
    3. Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
    donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. 

"""
from typing import List

def generar_lista(n: int) -> List[int]:
    """
    Pre:
        - n >= 0 (la entrada debe ser un número entero no negativo)
    Post:
        - Devuelve una lista de cuadrados de números desde 1 hasta n (inclusive)
    """
    if n < 0:
        print("ERROR, debe ser un numero entero positivo.")
        return []
    
    lista = [i**2 for i in range(1, n + 1)]
    return lista

def mostrar_valores(lista: List[int]) -> None:
    """
    Pre:
        - Lista debe ser una lista no vacia de numeros enteros
    Post:
        - Muestra por pantalla los ultimos 10 valores de la lista (o la lista completa si tiene menos de 10 elementos)
    """
    
    if len(lista) >= 10:
        print(f"Los ultimos 10 valores de la lista son: {lista[-10:]}")
    else:
        print(f"La lista cuenta con menos de 10 elementos: {lista}")
    
def main() -> None:
    """
    Funcion principal
    """
    try:
        usuario = int(input("Ingrese un numero positivo: "))
        lista = generar_lista(usuario)
        
        if not lista:
            return
        
        mostrar_valores(lista)
    except ValueError:
        print("ERROR: Ingrese un numero entero valido.")
        
if __name__ == "__main__":
    main()
    

    
"""
    1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
    
    a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.

    b. Calcular y devolver el producto de todos los elementos de la lista anterior.

    c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
    se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
    listas auxiliares.
    
    d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
    auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]
"""
from random import randint
from typing import List

def lista_a()-> List[int]:
    """
    Genera una lista con números al azar de cuatro dígitos.
    La cantidad de elementos también es un número al azar de dos dígitos.

    Pre:
        - No recibe parámetros.

    Post:
        - Devuelve una lista de int.
        - Todos los elementos están en el rango [1000, 9999].
        - La longitud de la lista está en el rango [10, 99].
    """
    
    numero_random = [randint(1000, 9999) for _ in range(randint(10, 99))]
    return numero_random

def lista_b(lista: List[int])-> int:
    """
    Calcula el producto de todos los elementos de la lista.

    Pre:
        - lista (List[int]): lista no vacía de enteros.

    Post:
        - Devuelve el producto de todos sus elementos.
    """
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

def lista_c(lista: List[int], valor: int)-> List[int]:
    """
    Elimina **todas** las apariciones de `valor` en la lista **in-place**.
    No utiliza listas auxiliares.

    Pre:
        - lista (List[int]): lista modificable.
        - valor (int): valor a eliminar.

    Post:
        - La misma lista **sin** el valor eliminado.
        - Si el valor no existía, la lista queda igual.
    """
    while valor in lista:
        lista.remove(valor)
    return lista

def es_capicua(lista: List[int])-> bool:
    """
    Determina si la lista es capicúa (palíndrome).

    Pre:
        - lista (List[int]): lista de enteros.

    Post:
        - Devuelve True si la lista es igual a su inversa.
        - No usa listas auxiliares.
    """
    return lista == lista[::-1]

def main()-> None:
    """
    Programa principal que prueba las funciones anteriores.
    
    """
    lista_original = lista_a()
    print(f"Lista cargada {lista_original}\n")
    
    producto = lista_b(lista_original)
    print(f"el Producto de todos los elementos de la lista es de: {producto}\n")
    
    eliminar_valor = int(input("Ingrese el valor que desea eliminar: "))
    lista_actualizada = lista_c(lista_original, eliminar_valor)
    print(f"\nResultado de la lista con los valores ingresados eliminados {lista_actualizada}")
    
    print(f"La lista {lista_actualizada}, es capicua? {es_capicua(lista_actualizada)}")
    
if __name__ == "__main__":
    main()
    
    
    



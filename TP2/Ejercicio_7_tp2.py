"""
    7. Intercalar los elementos de una lista entre los elementos de otra. La intercalación
    deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
    una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
    y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
    tener distintas longitudes.
"""

from typing import List

def intercalar(lista1: List[int], lista2: List[int]) -> None:
    """
    Intercala los elementos de lista2 en lista1 usando rebanadas.

    Pre:
        - lista1 y lista2 son listas de enteros.
    Post:
        - lista1 queda modificada con los elementos de lista2 intercalados.
        - Si lista2 es más larga, los elementos sobrantes se agregan al final de lista1.
    """
    long_min = min(len(lista1), len(lista2))
    
    for i in range(long_min):
        lista1[2 * i + 1:2 * i + 1] = [lista2[i]]
        
    if len(lista2) > long_min:
        lista1.extend(lista2[long_min:])


def main() -> None:
    lista1 = [29, 64, 28, 50, 90, 20, 18, 31, 83, 56]
    lista2 = [64, 50, 18, 20, 83, 56, 90, 28, 29, 31]
    intercalar(lista1, lista2)
    print("Lista intercalada:", lista1)


if __name__ == "__main__":
    main()
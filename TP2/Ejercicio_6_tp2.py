from typing import List


def normalizar_numeros(lista: List[int]) -> List[float]:
    """
    Normaliza una lista de enteros para que sus elementos sumen 1.0,
    respetando las proporciones originales.

    Pre:
        - lista: secuencia de enteros (no vacía, no todos ceros)
    Post:
        - Lista de floats cuya suma es 1.0 (con posible pérdida de precisión)
    """
    total = sum(lista)
    if total == 0:
        raise ValueError("La suma de la lista no puede ser cero.")
    return [x / total for x in lista]


def main() -> None:
    lista: List[int] = [9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
    print("Lista original:", lista)
    print("Lista normalizada:", normalizar_numeros(lista))
    print("Suma de normalizados:", sum(normalizar_numeros(lista)))


if __name__ == "__main__":
    main()
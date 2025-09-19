""""
    8. Utilizar la técnica de listas por comprensión para construir una lista con todos los
    números impares comprendidos entre 100 y 200.
"""
from typing import List

def impares() -> List[int]:
    """
    Genera una lista de números impares entre 100 y 200 (ambos incluidos).

    Pre:
        - Ninguna

    Post:
        - Retorna una lista con todos los números impares entre 100 y 200.
    """
    return [x for x in range(101, 201) if x % 2 != 0]

def main() -> None:
    """Función principal"""
    lista_impares = impares()
    print(lista_impares)

if __name__ == "__main__":
    main()

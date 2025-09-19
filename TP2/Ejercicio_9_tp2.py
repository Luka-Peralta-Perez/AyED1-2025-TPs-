"""
    9. Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
    que no sean múltiplos de 5. A y B se ingresar desde el teclado. 
"""
from typing import List


def multiplos(a: int, b: int) -> List[int]:
    """
    Devuelve los múltiplos de 7 que no sean múltiplos de 5
    en el intervalo abierto (a, b).

    Pre:
        a < b
    Post:
        Lista de enteros que cumplen:
            x % 7 == 0 y x % 5 != 0, con a < x < b
    """
    return [x for x in range(a + 1, b) if x % 7 == 0 and x % 5 != 0]


def main() -> None:
    """
    Solicita dos enteros y muestra los múltiplos solicitados.
    """
    try:
        a = int(input("Ingrese el extremo A: "))
        b = int(input("Ingrese el extremo B: "))

        if a >= b:
            print("ERROR: A debe ser menor que B.")
            return

        resultado = multiplos(a, b)
        print(f"Múltiplos de 7 que no son múltiplos de 5 entre {a} y {b}:")
        print(resultado)

    except ValueError:
        print("ERROR: ingrese números enteros válidos.")


if __name__ == "__main__":
    main()
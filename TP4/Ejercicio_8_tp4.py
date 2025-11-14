"""
8. Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""

def devolver_cadena(cadena: str, n: int) -> str:
    """
    Devuelve los últimos N caracteres de la cadena dada.

    Pre:
        - cadena (str): La cadena de la cual se extraerán los últimos caracteres.
        - n (int): La cantidad de caracteres a devolver.

    Post:
        - str: La subcadena que contiene los últimos N caracteres.
    """
    if n < 0:
        raise ValueError("El valor de N debe ser un número entero no negativo.")
    return cadena[-n:]

def main() -> None:
    """
    Función principal para verificar el comportamiento de la función devolver_cadena.

    Pre:
        - none

    Post:
        - Verifica el comportamiento de la función devolver_cadena.
    """
    cadena = input("Ingrese la cadena de caracteres: ")
    
    try:
        n = int(input("Ingrese la cantidad de últimos caracteres a devolver: "))
        
        if n < 0:
            raise ValueError("El valor de N debe ser un número entero no negativo.")
        
        print("Cadena original:", cadena)
        print("Últimos", n, "caracteres:", devolver_cadena(cadena, n))
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
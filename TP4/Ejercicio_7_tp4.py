"""
    7. Escribir una función para eliminar una subcadena de una cadena de caracteres,
    a partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante.
    Escribir también un programa para verificar el comportamiento de la misma.
    Escribir una función para cada uno de los siguientes casos:

    a. Utilizando rebanadas
    
    b. Sin utilizar rebanadas
"""

def eliminar_x_rebanadas(cadena: str, inicio: int, longitud: int) -> str:
    """
    Elimina una subcadena utilizando rebanadas.

    Pre:
        - cadena (str): La cadena de caracteres original.
        - inicio (int): Posición de inicio para eliminar la subcadena.
        - longitud (int): Cantidad de caracteres a eliminar.

    Post:
        - str: La cadena resultante después de eliminar la subcadena.
    """
    return cadena[:inicio] + cadena[inicio + longitud:]

def eliminar_sin_rebanadas(cadena: str, inicio: int, longitud: int) -> str:
    """
    Elimina una subcadena sin utilizar rebanadas.

    Pre:
        - cadena (str): La cadena de caracteres original.
        - inicio (int): Posición de inicio para eliminar la subcadena.
        - longitud (int): Cantidad de caracteres a eliminar.

    Post:
        - str: La cadena resultante después de eliminar la subcadena.
    """
    resultado = ""
    for i in range(len(cadena)):
        if i < inicio or i >= inicio + longitud:
            resultado += cadena[i]
    return resultado

def main() -> None:
    """
    Función principal para verificar el comportamiento de las funciones de eliminación de subcadenas.

    Pre:
        - none

    Post:
        - Verifica el comportamiento de las funciones eliminar_x_rebanadas y eliminar_sin_rebanadas.
    """
    cadena = input("Ingrese la cadena de caracteres: ")
    
    try:
        posicion = int(input("Ingrese la posición de inicio: "))
        cantidad = int(input("Ingrese la cantidad de caracteres a eliminar: "))
        
        if posicion < 0 or cantidad < 0:
            raise ValueError("La posición y la cantidad deben ser números enteros no negativos.")
        
        print("Cadena original:", cadena)
        print("Cadena resultante después de eliminar la subcadena:")
        print("Usando rebanadas:", eliminar_x_rebanadas(cadena, posicion, cantidad))
        print("Sin usar rebanadas:", eliminar_sin_rebanadas(cadena, posicion, cantidad))
    
    except ValueError as e:
        print(f"Error: {e}")
    except IndexError:
        print("Error: La posición de inicio y/o la cantidad exceden la longitud de la cadena.")

if __name__ == "__main__":
    main()
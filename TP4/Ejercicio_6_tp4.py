"""
6. Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma.
Ejemplo, dada la cadena "El número de teléfono es 4356-7890"
extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:

a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""

def extraer_x_rebanadas(cadena: str, inicio: int, longitud: int) -> str:
    """
    Extrae una subcadena utilizando rebanadas.

    Pre:
        - cadena (str): La cadena de caracteres original.
        - inicio (int): Posición de inicio para extraer la subcadena.
        - longitud (int): Cantidad de caracteres a extraer.

    Post:
        - str: La subcadena extraída.
    """
    return cadena[inicio:inicio + longitud]

def extraer_sin_rebanadas(cadena: str, inicio: int, longitud: int) -> str:
    """
    Extrae una subcadena sin utilizar rebanadas.

    Pre:
        - cadena (str): La cadena de caracteres original.
        - inicio (int): Posición de inicio para extraer la subcadena.
        - longitud (int): Cantidad de caracteres a extraer.

    Post:
        - str: La subcadena extraída.
    """
    subcadena = ""
    for i in range(inicio, inicio + longitud):
        subcadena += cadena[i]
    return subcadena

def main() -> None:
    """
    Función principal para verificar el comportamiento de las funciones de extracción de subcadenas.

    """
    cadena = input("Ingrese la cadena de caracteres: ")
    
    try:
        posicion = int(input("Ingrese la posición de inicio: "))
        cantidad = int(input("Ingrese la cantidad de caracteres a extraer: "))
        
        if posicion < 0 or cantidad < 0:
            raise ValueError("La posición y la cantidad deben ser números enteros no negativos.")
        
        print("Cadena original:", cadena)
        print("Subcadena que comienza en la posición", posicion, "y tiene", cantidad, "caracteres:")
        print("Usando rebanadas:", extraer_x_rebanadas(cadena, posicion, cantidad))
        print("Sin usar rebanadas:", extraer_sin_rebanadas(cadena, posicion, cantidad))
    
    except ValueError as e:
        print(f"Error: {e}")
    except IndexError:
        print("Error: La posición de inicio y/o la cantidad exceden la longitud de la cadena.")

if __name__ == "__main__":
    main()
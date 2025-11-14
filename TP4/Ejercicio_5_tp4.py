"""
    5. Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N,
    y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original.
    Escribir también un programa para verificar el comportamiento de la misma.
    Hacer tres versiones de la función, para cada uno de los siguientes casos:
    
    a. Utilizando sólo ciclos normales
    
    b. Utilizando listas por comprensión
    
    c. Utilizando la función filter

"""
def filtrar_palabras(cadena: str, n: int):
    """
    Filtra las palabras de una cadena que tienen N o más caracteres utilizando ciclos normales.

    Pre:
        - cadena (str): La cadena de caracteres que contiene la frase.
        - n (int): Número mínimo de caracteres que debe tener cada palabra.

    Post:
        - str: Cadena con las palabras filtradas que tienen N o más caracteres.
    """
    palabras = cadena.split()
    palabras_filtradas = []
    
    for palabra in palabras:
        if len(palabra) >= n:
            palabras_filtradas.append(palabra)
            
    return ' '.join(palabras_filtradas)  

def filtrar_x_compresion(cadena: str, n: int) -> str:
    """
    Filtra las palabras de una cadena que tienen N o más caracteres utilizando listas por compresion.

    Pre:
        - cadena (str): La cadena de caracteres que contiene la frase.
        - n (int): Número mínimo de caracteres que debe tener cada palabra.

    Post:
        - str: Cadena con las palabras filtradas que tienen N o más caracteres.
    """
    return ' '.join([palabra for palabra in cadena.split() if len(palabra) >=n])

def filtra_x_filter(cadena: str, n: int) -> str:
    """
    Filtra las palabras de una cadena que tienen N o más caracteres utilizando la función filter.

    Pre:
        - cadena (str): La cadena de caracteres que contiene la frase.
        - n (int): Número mínimo de caracteres que debe tener cada palabra.

    Post:
        - str: Cadena con las palabras filtradas que tienen N o más caracteres.
    """
    
    return ' '.join(filter(lambda palabra: len(palabra) >= n, cadena.split()))

def main()-> None:
    """
    Funcion principal del programa.
    """
    try:
        cadena = input("Ingrese la cadena de caracteres o frase : ")
        n = int(input("Ingrese el numero minimo de caracteres: "))
        
        print("\nResultados:\n")
        print(f"Usando ciclos normales: {filtrar_palabras(cadena, n)}")
        
        print(f"\nUsando listas por compresion: {filtrar_x_compresion(cadena, n)}")
        
        print(f"\nUsando filter: {filtra_x_filter(cadena, n)}")
        
    except ValueError:
        print("ERROR: Ingrese N debe ser un numero entero positivo")
        
if __name__ == "__main__":
    main()
        
        
        
        
        
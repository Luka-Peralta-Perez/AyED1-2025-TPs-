"""
    11.Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro 
    de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los 
    caracteres de la subcadena no necesariamente deben estar en forma consecutiva 
    dentro de la cadena, pero sí respetando el orden de los mismos.
"""

def contar_cadena(cadena: str, sub_cadena: str) -> str:
    
    cadena = cadena.lower()
    
    subcadena = sub_cadena.lower()
    
    apariciones = 0
    
    indice = 0
    
    for palabra in cadena:
        if palabra == subcadena[indice]:
            indice += 1
            if indice == len(subcadena):
                apariciones += 1
                indice = 0
            
    return apariciones

def main() -> None:
    """
    Funcion principal, donde se prueba el programa
    
    """
    try:
        # Solicitar al usuario que ingrese las cadenas
        cadena = input("Ingrese la cadena principal: ")
        subcadena = input("Ingrese la subcadena a buscar: ")
        
        # Validar que ambas entradas no estén vacías
        if not cadena.strip():
            raise ValueError("La cadena principal no puede estar vacía.")
        
        if not subcadena.strip():
            raise ValueError("La subcadena no puede estar vacía.")
        
        # Llamar a la función y obtener el resultado
        resultado = contar_cadena(cadena, subcadena)
        print(f"\nLa subcadena '{subcadena}' se encuentra {resultado} veces en la cadena.")
    
    except ValueError as ve:
        # Capturar errores específicos de validación
        print(f"Error: {ve}")
    
    except Exception as e:
        # Capturar cualquier otro error inesperado
        print(f"Ha ocurrido un error inesperado: {e}")
if __name__ == "__main__":
    main()

 
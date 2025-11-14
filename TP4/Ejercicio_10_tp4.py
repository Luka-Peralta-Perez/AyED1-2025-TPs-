"""
    10.Desarrollar una función para reemplazar todas las apariciones de una palabra por 
    otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la 
    cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse 
    palabras completas, y no fragmentos de palabras. Escribir también un programa 
    para verificar el comportamiento de la función. 
"""

def cambiar_palabra(cadena: str, palabra_original: str, palabra_nueva: str) -> str:
    """
    Reemplaza todas las apariciones de una palabra por otra en una cadena de caracteres.
        
    Precondiciones:
        - `cadena` debe ser una cadena de caracteres.
        - `palabra_original` debe ser una cadena de caracteres que se busca en `cadena`.
        - `palabra_nueva` debe ser una cadena de caracteres que reemplazará a `palabra_original`.
    
    Postcondiciones:
        - La cadena resultante contiene todas las apariciones de `palabra_original` reemplazadas por `palabra_nueva`.
        - El contador de reemplazos indica cuántas veces se realizó el reemplazo.
    """
    palabras = cadena.split()
    
    reemplazos = 0
    
    palabras_modificadas = []
    
    for palabra in palabras:
        if palabra == palabra_original:
            palabras_modificadas.append(palabra_nueva)
            reemplazos +=1
        else:
            palabras_modificadas.append(palabra)
            
    resultado = ""
    for palabra in palabras_modificadas:
        resultado += palabra + " "
        
    return resultado, reemplazos

def main() -> None:
    """
    Funcion principal del programa, no retorna nada 
    """
    cadena = "el cielo es verde"
    palabra_original = "verde"
    palabra_nueva = "azul"
    
    resultado, reemplazos = cambiar_palabra(cadena, palabra_original, palabra_nueva)
    
    print(f"La cadena original era: {cadena}")
    print(f"La nueva cadena es: {resultado}")
    print(f"Cantidad de reemplazos realizados: {reemplazos}")

if __name__ == "__main__":
    main()
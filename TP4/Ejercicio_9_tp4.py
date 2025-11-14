"""
    9. Escribir una función que reciba como parámetro una cadena de caracteres en la que 
    las palabras se encuentran separadas por uno o más espacios. Devolver otra 
    cadena con las palabras ordenadas según su longitud, dejando un espacio entre 
    cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la 
    longitud de las palabras, pero deberán conservarse en la cadena final.
"""

def limpiar_y_obtener_longitud(palabra: str) -> str:
    """
    Elimina los signos de puntuación de la palabra y devuelve la palabra limpia y su longitud.
    
    Precondiciones:
        - `palabra` debe ser una cadena de texto (str).
    
    Postcondiciones:
        - Devuelve una tupla que contiene:
        - La palabra limpia (sin signos de puntuación).
        - La longitud de la palabra limpia (int).
    """
    
    # Lista de signos de puntuación
    signos_puntuacion = '.,;:!?()[]{}"\''  
    # Eliminar los signos de puntuación y contar la longitud
    palabra_limpia = ''.join(x for x in palabra if x not in signos_puntuacion)
    return palabra_limpia, len(palabra_limpia)

def ordenar_palabras(cadena: str) -> str:
    """
    Ordena las palabras de la cadena según su longitud, ignorando signos de puntuación.
    
    Precondiciones:
        - `cadena` debe ser una cadena de texto (str).
    
    Postcondiciones:
        - Devuelve una cadena de texto (str) que contiene las palabras ordenadas por longitud,
         separadas por un espacio.
    """
    
    palabras = cadena.split()
    
    palabras_limpias_y_longitudes = [limpiar_y_obtener_longitud(palabra) for palabra in palabras]
  
    palabras_ordenadas = sorted(palabras_limpias_y_longitudes, key=lambda x: x[1])

    resultado = " ".join(palabra[0] for palabra in palabras_ordenadas)
    
    return resultado

def main() -> None:
    """
    Función principal que solicita al usuario una cadena y muestra las palabras ordenadas por longitud.
    
    Precondiciones:
        - No hay precondiciones específicas, ya que esta función interactúa con el usuario.
    
    Postcondiciones:
        - Si se ingresa una cadena válida, se imprime la cadena de palabras ordenadas por longitud.
        - Si no se ingresa ninguna palabra, se imprime un mensaje indicando que no se ingresó ninguna palabra.
        - Si ocurre un error, se imprime un mensaje de error.
    """
    try:
        cadena = input("Por favor, ingresa una cadena de texto: ").strip()  # Eliminar espacios al inicio y al final
        if cadena:  # Verificar que la cadena no esté vacía
            resultado = ordenar_palabras(cadena)
            print("Palabras ordenadas por longitud:")
            print(resultado)
        else:
            print("No se ingresó ninguna palabra.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        
if __name__ == "__main__":
    main()


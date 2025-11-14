def centrar_cadena(cadena: str) -> str:
    """
    Centra una cadena de caracteres en un ancho de 80 columnas.

    Pre:
        cadena (str): La cadena que se desea centrar.
    
    Post:
        Devuelve la cadena centrada con espacios adicionales a la izquierda y derecha.
    """
    columnas = 80
    longitud = len(cadena)
    espacios = (columnas - longitud) // 2
    return ' ' * espacios + cadena

def main() -> None:
    """
    Función principal del programa.
    
    Post:
        Permite al usuario ingresar una cadena y verla centrada en pantalla.
    """
    try:
        cadena = input("Ingrese una cadena de caracteres: ")
        cadena_centrada = centrar_cadena(cadena)
        print(cadena_centrada)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()
def es_capicua(cadena: str) -> bool:
    """
    Determina si una cadena de caracteres es capicúa usando listas de comprensión.
    
    Pre:
        cadena (str): Cadena de caracteres a verificar.
    
    Post:
        bool: Devuelve True si la cadena es capicúa, False en caso contrario.
    """
    return all(cadena[i] == cadena[-i-1] for i in range(len(cadena) // 2))


def main() -> None:
    """
    Función principal del programa.
    
    """
    while True:
        try:
            cadena = input("Ingrese una cadena de caracteres (o 'salir' para finalizar): ")
            if cadena.lower() == 'salir':
                print("Saliendo...")
                break
            if es_capicua(cadena):
                print(f"La cadena '{cadena}' es capicúa.")
            else:
                print(f"La cadena '{cadena}' no es capicúa.")
        except Exception as e:
            print(f"Se produjo un error: {e}")

if __name__ == "__main__":
    main()
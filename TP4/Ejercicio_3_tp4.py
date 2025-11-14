"""
    3. Los números de claves de dos cajas fuertes están intercalados dentro de un número
    entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
    para obtener ambas claves, donde la primera se construye con los dígitos ubicados
    en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
    posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave
    maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.
"""

def obtener_claves(clave_maestra: str) -> tuple:
    """
    Obtiene las dos claves a partir de la clave maestra.

    Pre:
        - clave_maestra (str): La clave maestra como una cadena de caracteres.

    Post:
        - tuple: Una tupla con las dos claves (clave1, clave2).
    """
    clave1 = []
    clave2 = []
    for i in range(len(clave_maestra)):
        if i % 2 == 0:
            clave1.append(clave_maestra[i])
        else:
            clave2.append(clave_maestra[i])
    
    return ''.join(clave1), ''.join(clave2)


def main() -> None:
    """
    Función principal que ejecuta las demás funciones.
    """
    clave_maestra = input("Ingrese la clave maestra: ")

    # Validación de entrada
    if not clave_maestra.isdigit():
        print("Por favor, ingrese solo dígitos.")
        return

    clave1, clave2 = obtener_claves(clave_maestra)
    print(f"Clave 1: {clave1}")
    print(f"Clave 2: {clave2}")
    
    
if __name__ == "__main__":
    main()


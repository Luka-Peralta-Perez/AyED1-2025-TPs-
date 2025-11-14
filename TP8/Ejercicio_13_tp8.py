"""
    13.Escribir una función buscarclave() que reciba como parámetros un diccionario y un 
    valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el
    diccionario. Comprobar el comportamiento de la función mediante un programa apro
    piado.   
"""

def buscar_clave(diccionario: dict, valor: int)-> list:
    """
    Busca las claves en un diccionario que correspondan al valor especificado.
    
    Pre:
        - `diccionario` debe ser un diccionario válido con claves y valores.
        - `valor` debe ser un valor compatible con los valores del diccionario.
    
    Post:
        Devuelve una lista con todas las claves del diccionario que tienen asignado el valor especificado.
    """
    return [clave for clave, val in diccionario.items() if val == valor]

def validar_valor(cadena: str) -> int:
    """
    Valida que el usuario ingrese un número entero. Si no lo hace, solicita el ingreso nuevamente.
    
    Pre:
        - `cadena` debe ser una cadena que se muestra como mensaje al usuario.
    
    Post:
        Devuelve un valor entero ingresado por el usuario.
    """
    
    try:
        valor = int(input(cadena))
        return valor
    except ValueError:
        print("ERRROR: Ingrese un valor valido.")
        return validar_valor(cadena)

def main() -> None:
    """
    Función principal del programa que prueba la función buscar_clave().
    
    Pre:
        No requiere parámetros de entrada.
    
    Post:
        Imprime las claves correspondientes al valor ingresado en el diccionario.
    """
    # diccionario de ejemplo
    diccionario = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 2,
        'e': 1,
        'f': 4,
        'g': 2
    }
    
  
    print("\nDiccionario actual:")
    for clave, valor in diccionario.items():
        print(f"Clave: {clave} -> Valor: {valor}")
    
    print("\nBúsqueda de claves por valor")
    valor_buscar = validar_valor("Ingrese el valor a buscar: ")
    
    # Buscar las claves que mapean al valor
    claves_encontradas = buscar_clave(diccionario, valor_buscar)
    
    # Mostrar resultados
    if claves_encontradas:
        print(f"\nLas claves que mapean al valor {valor_buscar} son: {claves_encontradas}")
    else:
        print(f"\nNo se encontraron claves que mapeen al valor {valor_buscar}")

if __name__ == "__main__":
    main()
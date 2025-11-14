"""
    8. Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 
    20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves. 
"""

def generar_diccionario()-> dict:
    """
    Genera un diccionario donde las claves van del numero 1 al 20 y los valores son sus cuadrados/
    
    Pre:
        La funcion no tiene parametros
    Post:
        - Devuelve un diccionario {numero: cuadrado}
    """
    return  {i: i ** 2 for i in range(1, 21)}

def main() -> None:
    """
    Funcion principal donde se prueba el programa.
    """
    diccionario = generar_diccionario()
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")

if __name__ == "__main__":
    main()
    
"""
    4. Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
    lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
    qué cambiaría la función si el rango de valores fuese diferente?
"""

def num_romanos(usuario: int) -> str:
    """
    Convierte un número entero en su representación romana.

    Pre:
        - usuario (int): Debe ser un número entero entre 0 y 3999.

    Post:
        - str: La representación en números romanos del número dado.
    """
    
    if usuario < 0 or usuario > 3999:
        raise ValueError("El numero debe estar entre 0 y 3999")
    val_romanos =  [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    
    romanos = []
    
    for valor, simbolo in val_romanos:
        while usuario >= valor:
            romanos.append(simbolo)
            usuario -= valor
    return ''.join(romanos)

def main()-> None:
    """
    Funcion principal 
    """
    try:
        usuario = int(input("Ingrese un numero entre 0 y 3999: "))
        romano = num_romanos(usuario)
        print(f"El numero {usuario} en romano es: {romano}")
    except ValueError as e:
        print(e)
        
if __name__ == "__main__":
    main()
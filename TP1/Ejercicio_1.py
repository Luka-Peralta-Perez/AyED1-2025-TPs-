""""
        1. Desarrollar una función que reciba tres números enteros positivos y devuelva el
        mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
        caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
        también un programa para ingresar los tres valores, invocar a la función y mostrar
        el máximo hallado, o un mensaje informativo si éste no existe.
        
"""

def mayor_estricto(a: int, b: int, c: int) -> int:
    """
    busca el mayor estricto de los tres números ingresados:

    Pre:
        a (int): número A
        b (int): número B
        c (int): número C

    Post:
         int: Devuelve el mayor estricto o -1 si no existe.
    """
    
    maximo = a
    
    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c
    
    if maximo == a and maximo == b:
        return -1
    if maximo == a and maximo == c:
        return -1
    if maximo == c and maximo == b:
        return -1
    
    return maximo

def main() -> None:
    """"
    Funcion principal del programa, el usuario ingresa los números solicitados.
    """
    try:
        a = int(input("Ingrese un número entero para A: "))
    except ValueError:
        print("ERROR. 'A', no es un número entero")
        return
    try:
        b = int(input("Ingrese un número Entero para B: "))
    except ValueError:
        print("ERROR. 'B', no es un número entero.")
        return
    try:
        c = int(input("Ingrese un número entero para C: "))
    except ValueError:
        print("ERROR. 'C', no es un número entero.")

    if a < 1:
        print("ERROR, debe usar números enteros positivos")
        return
    if b < 1:
        print("ERROR, debe usar números enteros positivos")
        return
    if c < 1:
        print("ERROR, debe usar números enteros positivos")
        return

    resultado = mayor_estricto(a, b, c)
    if resultado == -1:
        print("No hay un mayor estricto.")
    else:
        print(f"El mayor estricto es {resultado}.")

if __name__ == "__main__":
    main()
"""
    9. Escribir un programa que permita ingresar un número entero N y genere un 
    diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la 
    tabla de multiplicar con el formato apropiado.
"""

def generar_tabla(numero: int) -> dict:
    """
    genera un diccionario donde crea una tabla de multiplicacion de un numero N del 1 al 12
    
    Pre:
        - El usuario debe ingresar el numero a multiplicar.
        
    Post:
        - Crea un diccionario representando la tabla de multiplicar del numero ingresado.
    """
    return {i: numero * i for i in range(1, 13)}

def main():
    """
    Funcion principal donde se prueba todo el programa. 
    """
    try:
        numero = int(input("Ingrese el numero a multiplicar: "))
        
        resultado = generar_tabla(numero)
        
        for clave, valor in resultado.items():
            print(f"{numero} x {clave} = {valor}")
    except ValueError:
        print("ERROR: ingrese un valor valido. ")

if __name__ == "__main__":
    main()
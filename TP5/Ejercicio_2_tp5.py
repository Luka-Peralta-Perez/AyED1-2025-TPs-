"""
    2. Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un
    número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
    utilizando manejo de excepciones para detectar el error.

"""

def validar_cadenas(cadena1: str, cadena2: str ) -> float :
    """
    Suma dos números representados como cadenas y devuelve el resultado como un número real.
    
    Precondición:
    
        - cadena1 y cadena2 deben ser cadenas de caracteres que representen números reales.
        
    Postcondición:
    
        - Si ambas cadenas contienen números reales válidos, devuelve la suma como un número real.
        
        - Si alguna cadena no es válida, devuelve -1.
    """
    
    try:
        str1 = float(cadena1)
        str2 = float(cadena2)
        return str1 + str2
    
    except ValueError:
        return -1

def main() -> None:
    """
    Función principal, donde se solicita al usuario que ingrese dos cadenas a sumar

    Esta función no recibe parámetros y no devuelve ningún valor.

    """
    cadena1 = input("Ingrese la primera cadena de numeros: ")
    cadena2 = input("Ingrese la segunda cadena de numeros: ")
    resultado = validar_cadenas(cadena1, cadena2)
    
    if resultado == -1:
        print("ERROR, alguno de los valores ingresados no es valido. ")
    else:
        print(f"El resultado de la suma es: {resultado}")

if __name__ == "__main__":
    main()
    
    
    
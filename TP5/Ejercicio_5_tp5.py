""""
    5. La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
    módulo math. Escribir un programa que utilice esta función para calcular la raíz
    cuadrada de un número cualquiera ingresado a través del teclado. El programa
    debe utilizar manejo de excepciones para evitar errores si se ingresa un número
    negativo.

"""
import math

def raiz(num: int) -> float:
    """
    Calcula la raíz cuadrada de un número positivo.

    Pre:
        num: Un número real mayor o igual a 0.
        
    Post:
        - Retorna la raíz cuadrada del número si es válido.
        
        - Lanza ValueError si el número es negativo.

    """
    
    if num < 0:
        raise ValueError("El número no puede ser negativo.")
    return math.sqrt(num)
   

def main()-> None:
    """
    Solicita un número al usuario y calcula su raíz cuadrada,
    manejando excepciones para entradas negativas o no válidas
    
    """
    try:
        usuario = float(input("Ingrese un número para calcular su raíz cuadrada: "))
        resultado = raiz(usuario)
        print(f"La raíz cuadrada de {usuario} es {resultado:.2f}")
    except ValueError as e:
        print(f"ERROR: {e}")
    except Exception as e:
        print(f"ERROR inesperado: {e}")

if __name__ == "__main__":
    main()
        

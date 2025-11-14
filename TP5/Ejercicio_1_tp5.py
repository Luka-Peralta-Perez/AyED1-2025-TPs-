    """
    1. Desarrollar una función para ingresar a través del teclado un número natural. La
    función rechazará cualquier ingreso inválido de datos utilizando excepciones y
    mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
    número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
    exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
    correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.
    """

def probar_numero() -> int:
    '''
    Solicita al usuario ingresar un número natural (>= 0) y lo valida.
    
    Precondición:
        - El usuario debe ingresar un valor que pueda ser convertido a un número entero.
        
        - El número ingresado debe ser mayor a 0.
        
    Postcondición:
        
        - Devuelve el número entero ingresado si es válido.
        
        - En caso de error, muestra el mensaje correspondiente y solicita un nuevo ingreso.
    '''
    try:
        num = int(input("Ingrese un numero: "))

        if num < 0:
            raise ValueError("El numero debe ser mayor a 0.")
        return num
    except ValueError as e:
        print(f"ERROR: {e} Pruebe de nuevo.")

def main() -> None:
    """
    Programa principal para probar la función `probar_numero`.
    
    Precondición:
        - El programa solicitará números naturales al usuario.
        
    Postcondición:
        - El programa imprime cada número válido ingresado.
        
        - Si el usuario ingresa 0, el programa finaliza mostrando un mensaje de despedida.
    
    """
    while True:
        numero = probar_numero()
        
        if numero == 0:  # Permite salir del bucle
            print("Gracias por usar el programa. Saliendo...")
            break
        print(f"El número ingresado es: {numero}")

    
if __name__ == "__main__":
    main()

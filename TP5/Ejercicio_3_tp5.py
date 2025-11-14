"""
    3. Desarrollar una función que devuelva una cadena de caracteres con el nombre del
    mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
    obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
    Devolver una cadena vacía si el número de mes es inválido. La detección de meses
    inválidos deberá realizarse a través de excepciones.
"""

def mes(numero: int)-> str:
    """
    Devuelve el nombre del mes correspondiente al número recibido como parámetro.
    
    Precondición:
    
        - numero: debe ser un entero.
        
    Postcondición:
    
        - Si el número está en el rango 1-12, devuelve el nombre del mes.
        
        - Si el número es inválido, devuelve una cadena vacía.
    """
    
    meses = {1: "Enero",
             2: "Febrero",
             3: "Marzo",
             4: "Abril",
             5: "Mayo",
             6: "Junio",
             7: "Julio",
             8: "Agosto",
             9: "Septiembre",
             10: "Octubre",
             11: "Noviembre",
             12: "Diciembre",}
    try:
        return meses[numero]
    
    except KeyError:
        return ""

def main()-> None:
    """
    Función principal, donde se le solicita al usuario un número de mes.

    Esta función no recibe parámetros y no devuelve ningún valor
    """
    while True:
        try:
            usuario = int(input("Ingrese un numero correspondiente a un mes (0 para salir): "))
            
            if usuario == 0:
                print("Gracias por utilizar el programa. Saliendo...")
                break
            
            nombre_mes = mes(usuario)    
            if nombre_mes:
                print(f"El mes correspondiente al número {usuario} es: {nombre_mes}.")
            else:
                print("Número de mes inválido.")
        except ValueError:
            print("ERROR: Debe ingresar un número entero.")

if __name__ == "__main__":
    main()
            
        
    

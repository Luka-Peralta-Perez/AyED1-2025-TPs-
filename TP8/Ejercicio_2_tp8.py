"""
    2. Escribir una función que reciba como parámetro una tupla conteniendo una fecha  (día,mes,año)
    y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido.
    La función debe contemplarse que el año se ingrese en dos  dígitos, los que serán interpretados según un año de corte definido dentro del 
    programa. Cualquier año mayor que éste se considerará del siglo pasado. Por 
    ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030" 
    para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de 
    1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en 
    cuenta. Escribir también un programa para ingresar los datos, invocar a la función y 
    mostrar el resultado
"""
from typing import Tuple

def bisiesto(anio):
    """  
    Un año es bisiesto si es divisible por 4, excepto si es divisible por 100,
    a menos que también sea divisible por 400.

    Pre:
    - 'anio' es un entero positivo.

    Post:
    - Devuelve 'True' si el año es bisiesto, de lo contrario, 'False'.
    
    """
    return anio % 4 == 0 and (anio % 100 !=0 or anio % 400 == 0)

def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si una fecha es válida.

    Pre:
        dia (int): día de la fecha
        mes (int): mes de la fecha
        anio (int): año de la fecha

    Post:
        bool: True si la fecha es válida, False en caso contrario
    """
    
    meses = [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
    if mes < 1 or mes > 12:
        return False
    if anio < 1:
        return False
    if mes == 2 and bisiesto(anio):
        return dia >= 1 and dia <= 29
    return dia >= 1 and dia <= meses[mes-1][1]
        
def ingresar_fecha():
    """
    Solicita al usuario ingresar una fecha y verifica que sea válida.

    Pre:
        - No requiere precondiciones ya que maneja las validaciones internamente

    Post:
        Retorna una tupla (dia, mes, año) con una fecha válida
    """
    while True:
        try:
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))
            
            if validar_fecha(dia, mes, anio):
                print(f"\nLa fecha {dia}/{mes}/{anio} es válida \n")
                return (dia, mes, anio)
            else:
                print(f" \nLa fecha {dia}/{mes}/{anio} es inválida \n")
        except ValueError:
            print("ERROR. Intenta de nuevo ingresando números enteros positivos.\n")

def fecha_extendida(fecha: Tuple, anio_corte: int= 30) -> str:
    dia, mes, anio = fecha
    
    meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo",
             6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre",
             11: "Noviembre", 12: "Diciembre"}
    
    if anio < 100:
        if anio > anio_corte:
            anio_completo = 1900 + anio
        else:
            anio_completo= 2000 + anio
    else:
        anio_completo = anio
        
    return f"{dia} de {meses[mes]} de {anio_completo}"

def main() -> None:
    """
    Función principal para ingresar la fecha y mostrar el resultado en formato extendido.
    """
    fecha = ingresar_fecha()  # Obtener la fecha válida del usuario
    resultado = fecha_extendida(fecha)  # Convertir a formato extendido
    print(f"La fecha en formato extendido es: '{resultado}'")  # Mostrar el resultado

if __name__ == "__main__":
    main()
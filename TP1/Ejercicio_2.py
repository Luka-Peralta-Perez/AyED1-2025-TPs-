"""
    2. Desarrollar una función que reciba tres números enteros positivos correspondientes
    al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
    tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
    Devolver True o False según la fecha sea correcta o no. Realizar también un
    programa para verificar el comportamiento de la función.
    
"""

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

def bisiesto(anio):
    """  
    Un año es bisiesto si es divisible por 4, excepto si es divisible por 100,
    a menos que también sea divisible por 400.

    Pre:
    - 'anio' es un entero positivo.

    Post:
    - Devuelve 'True' si el año es bisiesto, de lo contrario, 'False'.
    
    """
    return anio % 4 == 0 and (anio %100 !=0 or anio %400 == 0)

def main()-> None:
    while True:
        
        try:
            dia = int(input("Ingrese el Día (Ingrse 0 para salir): "))
            mes = int(input("Ingrese el Mes (Ingrse 0 para salir): "))
            anio = int(input("Ingrese el Año (Ingrse 0 para salir): "))
            
            if dia == 0 and mes == 0 and anio == 0:
                print("Saliendo...")
                break
            print(validar_fecha(dia, mes, anio))
            
            if validar_fecha(dia, mes, anio):
                print(f"\nLa fecha {dia}/{mes}/{anio} es válida \n")
            else:
                print(f" \nLa fecha {dia}/{mes}/{anio} es inválida \n")
        except ValueError:
            print("ERROR. Intenta de nuevo ingresando números enteros positivos.\n")
            
            
if __name__ == "__main__":
    main()
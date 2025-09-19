"""
    7. Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
    fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
    correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
    ni agregados, desarrollar programas que permitan:
    
    a. Sumar N días a una fecha.
    
    b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

"""
from typing import Tuple

def bisiesto(anio: int) -> bool:
    """  
    Un año es bisiesto si es divisible por 4, excepto si es divisible por 100,
    a menos que también sea divisible por 400.

    Pre:
    - 'anio' es un entero positivo.

    Post:
    - Devuelve 'True' si el año es bisiesto, de lo contrario, 'False'.
    
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

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
    
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes < 1 or mes > 12:
        return False
    if anio < 1:
        return False
    if mes == 2 and bisiesto(anio):
        return dia >= 1 and dia <= 29
    return dia >= 1 and dia <= meses[mes-1]

def dia_siguiente(dia: int, mes: int, anio: int) -> Tuple[int, int, int]:
    """
    Calcula la fecha del día siguiente.

    Pre:
        dia (int): día de la fecha
        mes (int): mes de la fecha
        anio (int): año de la fecha

    Post:
        Tuple[int, int, int]: la fecha del día siguiente (día, mes, año)
    """
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and bisiesto(anio):
        if dia < 29:
            return dia + 1, mes, anio
        else:
            return 1, 3, anio
    elif dia < meses[mes-1]:
        return dia + 1, mes, anio
    else:
        if mes < 12:
            return 1, mes + 1, anio
        else:
            return 1, 1, anio + 1

def sumar_dias(dia: int, mes: int, anio: int, n: int) -> Tuple[int, int, int]:
    fecha_actual = (dia, mes, anio)
    for _ in range(n):
        fecha_actual = dia_siguiente(*fecha_actual)
    return fecha_actual

def dias_entre_fechas(dia1: int, mes1: int, año1: int, dia2: int, mes2: int, año2: int) -> int:
    dias = 0
    fecha_actual = (dia1, mes1, año1)
    while fecha_actual != (dia2, mes2, año2):
        fecha_actual = dia_siguiente(*fecha_actual)
        dias += 1
    return dias

def main():
    try:
        print("Ingrese la fecha inicial (día, mes, año):")
        dia1 = int(input("Día: "))
        mes1 = int(input("Mes: "))
        anio1 = int(input("Año: "))
        
        if not validar_fecha(dia1, mes1, anio1):
            print("ERROR. La fecha inicial es inválida.")
            return
        
        print("Ingrese la fecha final (día, mes, año):")
        dia2 = int(input("Día: "))
        mes2 = int(input("Mes: "))
        anio2 = int(input("Año: "))
        
        if not validar_fecha(dia2, mes2, anio2):
            print("ERROR. La fecha final es inválida.")
            return
        
        if (anio2, mes2, dia2) < (anio1, mes1, dia1):
                print("ERROR. La fecha final es anterior a la fecha inicial.")
                return
        
        dias = dias_entre_fechas(dia1, mes1, anio1, dia2, mes2, anio2)
        
        print(f"La cantidad de días de diferencia entre las fechas es: {dias} días")
    
    except ValueError:
        print("ERROR. Los valor ingresados deben ser numero enteros positivos para todos los datos.")

if __name__ == "__main__":
    main()
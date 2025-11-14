"""
    1. Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
    
    a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha válida.
    
    b. Sumar N días a una fecha.
    
    c. Ingresar un horario desde teclado, verificando que sea correcto.
    
    d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al segundo se considerará que el primero corresponde al día anterior.
    En ningún caso la diferencia en horas puede superar las 24 horas.
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
    

def validar_hora(hora: int, minuto: int) -> bool:
    """
    Verifica si un horario es válido.

    Pre:
        hora (int): hora a validar
        minuto (int): minutos a validar

    Post:
        bool: True si el horario es válido, False en caso contrario
    """
    if hora < 0 or hora > 24:
        return False
    if minuto < 0 or minuto >= 60:
        return  False
    return True
        
def ingresar_hora():
    while True:
        try:
            hora = int(input("Ingrese la hora: "))
            minuto = int(input("Ingrese los minutos: "))
            
            print(validar_hora(hora, minuto))
            
            if validar_hora(hora, minuto):
                print(f"\nLa hora {hora}:{minuto} es válida.\n")
                return (hora, minuto)
            else:
                print(f"\nLa hora {hora}:{minuto} es inválida. Intente nuevamente.\n")
        except ValueError:
            print("ERROR. Intenta de nuevo ingresando números enteros positivos.\n")
            
def sumar_dia(fecha: tuple, n: int) -> tuple:
    
    dia, mes, anio = fecha
    
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Ajustar febrero si es un año bisiesto
    if bisiesto(anio):
        meses[1] = 29
    dia +=n
    
    while dia > meses[mes -1]:
        dia -= meses[mes -1]
        mes += 1
        # Si el mes supera 12, avanzar al siguiente año
        if mes > 12:
            mes = 1
            anio += 1
            
             # Verificar si el nuevo año es bisiesto
            if bisiesto(anio):
                meses[1] = 29
            else:
                meses[1] = 28

    return (dia, mes, anio)

def diferencia_horarios(hora1: tuple, hora2: tuple) -> tuple:
    """
    Calcula la diferencia entre dos horarios, considerando que si el primer horario
    es mayor al segundo, el segundo corresponde al día siguiente.
    
    Pre:
        hora1: tupla (hora, minutos) del primer horario
        hora2: tupla (hora, minutos) del segundo horario
    
    Post:
        tupla (horas, minutos) con la diferencia entre los horarios
    """
    
    h1_hora, h1_minutos = hora1
    
    h2_hora, h2_minutos = hora2
    
    minutos_1_totales = h1_hora * 60 + h1_minutos  # Convierto ambos horarios a minutos totales
    minutos_2_totales = h2_hora * 60 + h2_minutos
    
    if minutos_1_totales > minutos_2_totales:  # Si el primer horario es mayor, lo ajusto para tener en cuenta el día anterior
        minutos_2_totales += 24 * 60
    
    diferencia_minutos = minutos_2_totales - minutos_1_totales
    diferencia_horas = diferencia_minutos // 60
    diferencia_minutos %= 60
    
    return (diferencia_horas, diferencia_minutos)

def main():
    # Ingreso y validación de fecha
    print("Ingrese una fecha\n")
    fecha = ingresar_fecha()
    
    # Suma de días
    n = int(input("\nIngrese cantidad de días a sumar: "))
    nueva_fecha = sumar_dia(fecha, n)
    print(f"Nueva fecha después de sumar {n} días: {nueva_fecha[0]}/{nueva_fecha[1]}/{nueva_fecha[2]}")
    
    # Ingreso de horarios
    print("\nIngrese el primer horario\n ")
    hora1 = ingresar_hora()
    
    print("\nIngrese el segundo horario\n")
    hora2 = ingresar_hora()
    
    # Cálculo de diferencia
    dif_horas, dif_minutos = diferencia_horarios(hora1, hora2)
    print(f"La diferencia entre horarios es de: {dif_horas} horas y {dif_minutos} minutos")

if __name__ == "__main__":
    main()          
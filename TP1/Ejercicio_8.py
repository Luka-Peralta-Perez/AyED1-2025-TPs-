"""
    8. La siguiente función permite averiguar el día de la semana para una fecha determinada.
    La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc.
    Escribir un programa para imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
    y año cualquiera basándose en la función suministrada. Considerar que la semana
    comienza en domingo.
    
def diadelasemana(dia,mes,año):
     if mes < 3:
        mes = mes + 10
        año = año – 1
        
     else:
        mes = mes – 2
        siglo = año // 100
        año2 = año % 100
        diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
        if diasem < 0:
        diasem = diasem + 7
      return diasem

"""
def dia_de_semana(dia: int, mes: int, anio: int) -> int:
    """
    Calcula el día de la semana para una fecha dada.

    Pre:
        dia (int): día de la fecha, mayor que 0
        mes (int): mes de la fecha, 1-12
        anio (int): año de la fecha, > 0

    Post:
        Devuelve un entero 0-6 representando el día de la semana:
        0: Domingo, 1: Lunes, ..., 6: Sábado
    """
    if mes < 3:
        mes += 10
        anio -= 1
        
    else:
        mes -= 2

    siglo = anio // 100
    anio2 = anio % 100
    diasem = ((26 * mes - 2) // 10 + dia + anio2 + anio2 // 4 + siglo // 4 - 2 * siglo) % 7
    if diasem < 0:
        diasem += 7
    return diasem
    

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
        Devuelve True si la fecha es válida, False si es incorrecta.
    """
    if mes < 1 or mes > 12 or anio < 1 or dia < 1:
        return False

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and bisiesto(anio):
        dias_por_mes[1] = 29

    return dia <= dias_por_mes[mes - 1]


def imprimir_calendario(mes: int, anio: int) -> None:
    """
    Imprime el calendario completo de un mes y año determinado.

    Pre:
        mes (int): número del mes (1-12)
        anio (int): año positivo

    Post:
        Se imprime el calendario en pantalla.
    """
    dias_semana = [" Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]
    print("   ".join(dias_semana))

    primer_dia = dia_de_semana(1, mes, anio)

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and bisiesto(anio):
        dias_por_mes[1] = 29

    # Imprimir espacios antes del primer día
    print("    " * primer_dia, end= " ")

    for dia in range(1, dias_por_mes[mes - 1] + 1):
        print(f"{dia:4d}", end="  ")
        if (dia + primer_dia) % 7 == 0:
            print()
    print()
    
def main()-> None:
    try:
        mes = int(input("Ingrese el mes (1-12): "))
        anio = int(input("Ingrese el año: "))

        if not validar_fecha(1, mes, anio):
            print("Fecha inválida")
        else:
            imprimir_calendario(mes, anio)
    except ValueError:
        print("ERROR: Los numeros ingresados deben ser correspondientes a los meses del año.")

if __name__ == "__main__":
    main()
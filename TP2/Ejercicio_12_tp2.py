"""
    12.Resolver el siguiente problema, utilizando funciones: Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car
ga. Se solicita:
 a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe 
aparecer una sola vez en el informe.
 b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus 
ingresos. Mostrar los registros de entrada al club antes y después de 
eliminarlo. Informar cuántos ingresos se eliminaron
"""
from typing import List, Dict

def validar_numero_socio(numero_socio: int) -> bool:
    """
    Valida si el número de socio es un número entero de cinco dígitos.

    Pre:
        numero_socio (int): el número a validar
    Post:
        bool: True si es válido, False si es inválido.
    """
    return 10000 <= numero_socio <= 99999

def registrar_ingreso(numero_socio: int, registros: Dict[int, int]) -> None:
    """
    Registra el ingreso de un socio.

    Pre:
        numero_socio (int): el número de socio
        registros (Dict[int, int]): diccionario de registros de ingresos
    Post:
        None
    """
    if numero_socio in registros:
        registros[numero_socio] += 1
    else:
        registros[numero_socio] = 1

def mostrar_ingresos(registros: Dict[int, int]) -> None:
    """
    Muestra cuántas veces ingresó cada socio al club.

    Pre:
        registros (Dict[int, int]): diccionario de registros de ingresos
    Post:
        None
    """
    for socio, veces in registros.items():
        print(f"Socio {socio} ingresó {veces} veces.")

def eliminar_ingresos(numero_socio: int, registros: Dict[int, int]) -> int:
    """
    Elimina todos los ingresos de un socio dado de baja.

    Pre:
        numero_socio (int): el número de socio
        registros (Dict[int, int]): diccionario de registros de ingresos
    Post:
        int: número de ingresos eliminados
    """
    if numero_socio in registros:
        cantidad_eliminada = registros.pop(numero_socio)
        return cantidad_eliminada
    return 0

def main() -> None:
    """
    Función principal para registrar los ingresos de los socios.
    """
    registros = {}
    while True:
        try:
            numero_socio = int(input("Ingrese el número de socio (o 0 para terminar): "))
            if numero_socio == 0:
                break
            if validar_numero_socio(numero_socio):
                registrar_ingreso(numero_socio, registros)
            else:
                print("ERROR: El número de socio debe tener cinco dígitos.")
        except ValueError:
            print("ERROR: Debe ingresar un número entero.")

    print("\nRegistro de ingresos:")
    mostrar_ingresos(registros)

    try:
        socio_baja = int(input("\nIngrese el número de socio a dar de baja (o 0 para no eliminar): "))
        if socio_baja != 0:
            ingresos_eliminados = eliminar_ingresos(socio_baja, registros)
            print(f"Se eliminaron {ingresos_eliminados} ingresos del socio {socio_baja}.")
        else:
            print("No se eliminaron registros.")
    except ValueError:
        print("ERROR: Debe ingresar un número entero.")

    print("\nRegistro de ingresos después de la baja:")
    mostrar_ingresos(registros)

if __name__ == "__main__":
    main()
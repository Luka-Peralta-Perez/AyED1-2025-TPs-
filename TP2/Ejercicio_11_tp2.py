"""
    11. Resolver el siguiente problema, diseñando las funciones a utilizar:
    clínica necesita un programa para atender a sus pacientes. Cada paciente que
    ingresa se anuncia en la recepción indicando su número de afiliado (número entero
    de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
    turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
    se solicita:
    
        a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
            los pacientes atendidos por turno en el orden que llegaron a la clínica.
        
        b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
            atendido por turno y cuántas por urgencia. R


"""

def validar_numero_afiliado(numero_afiliado: int) -> bool:
    '''
    Valida si el número de afiliado es un número entero de cuatro dígitos.

    Pre:
        numero_afiliado (int): el número a validar.
    Post:
        true: el número es válido.
        false: el número es inválido.
    '''
    return 1000 <= numero_afiliado <= 9999

def validar_tipo_atencion(tipo_atencion: int) -> bool:
    '''
    Valida si el usuario ingresa urgencia o turno.

    Pre:
        tipo_atencion (int): 0 es urgencia, 1 es turno.
    Post:
        true: el número ingresado es válido.
        false: el número ingresado es inválido.
    '''
    return tipo_atencion in (0, 1)

def registrar_atencion(numero_afiliado: int, tipo_atencion: int) -> None:
    '''
    Se registran los pacientes atendidos por urgencia y por turno.

    Pre:
        numero_afiliado (int): el número de afiliado.
        tipo_atencion (int): urgencia (0) o turno (1).
    Post:
        Se actualizan las listas de urgencias y turnos.
    '''
    if tipo_atencion == 0:
        lista_urgencias.append(numero_afiliado)
    else:
        lista_turnos.append(numero_afiliado)

def buscar_atencion(numero_afiliado: int) -> str:
    '''
    Se busca un paciente y se informa cuántas veces se atendió por urgencia y cuántas veces por turno.

    Pre:
        numero_afiliado (int): número de afiliado del paciente.
    Post:
        str: veces que fue atendido por turno, veces que fue atendido por urgencia.
    '''
    cantidad_turnos = lista_turnos.count(numero_afiliado)
    cantidad_urgencias = lista_urgencias.count(numero_afiliado)
    return f"Atendido por turno: {cantidad_turnos} veces. Atendido por urgencia: {cantidad_urgencias} veces."

def mostrar_listados() -> None:
    '''
    Muestra los listados de pacientes atendidos por urgencia y por turno.
    '''
    print("Pacientes atendidos por urgencia:", lista_urgencias)
    print("Pacientes atendidos por turno:", lista_turnos)

def main() -> None:
    '''
    Función principal, donde el usuario ingresa el número de afiliado del paciente y si fue atendido por urgencia o por turno.
    '''
    while True:
        try:
            numero_afiliado = int(input("Número de afiliado (ingresar -1 para finalizar): "))
            if numero_afiliado == -1:
                break

            if validar_numero_afiliado(numero_afiliado):
                tipo_atencion = int(input("Urgencia o con turno (0 para urgencia, 1 para turno): "))
                if validar_tipo_atencion(tipo_atencion):
                    registrar_atencion(numero_afiliado, tipo_atencion)
                    print(buscar_atencion(numero_afiliado))
                else:
                    print("ERROR. Revisa que urgencia o turno corresponda a 0 o 1.")
            else:
                print("ERROR. Revisa que el número de afiliado tenga 4 dígitos.")
        except ValueError:
            print("ERROR. Revisa de ingresar números enteros.")

    mostrar_listados()

lista_urgencias = []
lista_turnos = []
if __name__ == "__main__":
    main()
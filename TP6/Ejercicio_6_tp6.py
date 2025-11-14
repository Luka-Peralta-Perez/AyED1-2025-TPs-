"""
    6. Un hotel necesita un programa para gestionar la operación de sus habitaciones. El hotel 
    cuenta con 10 pisos y 6 habitaciones por piso. Por cada huésped o grupo familiar que se aloja en el mismo se registra la siguiente información:
    
     · DNI del cliente (número entero)
     · Apellido y Nombre
     · Fecha de ingreso (DDMMAAAA)
     · Fecha de egreso  (DDMMAAAA)
     · Cantidad de ocupantes
    Se solicita desarrollar un programa para realizar las siguientes tareas:
    
    · Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de DNI -1.
    Esta información deberá grabarse en un archivo CSV donde cada registro incluirá todos 
    los campos indicados más arriba. Tener en cuenta que los números de DNI no pueden 
    repetirse y que la fecha de salida debe ser mayor a la de entrada.
    
     · Finalizado el ingreso de huéspedes se solicita:
     a. Leer el archivo de huéspedes y asignar la habitaciones a cada uno. El piso y habitación son asignados arbitrariamente, y no puede asignarse una habitación ya 
        otorgada.
    
     b. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
     
     c. Mostrar cuántas habitaciones vacías hay en todo el hotel.
     
     d. Mostrar el piso con mayor cantidad de personas.
     
     e. Mostrar cuál será la próxima habitación en desocuparse. La fecha actual se ingresa por teclado. Mostrar todas las que correspondan.
 
     f. Mostrar un listado de todos los huéspedes registrados en el hotel, ordenado por cantidad de días de alojamiento.
"""
def validar_fecha(fecha: str) -> bool:
    """Valida que una fecha en formato DDMMAAAA sea válida."""
    if len(fecha) != 8 or not fecha.isdigit():
        return False
    
    dia = int(fecha[:2])
    mes = int(fecha[2:4])
    año = int(fecha[4:])
    
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if mes in {4, 6, 9, 11} and dia > 30:
        return False
    if año < 2000:
        return False
    # Validación específica para febrero
    if mes == 2:
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):  # Año bisiesto
            if dia > 29:
                return False
        elif dia > 28:
            return False
    return True

def registrar_huespedes(archivo_salida: str) -> None:
    """Registra los huéspedes en un archivo."""
    dnis_registrados = set()  # Para evitar repeticiones de DNI
    
    with open(archivo_salida, 'w') as f:
        while True:
            dni = input("Ingrese el DNI del cliente (-1 para terminar): ").strip()
            
            if dni == "-1":  # Comparar como cadena
                print("Registro finalizado.")
                break
            
            if not dni.isdigit():
                print("Error: DNI debe ser un número entero positivo.")
                continue
            
            if dni in dnis_registrados:
                print("Error: DNI ya registrado.")
                continue
            
            # Solicitar datos del huésped
            apellido_nombre = input("Ingrese Apellido y Nombre: ").strip()
            
            fecha_ingreso = input("Ingrese fecha de ingreso (DDMMAAAA): ").strip()
            while not validar_fecha(fecha_ingreso):
                print("Fecha inválida. Intente nuevamente.")
                fecha_ingreso = input("Ingrese fecha de ingreso (DDMMAAAA): ").strip()
            
            fecha_egreso = input("Ingrese fecha de egreso (DDMMAAAA): ").strip()
            while not validar_fecha(fecha_egreso) or fecha_egreso <= fecha_ingreso:
                print("Fecha inválida o anterior a la fecha de ingreso. Intente nuevamente.")
                fecha_egreso = input("Ingrese fecha de egreso (DDMMAAAA): ").strip()
            
            cantidad_ocupantes = input("Ingrese cantidad de ocupantes: ").strip()
            while not cantidad_ocupantes.isdigit() or int(cantidad_ocupantes) < 1:
                print("Cantidad inválida. Debe ser un número mayor o igual a 1.")
                cantidad_ocupantes = input("Ingrese cantidad de ocupantes: ").strip()
            
            # Escribir registro al archivo
            f.write(f"{dni},{apellido_nombre},{fecha_ingreso},{fecha_egreso},{cantidad_ocupantes}\n")
            dnis_registrados.add(dni)

def asignar_habitaciones(archivo_huespedes: str) -> dict:
    """Asigna habitaciones a los huéspedes y retorna un diccionario con la información."""
    habitaciones = {}
    with open(archivo_huespedes, 'r') as f:
        for linea in f:
            dni, apellido_nombre, fecha_ingreso, fecha_egreso, cantidad_ocupantes = linea.strip().split(',')
            piso = len(habitaciones) // 6 + 1
            if piso > 10:  # Verificar que no exceda el límite de pisos
                print(f"No hay más habitaciones disponibles para el huésped {apellido_nombre}")
                continue
            habitacion = len(habitaciones) % 6 + 1
            habitaciones[dni] = (apellido_nombre, piso, habitacion, fecha_ingreso, fecha_egreso, cantidad_ocupantes)
    return habitaciones

def habitaciones_ocupadas(habitaciones: dict) -> None:
    """Muestra el piso con mayor cantidad de habitaciones ocupadas."""
    ocupadas = {}
    for _, datos in habitaciones.items():
        piso = datos[1]
        ocupadas[piso] = ocupadas.get(piso, 0) + 1
    
    if ocupadas:
        piso_max_ocupado = max(ocupadas, key=ocupadas.get)
        print(f"Piso con mayor cantidad de habitaciones ocupadas: {piso_max_ocupado}")
        print(f"Cantidad de habitaciones ocupadas en ese piso: {ocupadas[piso_max_ocupado]}")

def habitaciones_vacias(habitaciones: dict) -> None:
    """Muestra la cantidad total de habitaciones vacías."""
    total_habitaciones = 10 * 6  # 10 pisos x 6 habitaciones
    ocupadas = len(habitaciones)
    print(f"Total de habitaciones vacías: {total_habitaciones - ocupadas}")

def piso_mas_personas(habitaciones: dict) -> None:
    """Muestra el piso con mayor cantidad de personas."""
    personas_por_piso = {}
    for _, datos in habitaciones.items():
        piso = datos[1]
        ocupantes = int(datos[5])
        personas_por_piso[piso] = personas_por_piso.get(piso, 0) + ocupantes
    
    if personas_por_piso:
        piso_max_personas = max(personas_por_piso, key=personas_por_piso.get)
        print(f"Piso con mayor cantidad de personas: {piso_max_personas}")
        print(f"Cantidad de personas en ese piso: {personas_por_piso[piso_max_personas]}")

def proxima_habitacion_desocupada(habitaciones: dict, fecha_actual: str) -> None:
    """Muestra las habitaciones que se desocuparán próximamente."""
    desocupadas = []
    for dni, datos in habitaciones.items():
        fecha_egreso = datos[4]
        if fecha_egreso > fecha_actual:
            desocupadas.append((dni, datos))
    
    if desocupadas:
        print("\nHabitaciones que se desocupan próximamente:")
        # Ordenar por fecha de egreso
        desocupadas.sort(key=lambda x: x[1][4])
        for dni, datos in desocupadas:
            print(f"DNI: {dni}")
            print(f"Nombre: {datos[0]}")
            print(f"Piso: {datos[1]}, Habitación: {datos[2]}")
            print(f"Fecha de egreso: {datos[4]}\n")
    else:
        print("No hay habitaciones por desocuparse próximamente")

def main():
    archivo_huespedes = 'huespedes.txt'
    
    # Registrar huéspedes
    registrar_huespedes(archivo_huespedes)
    
    # Asignar habitaciones y obtener diccionario con la información
    habitaciones = asignar_habitaciones(archivo_huespedes)
    
    # Mostrar estadísticas
    habitaciones_ocupadas(habitaciones)
    habitaciones_vacias(habitaciones)
    piso_mas_personas(habitaciones)
    
    # Verificar próximas desocupaciones
    fecha_actual = input("Ingrese la fecha actual (DDMMAAAA): ")
    while not validar_fecha(fecha_actual):
        print("Fecha inválida. Intente nuevamente.")
        fecha_actual = input("Ingrese la fecha actual (DDMMAAAA): ")
    
    proxima_habitacion_desocupada(habitaciones, fecha_actual)

if __name__ == "__main__":
    main()

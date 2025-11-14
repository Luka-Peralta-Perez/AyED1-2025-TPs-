"""
    3. Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los 
    próximos Juegos Panamericanos. Para eso encargó la realización de un programa 
    que incluya las siguientes funciones:
    GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas 
    disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una 
    línea distinta. Ejemplo:
     <Deporte 1>
     <altura del atleta 1>
     <altura del atleta 2>
     < . . . >
     <Deporte 2>
     <altura del atleta 1>
     <altura del atleta 2>
     < . . . >
    GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atletas,
    leyendo los datos del archivo generado en el paso anterior. La disciplina y el 
    promedio deben grabarse en líneas diferentes. Ejemplo:
     <Deporte 1>
     <Promedio de alturas deporte 1>
     <Deporte 2>
     <Promedio de alturas deporte 2>
     < . . . >

    MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas 
    superan la estatura promedio general. Obtener los datos del segundo archivo.
"""

def grabar_alturas(archivo: str) -> None:
    """
    Graba las alturas de los atletas de distintas disciplinas en un archivo.

    Args:
    - archivo (str): Nombre del archivo donde se guardarán las alturas.
    """
    with open(archivo, 'w') as f:
        while True:
            deporte = input("Ingrese el nombre del deporte (o 'fin' para terminar): ")
            if deporte.lower() == 'fin':
                break
            
            f.write(f"{deporte}\n")
            while True:
                altura = input(f"Ingrese la altura del atleta (o 'fin' para terminar): ")
                if altura.lower() == 'fin':
                    break
                f.write(f"{altura}\n")

def grabar_promedio(archivo_alturas: str, archivo_promedios: str) -> None:
    """
    Graba los promedios de las alturas de los atletas en un archivo.

    Args:
    - archivo_alturas (str): Nombre del archivo que contiene las alturas.
    - archivo_promedios (str): Nombre del archivo donde se guardarán los promedios.
    """
    with open(archivo_alturas, 'r') as f:
        lineas = f.readlines()

    promedios = {}
    deporte_actual = ""
    alturas = []

    for linea in lineas:
        linea = linea.strip()
        if linea:  # Ignorar líneas vacías
            if not linea.isdigit() and linea.replace('.', '', 1).isdigit():  # Verificar si es una altura
                alturas.append(float(linea))
            else:  # Es un deporte
                if deporte_actual and alturas:  # Guardar el promedio del deporte anterior
                    promedio = sum(alturas) / len(alturas)
                    promedios[deporte_actual] = promedio
                deporte_actual = linea
                alturas = []

    # Guardar el último deporte
    if deporte_actual and alturas:
        promedio = sum(alturas) / len(alturas)
        promedios[deporte_actual] = promedio

    # Grabar promedios en el archivo
    with open(archivo_promedios, 'w') as f:
        for deporte, promedio in promedios.items():
            f.write(f"{deporte}\n{promedio:.2f}\n")

def mostrar_mas_altos(archivo_promedios: str) -> None:
    """
    Muestra las disciplinas cuyos atletas superan la altura promedio general.

    Args:
    - archivo_promedios (str): Nombre del archivo que contiene los promedios.
    """
    with open(archivo_promedios, 'r') as f:
        lineas = f.readlines()

    promedios = {}
    total_alturas = 0
    total_deportes = 0

    for i in range(0, len(lineas), 2):
        deporte = lineas[i].strip()
        promedio = float(lineas[i + 1].strip())
        promedios[deporte] = promedio
        total_alturas += promedio
        total_deportes += 1

    if total_deportes > 0:
        promedio_general = total_alturas / total_deportes
        print(f"Promedio general de alturas: {promedio_general:.2f}")
        print("Disciplinas cuyos atletas superan la altura promedio general:")
        for deporte, promedio in promedios.items():
            if promedio > promedio_general:
                print(deporte)

def main() -> None:
    """
    Función principal que ejecuta el programa.
    """
    archivo_alturas = "alturas_atletas.txt"
    archivo_promedios = "promedios_alturas.txt"

    grabar_alturas(archivo_alturas)
    grabar_promedio(archivo_alturas, archivo_promedios)
    mostrar_mas_altos(archivo_promedios)

if __name__ == "__main__":
    main()
    
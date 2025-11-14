"""
2. Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuar
se después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria.
"""
def dividir_archivo(nombre_archivo, tamano_maximo):
    try:
    with open(nombre_archivo, "r") as archivo:
    parte = 1
    tamano_actual = 0
    archivo_salida = None
    for linea in archivo:
        if archivo_salida is None or tamano_actual + len(linea) > tamano_maximo:
        if archivo_salida:
        archivo_salida.close()
        nombre_parte = f"{nombre_archivo}_parte_{parte}.txt"
        archivo_salida = open(nombre_parte, "w")
        parte += 1
        tamano_actual = 0
        archivo_salida.write(linea)
        tamano_actual += len(linea)
    if archivo_salida:
    archivo_salida.close()
    print("El archivo fue dividido correctamente.")
    except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
    except Exception as e:
    print(f"Error: No se pudo completar el proceso. Detalles: {e}")
def main() -> None:
nombre_archivo = input("Ingrese el nombre del archivo a dividir: ")
try:
tamano_maximo = int(input("Ingrese el tamaño máximo de cada parte (en bytes): "))
if tamano_maximo <= 0:
print("Error: El tamaño debe ser un número positivo.")
return
dividir_archivo(nombre_archivo, tamano_maximo)
except ValueError:
print("Error: El tamaño máximo debe ser un número entero.")
if __name__ == "__main__":
main()

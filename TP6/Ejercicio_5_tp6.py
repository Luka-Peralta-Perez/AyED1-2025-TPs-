"""
     5. Se dispone de tres formatos diferentes de archivos de texto en los que se
     almacenan datos de empleados, detallados más abajo. Desarrollar un programa para cada 
    uno de los formatos suministrados, que permitan leer cada uno de los archivos y 
    grabar los datos obtenidos en otro archivo de texto con formato CSV.
"""

import os

def archivo_fijo(archivo_entrada, archivo_salida):
    # Verificar si el archivo de entrada existe
    if not os.path.exists(archivo_entrada):
        print(f"Error: El archivo '{archivo_entrada}' no se encuentra en la ubicación actual.")
        return
    
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f, open(archivo_salida, 'w', encoding='utf-8') as salida:
            for linea in f:
                # Definimos las longitudes de los campos
                longitudes = [15, 8, 8, 20]  # Longitudes de los campos
                fila = []
                inicio = 0
                for longitud in longitudes:
                    # Leer cada campo según la longitud definida
                    campo = linea[inicio:inicio + longitud].strip()  # Leer y eliminar espacios en blanco
                    fila.append(campo)
                    inicio += longitud  # Mover el índice para el siguiente campo
                
                # Escribir los campos en el archivo CSV
                salida.write(','.join(fila) + '\n')
        print(f"Archivo '{archivo_salida}' generado exitosamente.")
    except Exception as e:
        print(f"Error al procesar el archivo '{archivo_entrada}': {e}")

def main():
    archivo_entrada = 'prueba.txt'  # Archivo de entrada
    archivo_salida = 'prueba.csv'   # Archivo CSV de salida
    archivo_fijo(archivo_entrada, archivo_salida)

if __name__ == "__main__":
    main()

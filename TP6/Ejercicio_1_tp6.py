"""
     1. Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo 
     ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los terminados en "EZ". Descartar el resto. Ejemplo:
         Arslanian, Gustavo–> ARMENIA.TXT
         Rossini, Giuseppe–> ITALIA.TXT
         Pérez, Juan –> ESPAÑA.TXT
         Smith, John–> descartar
     El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor. 
"""

def procesar_archivo_nombres(nombre_archivo: str) -> None:
      try:
        # Leer el archivo de entrada
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            nombres = archivo.readlines()
            
        # Crear o limpiar los archivos de destino
        open('ARMENIA.TXT', 'w', encoding='utf-8').close()
        open('ITALIA.TXT', 'w', encoding='utf-8').close()
        open('ESPAÑA.TXT', 'w', encoding='utf-8').close()
        
        # Procesar cada línea
        for nombre in nombres:
            nombre = nombre.strip()
            if nombre and ',' in nombre:  # Verificar que la línea no esté vacía y tenga el formato correcto
                apellido = nombre.split(',')[0].strip()
                
                # Clasificar según la terminación
                if apellido.upper().endswith('IAN'):
                    with open('ARMENIA.TXT', 'a', encoding='utf-8') as f:
                        f.write(nombre + '\n')
                elif apellido.upper().endswith('INI'):
                    with open('ITALIA.TXT', 'a', encoding='utf-8') as f:
                        f.write(nombre + '\n')
                elif apellido.upper().endswith('EZ'):
                    with open('ESPAÑA.TXT', 'a', encoding='utf-8') as f:
                        f.write(nombre + '\n')
                        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main() -> None:
    """Función principal del programa"""
    try:
        # Procesar el archivo
        procesar_archivo_nombres('apellidos.txt')
        
        
        print("\nProcesamiento completado. Contenido de los archivos generados:")
        
        # Mostrar contenido de cada archivo
        archivos = ['ARMENIA.TXT', 'ITALIA.TXT', 'ESPAÑA.TXT']
        for archivo in archivos:
            print(f"\nContenido de {archivo}:")
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read().strip()
                    if contenido:
                        print(contenido)
                    else:
                        print("(Archivo vacío)")
            except FileNotFoundError:
                print(f"No se pudo leer el archivo {archivo}")
                
    except Exception as e:
        print(f"Error en el programa: {str(e)}")

if __name__ == "__main__":
    main()
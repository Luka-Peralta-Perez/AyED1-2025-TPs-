"""
    4. Desarrollar un programa para eliminar todos los comentarios de un programa
    escrito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el 
    signo # (siempre que éste no se encuentre encerrado entre comillas simples o
    dobles) y que también se considera comentario a las cadenas de documentación 
    (docstrings).
    
"""
import re

def eliminar_comentarios(archivo_entrada: str, archivo_salida: str) -> None:
    """
    Elimina los comentarios y docstrings de un archivo Python.
    """
    with open(archivo_entrada, 'r') as f:
        lineas = f.readlines()

    # Expresión regular para eliminar docstrings
    docstring_pattern = re.compile(r'("""(.*?)"""|\'\'\'(.*?)\'\'\'|#.*?$)', re.DOTALL | re.MULTILINE)

    # Lista para almacenar las líneas sin comentarios
    lineas_sin_comentarios = []

    for linea in lineas:
        # Eliminar docstrings y comentarios de la línea
        linea_limpia = docstring_pattern.sub('', linea).strip()
        if linea_limpia:  # Solo agregar líneas no vacías
            lineas_sin_comentarios.append(linea_limpia)

    # Guardar el resultado en el archivo de salida
    with open(archivo_salida, 'w') as f:
        for linea in lineas_sin_comentarios:
            f.write(linea + '\n')

def main() -> None:
    """
    Función principal que ejecuta el programa.
    """
    archivo_entrada = input("Ingrese el nombre del archivo Python a procesar: ")
    archivo_salida = input("Ingrese el nombre del archivo de salida: ")
    
    eliminar_comentarios(archivo_entrada, archivo_salida)
    print(f"Comentarios eliminados. El código limpio se ha guardado en '{archivo_salida}'.")

if __name__ == "__main__":
    main()

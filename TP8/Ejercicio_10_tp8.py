"""
    10.Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario 
    y una lista de claves. La función debe eliminar del diccionario todas las claves 
    contenidas en la lista, devolviendo el diccionario modificado y un número entero 
    que represente la cantidad de claves eliminadas. Desarrollar también un programa 
    para verificar su comportamiento.
"""

def eliminarclaves(diccionario: dict, claves: list)-> tuple:
    """
    Elimina claves especificas de un diccionario.
    """
    
    claves_eliminadas = 0
    
    for clave in claves:
        if clave in diccionario:
            diccionario.pop(clave)
            claves_eliminadas += 1
    return diccionario, claves_eliminadas

def main() -> None:
    
    try:
        diccionario = {
            "Alumno": "Luka Peralta",
            "LU" : "1170204",
            "Edad" : "21 años",
            "Carrera" : "Tec en desarrollo de software"
            }
        
        print("Diccionario Inicial", diccionario)
        
        claves_eliminar = ["Edad", "Carrera", "LU"]
        
        diccionario_nuevo, eliminadas = eliminarclaves(diccionario, claves_eliminar)
        
        print(f"\nDiccionario modificado {diccionario_nuevo}\n")
        print(f"\nCantidad de claves eliminadas: {eliminadas}")
        
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    main()
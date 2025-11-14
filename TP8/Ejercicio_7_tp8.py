"""
    7. Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al 
    usuario y eliminarlos del conjunto mediante el método remove, mostrando el con
    tenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1. 
    Utilizar manejo de excepciones para evitar errores al intentar quitar elementos 
    inexistentes.
"""

def conjunto_inicial():
    """
    Crea un conjunto inicial con números del 0 al 9.
    """
    conjunto = set(range(10))
    
    print(f"Conjunto inicial: {conjunto}")
    return conjunto

def remover_numero(conjunto: set)-> None:
    """
    Solicita al usuario numeros para eliminarlos del conjunto.
    Muestra el contenido del conjunto despues de cada eliminacion
    
    Pre:
        - Conjunto: Conjunto de numeros eneteros
    Post:
        - Actualiza el conjunto eliminando numeros hasta que el usairio ingrese -1.
    """
    while True:
        try:
            numero = int(input("Ingrese un numero para eliminar (-1 para salir): "))
            
            if numero == -1:
                print("Saliendo...")
                break
            
            conjunto.remove(numero)
            print(f"Número {numero} eliminado. Conjunto actual: {conjunto}")
            
        except KeyError:
            print(f"ERROR: El numero {numero} no esta dentro del conjunto. Intente nuevamente.")
        except ValueError:
            print(f"ERROR: Ingrese un valor valido.")
        except Exception as e:
            print(f"Se produjo un error inesperado {e}")

def main():
    """
    funcion principal donde se prueba el programa.
    """
    conjunto = conjunto_inicial()
    remover_numero(conjunto)
    
if __name__ == "__main__":
    main()
            
            

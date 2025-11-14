"""
    6. El método index permite buscar un elemento dentro de una lista, devolviendo la
    posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
    produce una excepción de tipo ValueError. Desarrollar un programa que cargue
    una lista con números enteros ingresados a través del teclado (terminando con -1)
    y permita que el usuario ingrese el valor de algunos elementos para visualizar la
    posición que ocupan, utilizando el método index. Si el número no pertenece a la
    lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
    proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

def cargar_lista() -> list[int]:
    
    lista = []
    while True:
        try:
            usuario = int(input("\nIngrese un número ( -1 para terminar): "))
            if usuario == -1:
                print("Saliendo de cargar la lista...")
                break
            lista.append(usuario)
        
        except ValueError:
             print("ERROR. debe solo debe ingresar numeros. ")
    return lista

def buscar_num(lista: list) -> None:
    errores = 0
    while errores < 3:
        try:
            buscar_numero = int(input("Ingrese el numero a buscar dentro de la lista: "))
            print(f"El numero{buscar_numero}, esta en la posicion {lista.index(buscar_numero)}.")
            errores = 0
            
        except ValueError:
            print(f"El numero {buscar_numero}, no se esncuentra en la lista. Intentos fallidos {errores}.")
            errores += 1
            if errores == 3:
                print("Se realizaron 3 ERRORES, el programa se cerrara. SALIENDO...")
                break
            
def main()-> None:
    
    lista = cargar_lista()
    print(f"lista cargada: {lista}")
    buscar_num(lista)
    
if __name__ == "__main__":
    main()
            
    
    
            
        
"""
    4. Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas 
    son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True 
    o False. Escribir también un programa para verificar su comportamiento. Considerar 
    el uso de conjuntos para resolver este ejercicio.


"""

def encajar_fichas(ficha1: tuple, ficha2: tuple) -> bool:
    """
    Verifica si dos fichas de dominó encajan entre sí.
    
    Pre:
        ficha1: tupla de dos enteros representando una ficha de dominó
        ficha2: tupla de dos enteros representando una ficha de dominó
        
    Post:
        bool: True si las fichas encajan (tienen un número en común),
              False si no encajan
    
    Ejemplo:
        encajan_fichas((3,4), (5,4)) -> True
        encajan_fichas((1,2), (3,4)) -> False
    """
    num_ficha1 = set(ficha1)
    num_ficha2 = set(ficha2)
    
    return bool(num_ficha1 & num_ficha2)

def main()-> None:
    """
    Función principal para solicitar las fichas de dominó y verificar si encajan.
    """
    try:
        print("\nPrimera ficha\n")
        
        n1 = int(input("Ingrese el primer  número: "))
        n2= int(input("Ingrese el segundo  número: "))
        ficha1 = (n1, n2)
        
        print("\nSegunda ficha\n")
        
        n3 = int(input("Ingrese el primer número: "))
        n4 = int(input("Ingrese el segundo número: "))
        ficha2 = (n3, n4)
        
        if encajar_fichas(ficha1, ficha2):
            print(f"\nLas fichas {ficha1} y {ficha2} encajan!")
        else:
            print(f"\nLas fichas {ficha1} y {ficha2} no encajan.")
            
    except ValueError:
        print("\nError: Por favor ingrese números enteros válidos.")

if __name__ == "__main__":
    main()
        

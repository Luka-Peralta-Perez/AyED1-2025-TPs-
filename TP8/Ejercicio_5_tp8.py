"""
    5. En geometría un vector es un segmento de recta orientado que va desde un punto 
    A hasta un punto B. Los vectores en el plano se representan mediante un par ordenado de números reales (x, y) llamados componentes.
    Para representarlos basta con unir el origen de coordenadas con el punto indicado en sus componentes: 
    Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo: 

    A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
    Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor de verdad indicando si son ortogonales o no. Desarrollar también un programa
    que permita verificar el comportamiento de la función.
     
"""

def vectores(vector1: tuple, vector2: tuple)-> bool:
    producto_escalar = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    
    return producto_escalar == 0

def main() -> None:
    try:
        print("\nIngrese las componentes del primer vector\n")
        x1 = float(input("Componente x1: "))
        y1 = float(input("Componente y1: "))
        vector1 = (x1, y1)
        
        print("\nIngrese los componentes del segundo vector\n")
        x2 = float(input("Componente x2: "))
        y2 = float(input("Componente y2: "))
        vector2 = (x2, y2)
        
        if vectores(vector1, vector2):
            print(f"\nLos vectores {vector1} y {vector2} son ortogonales.")
        
        else:
            print(f"\nLos vectores {vector1} y {vector2} no son ortogonales")
    except ValueError:
        print("\nERROR: Por Favor ingresar numeros reales validos.")
if __name__ == "__main__":
    main()
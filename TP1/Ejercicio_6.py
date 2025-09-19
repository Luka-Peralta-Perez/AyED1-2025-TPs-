"""
    6. Desarrollar una función que reciba como parámetros dos números enteros positivos
    y devuelva como valor de retorno el número que resulte de concatenar ambos parámetros.
    Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase.
    
"""
def concatenar_numero(n1: int, n2: int)-> str:
    """
    esta funcion se encarga de concatenar los numero ingresados por el usuario.
    
    Pre:
        - n1 y n2 deben ser numero enteros positivos mayores a 0
    Post:
        - La funcion devuelve un numero entero, que resulta de la
        concatenación de n1 y n2.
    """
    dig = 0
    aux = n2
    while aux > 0:
        aux //= 10
        dig += 1
    numero = n1 * (10 ** dig) + n2 
    return numero

def main() -> None:
    try:
        num = int(input("Ingrese el primer numero a concatenar: "))
        num2 = int(input("Ingrese el segundo numero a concatenar: "))
        print(concatenar_numero(num, num2))
    except ValueError:
        print("ERROR. Valor ingresado no valido.")

if __name__ == "__main__":
    main()

    
    
"""
    5. Escribir funciones lambda para:
    a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
    se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3.
    
    b. Informar si un número es triangular. Un número se define como triangular si
    puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
    obtiene sumando 1+2+3+4.
    
    Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False. No se permite utilizar ayudas externas a las mismas.
    
"""

es_oblongo = lambda n: n > 0 and any(n == i * (i + 1) for i in range(1, int(n ** .5) + 1))

es_triangular = lambda n: n > 0 and any(n == i * (i + 1) // 2 for i in range(1, int((2 * n) ** .5) + 1))

def main() -> None:
    """Solicita un número y reporta si es oblongo y/o triangular."""
    try:
        usuario = int(input("Ingrese el número: "))
        if usuario <= 0:
            print("ERROR: debe ser un número natural (mayor a 0).")
            return

        print(f"El número {usuario} {'es' if es_oblongo(usuario) else 'no es'} oblongo.")
        print(f"El número {usuario} {'es' if es_triangular(usuario) else 'no es'} triangular.")

    except ValueError:
        print("ERROR: verifique que el número sea entero.")

if __name__ == "__main__":
    main()

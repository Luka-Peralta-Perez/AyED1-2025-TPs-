"""
   12.Una librería almacena su lista de precios en un diccionario. Diseñar un programa 
    para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un 
    listado con todos los elementos de la lista de precios e indicar cuál es el ítem más 
    costoso que venden en el comercio.
    
"""
def crear_lista_precios():
    """
    Crea un diccionario inicial con los productos de la librería y sus precios.
    
    Pre: 
        - No recibe parámetros.
    Post: 
        - Devuelve un diccionario con los nombres de los productos como claves 
         y sus precios como valores.
    """
    # Creamos el diccionario con algunos productos de librería
    precios = {
        'cuaderno A4': 5000.00,
        'cuaderno A5': 4500.50,
        'lapicera': 1200.00,
        'borrador': 1000.00,
        'resaltador': 3000.00,
        'cuaderno universitario': 7000.50,
        'cartuchera': 6000.00,
        'regla': 1000.50
    }
    return precios

def incrementar_precio(precios: dict, porcentaje)-> None:
    """
    Incrementa los precios de los productos que contengan "cuaderno" en su nombre 
    según el porcentaje indicado.
    
    Pre:
        - `precios` debe ser un diccionario donde las claves son productos (str) y los valores son precios (float).
        - `porcentaje` debe ser un número positivo.
    
    Post:
        Devuelve el diccionario modificado con los precios incrementados para los productos seleccionados.
    """
    for producto in precios:
        if "cuaderno" in producto.lower():
            precios[producto] *= (1 + porcentaje/100)
    return precios

def imprimir_precios(precios)-> None:
    """
    Imprime en formato de tabla los productos y sus precios.
    
    Pre:
        `precios` debe ser un diccionario con claves de tipo str y valores de tipo float.
    
    Post:
        No devuelve nada, pero muestra los productos y sus precios en formato tabular.
    """
    print("\nLista de precios actualizada:")
    print("-" * 40)
    print(f"{'Producto':<25} {'Precio':>10}")
    print("-" * 40)
    for producto, precio in precios.items():
        print(f"{producto:<25} ${precio:>9.2f}")

def mas_caro(precios):
    """
    Encuentra el producto más costoso en el diccionario.
    
    Pre:
        `precios` debe ser un diccionario no vacío con claves de tipo str y valores de tipo float.
    
    Post:
        Devuelve una tupla con el nombre del producto más costoso y su precio.
    """
    mayor_precio = max(precios, key = precios.get)
    return mayor_precio, precios[mayor_precio]


def main() -> None:
    """
    Programa principal que ejecuta las funcionalidades:
    - Crea la lista de precios.
    - Incrementa los precios de los cuadernos en un 15%.
    - Imprime los precios actualizados.
    - Encuentra e imprime el producto más costoso.
    """
 
    precios = crear_lista_precios()
    
    
    print("\nLista de precios original:")
    imprimir_precios(precios)
    
    # Incrementar precio de cuadernos en 15%
    precios = incrementar_precio(precios, 15)
    
    # Mostrar lista actualizada
    print("\nLista después del incremento:")
    imprimir_precios(precios)
    
    
    producto_mas_caro, precio_mas_alto = mas_caro(precios)
    print(f"\nEl producto más costoso es: {producto_mas_caro} (${precio_mas_alto:.2f})")

if __name__ == "__main__":
    main()
    

    
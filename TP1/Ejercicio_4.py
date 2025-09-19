"""
    4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que
    le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
    dos números enteros, correspondientes al total de la compra y al dinero recibido.
    Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
    de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
    de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
    dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
    de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
    abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
    billete de $200, 1 billete de $100 y 3 billetes de $10.
    
"""

def calcular_vuelto(compra: int, dinero_recibido: int):
    """
    Calcula el vuelto total por billete que debe devolver al cliente,
    con una lista que contiene las denominacion de los billetes.
    
    Pre:
        - Total de la compra(el gasto realizado)
        - total del dinero recibido (El pago realizado)
        
    Post:
        - Devuelve un diccionario 
    """
    if compra < 0 or dinero_recibido < 0:
        print("ERROR: la compra y el dinero deben ser positivos.")
        return None

    if dinero_recibido < compra:
        print("ERROR: el dinero recibido es insuficiente.")
        return None
    
    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    cambio = dinero_recibido - compra
    vuelto = {}
    
    for billete in billetes:
        cantidad = cambio // billete
        if cantidad > 0:
            vuelto[billete] = cantidad
            cambio %= billete
            
    if cambio != 0:
        print("ERROR, no se puede entregar el cambio por falta de billetes. ")
        return
    
    total_billetes = sum(vuelto.values())
    
    print("Vuelto: ")
    for billete, cantidad in vuelto.items():
        print(f"{cantidad} billete(s) de ${billete}")#
    print(f"Total de billetes entregados: {total_billetes}")
        
    return vuelto

def main() -> None:
    """
     Funcion principal, el usuario ingresa el total que gasto y el dinero que entrego.
     
    """
    try:
        compra = int(input("Ingrese el total de la compra: "))
        dinero_recibido = int(input("Ingrese el dinero recibido: "))
        calcular_vuelto(compra, dinero_recibido)
    except ValueError:
        print("ERROR. Revisa que el valor de la compra y el dinero recibido sean numeros enteros positivos. ")
        
if __name__ == "__main__":
    main()
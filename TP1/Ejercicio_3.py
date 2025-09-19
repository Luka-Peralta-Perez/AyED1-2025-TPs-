"""
    3. Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes.
    Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo)
    se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en undeterminado mes y
    devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.
"""

def cantidad_viajes(viajes: int) -> float:
    """
    Calcula el gasto total en viajes, en base a la tarifa basica y los viajes realizados.
    
    Pre:
        - Viajes debe ser un numero entero positivo.
        
    Post:
        -Gasto total de viajes.
    """
    if viajes < 1:
        raise ValueError("La cantidad de viajes debe ser un numero entero positivo. ")
    
    tarifa_basica = 1322
    
    if viajes > 1 and viajes < 20:
        return tarifa_basica * viajes
    
    elif viajes <= 30:
        return tarifa_basica * viajes * 0.8 #20% de descuento
    
    elif viajes >= 31 and viajes <= 40:
        return tarifa_basica * viajes * 0.7 #30% de descuento
    
    else:
        return tarifa_basica * viajes *  0.6 #40% de descuento
    
def main() -> None:
    while True:
        try:
            usuario = int(input("Ingrese la cantidad de viajes realizados (-1 para salir): "))
            if usuario < 0:
                print("ERROR , la cantidad de viajes no puede ser menor a 1. ")
            if usuario == -1:
                print("Saliendo...")
                break
            else:
                total = cantidad_viajes(usuario)
                print(f"El total gastado es de ${total}")
        except ValueError:
            print("ERROR: la cantidad de viajes debe ser un numero entero positivo, intente de nuevo. ")
            
                
if __name__ == "__main__":
    main()
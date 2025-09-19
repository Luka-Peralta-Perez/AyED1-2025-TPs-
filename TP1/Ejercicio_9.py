"""
    9. Resolver el siguiente problema utilizando funciones:
    Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
    para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
    cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
    caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
    de alguna naranja se encuentra fuera del rango indicado se la clasifica para
    procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
    cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
    jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
    reparto. Simular el peso de cada unidad generando un número entero al azar entre
    150 y 350.
    
    Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando
    que la ocupación del camión no debe ser inferior al 80%;
    en caso contrario el camión no serán despachado por su alto costo.

"""


from random import randint
from typing import Tuple


def clasificar_y_cajonear(cantidad: int) -> Tuple[int, int, int, int]:
    """
    Clasifica naranjas según peso y forma cajones completos.

    Pre:
        
    Post:
        Devuelve:
            - naranjas_jugo: int (fuera de 200-300 g)
            - cajones_llenos: int (100 útiles cada uno)
            - sobrante_utiles: int (naranjas útiles que no completan cajón)
            - peso_util_total: int (gramos de naranjas útiles)
    """
    utiles_en_cajon = 0
    naranjas_jugo = 0
    cajones_llenos = 0
    peso_util_total = 0

    for _ in range(cantidad):
        peso = randint(150, 350)  # gramos
        if 200 <= peso <= 300:
            utiles_en_cajon += 1
            peso_util_total += peso
            if utiles_en_cajon == 100:
                cajones_llenos += 1
                utiles_en_cajon = 0
        else:
            naranjas_jugo += 1

    sobrante_utiles = utiles_en_cajon
    return naranjas_jugo, cajones_llenos, sobrante_utiles, peso_util_total


def camiones_despachados(peso_util: int) -> Tuple[int, int]:
    """
    Calcula camiones que pueden despacharse con ≥ 80 % de ocupación.

    Pre:
        peso_util >= 0 (gramos)
    Post:
        Devuelve:
            - camiones_despachados: int
            - sobrante_peso: int (gramos que no completan camión mínimo)
    """
    CAPACIDAD_CAMION = 500_000  # g
    MINIMO = int(0.8 * CAPACIDAD_CAMION)  # 80 %

    camiones = peso_util // CAPACIDAD_CAMION
    sobrante = peso_util % CAPACIDAD_CAMION
    if sobrante >= MINIMO:
        camiones += 1
        sobrante = 0
    return camiones, sobrante


def main() -> None:
    """
    Solicita cantidad de naranjas y muestra cajones y camiones.

    Pre:
        - El usuario ingresa un número entero positivo
    Post:
        - Se imprimen los resultados en pantalla
    """
    try:
        cantidad = int(input("Ingrese la cantidad de naranjas cosechadas: "))
        if cantidad <= 0:
            print("ERROR: Debe ser un número positivo.")
            return

        jugo, cajones, sobrante_unidades, peso_util = clasificar_y_cajonear(cantidad)
        print(f"\nCajones completos: {cajones}")
        print(f"Naranjas para jugo: {jugo}")
        print(f"Sobrante de naranjas útiles: {sobrante_unidades}")

        if cajones:
            print(f"Peso promedio por cajón: {peso_util / cajones / 1000:.1f} kg")

        camiones, sobrante_peso = camiones_despachados(peso_util)
        print(f"Camiones despachados (> 80 %): {camiones}")
        if sobrante_peso > 0:
            print(f"Sobrante de peso para próximo reparto: {sobrante_peso / 1000:.1f} kg")

    except ValueError:
        print("ERROR: ingrese un número entero válido.")


if __name__ == "__main__":
    main()
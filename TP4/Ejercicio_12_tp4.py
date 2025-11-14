"""
    12.Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe contener cadenas de caracteres.
    Ejemplo: ["1 Oros", "2 Oros"... ]. Imprimir la lista por pantalla.
"""

def crear_baraja()-> list[str]:
    """
    Genera una lista con los naipes de la baraja española.
    
    Pre:
        - Ninguna.

    Post:
        - Devuelve una lista con los naipes en formato "Número Palo", por ejemplo: ["1 Oros", "2 Oros", ...].
    """
    
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    
    baraja = [f"{numero} {palo}"for palo in palos for numero in range(1, 13)]
    
    return baraja

def main():
    """
    Programa principal que imprime la baraja española.

    """
    print(crear_baraja())
    
   

if __name__ == "__main__":
    main()
    
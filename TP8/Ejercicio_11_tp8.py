"""
    11.Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales 
    contiene, identificando la cantidad de cada una. Devolver un diccionario con los 
    resultados. Luego desarrollar un programa para leer una frase e invocar a la 
    función por cada palabra que contenga la misma. Imprimir las palabras y la 
    cantidad de vocales hallada. 
"""

def contar_vocales(palabra: str) -> dict:
    """
    Cuenta la cantidad de vocales de una palabra ingresada por el usuario.
    
    Pre:
        - palabra: string con la palabra a analizar.
    
    Post:
        - Devuelve un diccionario con las vocales como claves y la cantidad de cada una como valores.
    """
    vocales = "aeiou"
    
    contar_vocales = {"a": 0,
                      "e": 0,
                      "i": 0,
                      "o": 0,
                      "u": 0}
    
    for letra in palabra.lower():
        if letra in vocales:
            contar_vocales[letra] += 1
            
    return contar_vocales

def main() -> None:
    """
    Programa principal para procesar una frase y mostrar la cantidad de vocales
    de cada palabra.
    """
    try:
        frase = input("Ingrese una frase: ")
        palabras = frase.split()
        
        for palabra in palabras:
            resultado = contar_vocales(palabra)
            print(f"\nPalabra {palabra}")
            
            print("Vocales encontradas: ")
            for vocal, cantidad in resultado.items():
                print(f"  {vocal}: {cantidad}")
                
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    main()
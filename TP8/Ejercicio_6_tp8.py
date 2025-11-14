"""
    6. Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras 
    repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras 
    ordenadas según su longitud. Los signos de puntuación no deben afectar el 
    proceso.
"""

def procesar_palabra(frase: str) -> list:
    
    signos = ",;.:-_!\"'¡¿?()"
    
    for signo in signos:
        frase = frase.replace(signo, '')
        
    palabras = frase.lower().split()
    
    palabras_unicas = set(palabras)
    
    palabras_ordenadas = sorted(palabras_unicas, key= len)
    
    return palabras_ordenadas

def main() -> None:
    
    try:
        frase = input("Ingrese una frase: ")
        
        if not frase.strip():
            print("ERROR: La frase no puede estar vacia.")
            return
        resultado = procesar_palabra(frase)
        
        print("\nPalabras odenadas por longitud: ")
        
        for palabra in resultado:
            print(f"{palabra} ({len(palabra)} letras)")

            
    except Exception as e:
        print(f"ERROR: {e}")
        
if __name__ == "__main__":
    main()
        
"""
    7. Escribir un programa que juegue con el usuario a adivinar un número. El programa
    debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
    eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
    , se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
    el número. Si el usuario introduce algo que no sea un número se mostrará un
    mensaje en pantalla y se lo contará como un intento más.
"""

from random import randint

def jugar():
    """
    Juega a adivinar un número aleatorio entre 1 y 500.
    
    Precondición:
    
        - No se requieren parámetros de entrada.
        
    Postcondición:
    
        - El programa solicita al usuario que adivine un número.
        
        - Imprime si el número ingresado es mayor, menor o igual al número aleatorio.
        
        - Finaliza cuando el usuario adivina el número o ingresa -1 para salir.
        
        - Cuenta e imprime la cantidad de intentos realizados, incluyendo entradas no válidas.
    
    """
    num_random = randint(1, 500)
    intentos =  0
    
    while True:
        usuario = input("Tienes que adivinar el numero en un rango de 1 a 500 (-1 para salir): ")
        try:
            intento = int(usuario)
            
            if intento == -1:
                print("Saliendo...")
                break
            intentos +=1
            
            if intento < num_random:
                print("El numero a adivinar es mayor al numero ingresado :D")
            elif intento > num_random:
                print("El numero a adivinar es menor al numero ingresado D:")
            else:
                print(f"!FELICITACIONES ADIVINASTE!, en numero era {num_random} en {intentos} intento.")
                break
        except ValueError:
            intentos += 1
            print("ERROR, el valor ingresado no es valido. Intente nuevamente.")
            
def main()-> None:
    """
    Inicia el juego de adivinar un número.
    
    Precondición:
    
        - No se requieren parámetros de entrada.
        
    Postcondición:
    
        - Llama a la función `jugar()` para ejecutar la lógica del juego.
    
    """
    jugar()
    
if __name__ == "__main__":
    main()    
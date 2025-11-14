"""
    4. Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
    las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
    un programa para imprimir los números enteros entre 1 y 100000, y que solicite
    confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
    
"""
    
def imprimir_num():
    """
    
    Imprime los números enteros del 1 al 100000. Si se presiona Ctrl-C, solicita
    confirmación al usuario antes de detenerse.

    Pre: Ninguna.
    
    Post: Imprime números hasta 100000, salvo que el usuario confirme detenerse.
    
    """
    num = 1
    try:
        for num in range(num, 100001):
            print(num)
    except KeyboardInterrupt:
         try:
             usuario = input("\nSe detecto Ctrl-C. Desea detener el programa? (S/N): ").strip().lower()
             if usuario == "s":
                 print("El usuario detuvo el programa. ")
                 return
             else:
                print("Reanudando...")
                imprimir_num()
         except KeyboardInterrupt:
                print("\nSalida forzada. Programa finalizado.")
            
def main()-> None:
    """
     '
    Función principal, donde se ejecuta el programa.

    Esta función no recibe parámetros y no devuelve ningún valor.
    

    """
    
    imprimir_num()
    
if __name__ == "__main__":
    main()
         
         
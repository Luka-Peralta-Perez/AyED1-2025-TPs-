"""
    14.Se solicita crear un programa para leer direcciones de correo electrónico y verificar 
    si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que 
    una dirección sea considerada válida el nombre de usuario debe poseer solamente 
    caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe 
    tener al menos un carácter y tiene que finalizar con .com o .com.ar. 
"""
import re

def validar_correo(correo: str) -> bool:
    
    """
    Valida si una dirección de correo electrónico cumple con las condiciones especificadas.

    Precondiciones:
        - `correo` debe ser una cadena de texto no vacía.
        
    Postcondiciones:
        - Devuelve True si el correo cumple con el formato especificado:
            * Un solo carácter "@".
            * Solo caracteres alfanuméricos antes del "@".
            * Dominio válido que finaliza en ".com" o ".com.ar".
            
        - Devuelve False en caso contrario.
    """
    patron = r"^[a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+\.(com|com\.ar|edu\.ar)$"

    return bool(re.match(patron, correo))

def extraer_dominio(correo: str) -> str:
    
    """
    Extrae el dominio de un correo electrónico válido.

    Precondiciones:
        - `correo` debe ser una cadena válida con un único "@".
        
    Postcondiciones:
        - Devuelve el dominio después del "@".
        
    """
    return correo.split('@')[1]  # Se asume que el correo ya fue validado

def main():
    """
    Función principal que permite al usuario ingresar correos, validarlos y listar los dominios válidos.

    Precondiciones:
        - No se requiere ninguna entrada previa.
        
    Postcondiciones:
        - Solicita correos electrónicos y muestra dominios válidos únicos y ordenados alfabéticamente.
    """
    print("Verificador de correos electrónicos\n")
    dominios_validos = set()  # Usamos un conjunto para evitar duplicados

    while True:
        try:
            correo = input("Ingrese una dirección de correo electrónico (o cadena vacía para terminar): ").strip().lower()
            
            if correo == "":
                print("Saliendo...")
                break 
            
            if validar_correo(correo):
                print("La dirección de correo es válida.\n")
                dominio = extraer_dominio(correo)  
                dominios_validos.add(dominio)
            else:
                print("La dirección de correo NO es válida.\n")
        
        except Exception as e:
            print(f"Error inesperado: {e}")

    if dominios_validos:
        print("\nListado de dominios válidos:")
        for dominio in sorted(dominios_validos):
            print(dominio)
    else:
        print("\nNo se ingresaron correos válidos.")

if __name__ == "__main__":
    main()
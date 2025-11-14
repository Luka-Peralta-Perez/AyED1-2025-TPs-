"""
    3. Desarrollar un programa que utilice una función que reciba como parámetro una 
    cadena de caracteres conteniendo una dirección de correo electrónico y devuelva 
    una tupla con las distintas partes que componen dicha dirección. Ejemplo: 
    alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar 
    formatos de fecha inválidos y devolver una tupla vacía.
"""
import re

def validar_mail(mail: str) -> bool:
    """
    Valida si un correo electrónico tiene un formato válido.
    
    Pre:
        mail (str): cadena que contiene el correo a validar
    
    Post:
        bool: True si el formato es válido, False en caso contrario
    """
    patron = r"^[a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+\.(com|com\.ar|edu\.ar)$"
    return bool(re.match(patron, mail))  

def identificar_correo(mail: str) -> tuple:
    """
    Separa un correo electrónico en sus partes componentes.
    
    Pre:
        mail (str): cadena que contiene el correo a procesar.
    
    Post:
        tuple: - Si el mail es válido, retorna tupla con las partes del correo.
               - Si el mail es inválido, retorna tupla vacía.
    """
    try:
        if not validar_mail(mail):
            return tuple()
            
        nombre, dominio = mail.split('@')  
        dominios = dominio.split('.')     
        
        return (nombre, *dominios)
        
    except:
        return tuple()

def main():
    """
    Función principal que solicita al usuario ingresar un correo, 
    lo procesa y muestra el resultado.
    
    Pre:
        - No tiene precondiciones explícitas ya que solicita la entrada al usuario.
    
    Post:
        - Imprime en pantalla las partes del correo si es válido.
        - Si el correo es inválido, informa al usuario.
    """
    mail = input("Ingrese una dirección de correo: ")
    partes = identificar_correo(mail)
    
    if partes:
        print("Las partes del correo son:", partes)
    else:
        print("El correo ingresado es inválido")

if __name__ == "__main__":
    main()
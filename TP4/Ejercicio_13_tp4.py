"""
    13.Muchas aplicaciones financieras requieren que los números sean expresados tam
    bién en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento 
    cincuenta y tres". Escribir un programa que utilice una función para convertir un 
    número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría 
    la función si también aceptara números negativos? ¿Y números con decimales?
"""
def convertir_a_letras(num: int) -> str:
    """
    Convierte un número entero entre 0 y 1 billón a su representación en letras.

   
    """
    if num < 0:
        return "menos " + convertir_a_letras(-num)

    if num == 0:
        return "cero"

    # Diccionarios base
    unidades = {
        1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco",
        6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez",
        11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
        16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve"
    }

    decenas = {
        2: "veinte", 3: "treinta", 4: "cuarenta", 5: "cincuenta",
        6: "sesenta", 7: "setenta", 8: "ochenta", 9: "noventa"
    }

    centenas = {
        1: "ciento", 2: "doscientos", 3: "trescientos", 4: "cuatrocientos",
        5: "quinientos", 6: "seiscientos", 7: "setecientos", 8: "ochocientos",
        9: "novecientos"
    }

    def convertir_centenas(n: int) -> str:
        """Convierte números menores a 1000 en letras."""
        if n == 0:
            return ""
        elif n < 20:
            return unidades[n]
        elif n < 100:
            return decenas[n // 10] + (" y " + unidades[n % 10] if n % 10 != 0 else "")
        elif n == 100:
            return "cien"
        else:
            return centenas[n // 100] + (" " + convertir_centenas(n % 100) if n % 100 != 0 else "")

    def convertir_miles(n: int) -> str:
        """Convierte números menores a 1 millón."""
        if n < 1000:
            return convertir_centenas(n)
        else:
            miles = n // 1000
            resto = n % 1000
            if miles == 1:  # Caso especial para "mil"
                return "mil" + (" " + convertir_centenas(resto) if resto != 0 else "")
            else:
                return convertir_centenas(miles) + " mil" + (" " + convertir_centenas(resto) if resto != 0 else "")

    # Descomponer el número
    millones = num // 1_000_000
    miles = (num // 1_000) % 1_000
    resto = num % 1_000

    resultado = ""

    # Millones
    if millones > 0:
        if millones == 1:
            resultado += "un millón"
        else:
            resultado += convertir_miles(millones) + " millones"

    # Miles
    if miles > 0:
        resultado += (" " if resultado else "") + convertir_miles(miles)

    # Resto
    if resto > 0:
        resultado += (" " if resultado else "") + convertir_centenas(resto)

    return resultado.strip()


def main():
    """
    Programa principal para probar la conversión de números a letras.
    """
    while True:
        try:
            numero = int(input("Ingrese un número entero entre 0 y 1 billón: "))
            if 0 <= numero <= 1_000_000_000_000:
                resultado = convertir_a_letras(numero)
                print(f"{numero} en letras es: '{resultado}'")
                break
            else:
                print("El número debe estar entre 0 y 1 billón.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")


if __name__ == "__main__":
    main()


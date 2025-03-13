# DESARROLLO PRUEBA DE PROGRAMACIÓN
"""
* 3
* Crea un programa que analice una matriz 3x3 compuesta por "X" y "O"
* y retorne lo siguiente:
* - "X" si han ganado las "X"
* - "O" si han ganado los "O"
* - "Empate" si ha habido un empate
* - El arreglo de entrada puede ser escrito en el código y no como un input
* Nota: La matriz puede no estar totalmente cubierta.
* Se podría representar con un vacío "", por ejemplo.
*/

"""

def analizar_ganador(matriz):
    a = matriz[0]
    b = matriz[1]
    c = matriz[2]
    # Filas
    if a[0] == a[1] == a[2]:
        return a[0]
    if b[0] == b[1] == b[2]:
        return b[0]
    if c[0] == c[1] == c[2]:
        return c[0]
    # Columnas
    if a[0] == b[0] == c[0]:
        return a[0]
    if a[1] == b[1] == c[1]:
        return a[1]
    if a[2] == b[2] == c[2]:
        return a[2]
    # Diagonales
    if a[0] == b[1] == c[2]:
        return a[0]
    if a[2] == b[1] == c[0]:
        return a[2]
    return "Empate"

# DEFINICION DE FORMATO PARA ESTABLECER EL PARAMETRO PARA ANALIZAR
# matriz = [
#     ["X", "O", "X"],  # X O X
#     ["O", "X", "O"],  # O X O
#     ["X", "X", "O"]   # X X O
# ]
# print(analizar_ganador(matriz))  # X  (Ganador X)

# SE GENERA MARTRIZ DE EJEMPLO 
matriz = [
     ["X", "O", "X"],  # X O X
     ["O", "X", "O"],  # O X O
     ["X", "X", "O"]   # X X O
 ]
print(f"El ganador de la prueba es :{analizar_ganador(matriz)}")  # X  (Ganador X)

"""
* 2
* Crea un programa que calcule y retorne cuántos días hay entre dos cadenas
* de texto que representen fechas.
* - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
* - La función recibirá dos String y retornará un Int.
* - La diferencia en días será absoluta (no importa el orden de las fechas).
* - Si una de las dos cadenas de texto no representa una fecha correcta se
*   lanzará una excepción.
* - Las fechas de entrada pueden ser insertadas en el código directamente
*   sin necesidad de un input
*
"""
def cantidad_dias(fecha1, fecha2):
    from datetime import datetime
    fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
    fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")
    return abs((fecha2 - fecha1).days)

print("Desarrollo de pruebas entre fechas")
ejemplo1 = "01/01/2020"
ejemplo2 = "01/01/2021"

resultado = cantidad_dias(ejemplo1, ejemplo2)
print(f"El valor de dias entre fechas es de :{resultado}")
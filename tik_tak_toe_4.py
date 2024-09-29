import os
import random

# Inicializa la tabla de juego de 3x3 como una lista de listas, llenando cada celda con un número único.
table = [[None for x in range(1,4)] for y in range(1,4)]
table[0][0] = 1
table[0][1] = 2
table[0][2] = 3
table[1][0] = 4
table[1][1] = 5
table[1][2] = 6
table[2][0] = 7
table[2][1] = 8
table[2][2] = 9

# Lista que almacena los números de la tabla, más un 0 inicial.
number_tabla = [0, table[0][0], table[0][1], table[0][2], table[1][0], table[1][1], table[1][2], table[2][0], table[2][1], table[2][2]]

# Función para mostrar la tabla de juego en formato de Tic-Tac-Toe.
def tabla_juego_tikTakToe():
    print(f"""+-------+-------+-------+
|       |       |       |
|   {table[0][0]}   |   {table[1][0]}   |   {table[2][0]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {table[0][1]}   |   {table[1][1]}   |   {table[2][1]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {table[0][2]}   |   {table[1][2]}   |   {table[2][2]}   |
|       |       |       |
+-------+-------+-------+""")
    #print(number_tabla)

# Elimina un número de `number_tabla` una vez que ha sido seleccionado.
def elemento_eliminar(numero_delete):
    for item in number_tabla:
        if item == numero_delete:
            number_tabla.remove(numero_delete)

# Obtiene un número aleatorio de la lista de números disponibles para la IA (excepto el 0).
def obtener_item_lista():
    while True:
        numero_IA = random.choice(number_tabla)
        if numero_IA != 0:
            return numero_IA

# Obtiene un número ingresado por el usuario que debe estar disponible en la tabla.  
def obtener_numero_consola():
    while True:
        number_con = int(input("Ingresar un numero : "))
        if number_con in number_tabla and number_con != 0:
            return number_con
        else:
            print("Ingresar un numero disponible")

# Actualiza la tabla al final del juego mostrando la combinación ganadora, marcando las posiciones con el símbolo del jugador ('X' o 'O').
def tabla_juego_finalizado_II(num1, num2, num3, num4, num5, num6, sim):
    # Limpia la tabla llenando con guiones '-'.
    for colum in range(3):
        for item in range(3):
            table[colum][item] = '-'

    # Coloca los símbolos del ganador en las posiciones correctas.
    table[num1][num2] = sim
    table[num3][num4] = sim
    table[num5][num6] = sim

    #print(table)
    os.system("cls")
    tabla_juego_tikTakToe()


# Comprueba si hay un ganador revisando todas las posibles combinaciones ganadoras (filas, columnas y diagonales).    
def comprobar_juego():
    #Comprobar juego horizontal
    if table[0][0] == 'X' and table[0][1] == 'X' and table[0][2] == 'X':
        tabla_juego_finalizado_II(0, 0, 0, 1, 0, 2, 'X')
        return False
    elif table[0][0] == 'O' and table[0][1] == 'O' and table[0][2] == 'O':
        tabla_juego_finalizado_II(0, 0, 0, 1, 0, 2, 'O')
        return True
    elif table[1][0] == 'X' and table[1][1] == 'X' and table[1][2] == 'X':
        tabla_juego_finalizado_II(1, 0, 1, 1, 1, 2, 'X')
        return False
    elif table[1][0] == 'O' and table[1][1] == 'O' and table[1][2] == 'O':
        tabla_juego_finalizado_II(1, 0, 1, 1, 1, 2, 'O')
        return True
    elif table[2][0] == 'X' and table[2][1] == 'X' and table[2][2] == 'X':
        tabla_juego_finalizado_II(2, 0, 2, 1, 2, 2, 'X')
        return False
    elif table[2][0] == 'O' and table[2][1] == 'O' and table[2][2] == 'O':
        tabla_juego_finalizado_II(2, 0, 2, 1, 2, 2, 'O')
        return True
    
    #comprobar juego horizontal
    elif table[0][0] == 'X' and table[1][0] == 'X' and table[2][0] == 'X':
        tabla_juego_finalizado_II(0, 0, 1, 0, 2, 0, 'X')
        return False
    elif table[0][0] == 'O' and table[1][0] == 'O' and table[2][0] == 'O':
        tabla_juego_finalizado_II(0, 0, 1, 0, 2, 0, 'O')
        return True
    elif table[0][1] == 'X' and table[1][1] == 'X' and table[2][1] == 'X':
        tabla_juego_finalizado_II(0, 1, 1, 1, 2, 1, 'X')
        return False
    elif table[0][1] == 'O' and table[1][1] == 'O' and table[2][1] == 'O':
        tabla_juego_finalizado_II(0, 1, 1, 1, 2, 1, 'O')
        return True
    elif table[0][2] == 'X' and table[1][2] == 'X' and table[2][2] == 'X':
        tabla_juego_finalizado_II(0, 2, 1, 2, 2, 2, 'X')
        return False
    elif table[0][2] == 'O' and table[1][2] == 'O' and table[2][2] == 'O':
        tabla_juego_finalizado_II(0, 2, 1, 2, 2, 2, 'O')
        return True
    
    #Comprobar juego diagonal
    elif table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X':
        tabla_juego_finalizado_II(0, 0, 1, 1, 2, 2, 'X')
        return False
    elif table[0][0] == 'O' and table[1][1] == 'O' and table[2][2] == 'O':
        tabla_juego_finalizado_II(0, 0, 1, 1, 2, 2, 'O')
        return True
    elif table[2][0] == 'X' and table[1][1] == 'X' and table[0][2] == 'X':
        tabla_juego_finalizado_II(2, 0, 1, 1, 0, 2, 'X')
        return False
    elif table[2][0] == 'O' and table[1][1] == 'O' and table[0][2] == 'O':
        tabla_juego_finalizado_II(2, 0, 1, 1, 0, 2, 'O')
        return True

# Bucle principal del juego Tic-Tac-Toe.
while True:
    os.system("cls") # Limpia la consola para una visualización limpia.
    tabla_juego_tikTakToe() # Muestra la tabla actualizada.

    if comprobar_juego() == True: #Comprueba el juego
        print("+-----------------------+")
        print("|       Haz ganado      |")
        print("+-----------------------+")
        break
    elif comprobar_juego() == False:
        print("+-----------------------+")
        print("|       Haz perdido     |")
        print("+-----------------------+")
        break

    number = obtener_numero_consola()

    # Turno del jugador: obtiene un número de la consola y actualiza la tabla.
    for colum in range(3):
        for item in range(3):
            if table[colum][item] == number: 
                table[colum][item] = 'O'
                elemento_eliminar(number)
                #print("Turno completado (jugador)")

    # Comprueba nuevamente si el jugador ha ganado después de su turno.
    if comprobar_juego() == True: 
        print("+-----------------------+")
        print("|       Haz ganado      |")
        print("+-----------------------+")
        break
    elif comprobar_juego() == False:
        print("+-----------------------+")
        print("|       Haz perdido     |")
        print("+-----------------------+")
        break

    # Comprueba si la tabla está vacía para finalizar el juego.
    if len(number_tabla) == 1: 
        print("+-----------------------+")
        print("|    Juego Finalizado   |")
        print("+-----------------------+")
        break

    # Turno de la IA: selecciona un número aleatorio y lo coloca en la tabla.
    numero_IA = obtener_item_lista()
    for colum in range(3):
        for item in range(3):
            if table[colum][item] == numero_IA:
                table[colum][item] = 'X'
                elemento_eliminar(numero_IA)
                #print(f"Turno completado (IA) {numero_IA}")

print("Fin del programa")
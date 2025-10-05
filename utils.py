import numpy as np
from numpy import random

# CREAR TABLERO
# asumimos que el tablero siempre sera cuadrado
def crear_tablero(n=10):
    tablero = np.full((n,n), "_")
    #print(tablero)
    return tablero


# CREAR BARCO (SIN VALIDAR)
def crear_barco_sin_validar(tablero, eslora):
    #print("Crear barco con", eslora, "esloras")
    # eslora es la cantidad de tuplas (x,y) que debera crear
    barco = []
    #print(barco)
    pos_inicial = (np.random.randint(tablero.shape[0]-1), np.random.randint(tablero.shape[0]-1))
    #print("Posicion inicial:", pos_inicial)
    barco.append(pos_inicial)
    #print(barco)
    valores = ("N","S","E","O")
    orientacion = np.random.choice(valores)
    #print("Con orientacion:", orientacion)
    
    for i in range(eslora-1):
        # para que el barco se cree horizontalmente (igual numero de fila) o verticalmente (igual numero de columna)
        fila = pos_inicial[0]
        columna = pos_inicial[1]    
        
        if orientacion == "N":
            pos_sig = (fila-1,columna) 
        elif orientacion == "S":
            pos_sig = (fila+1,columna)
        elif orientacion == "E":
            pos_sig = (fila,columna+1)
        elif orientacion == "O":
            pos_sig = (fila,columna-1)

        barco.append(pos_sig)
        pos_inicial = pos_sig

    return barco

# VALIDAR BARCO
def validacion(barco, tablero):
        
        tam_tablero = tuple(range(tablero.shape[0]))
        for x in barco:
            # validacion para que el barco este dentro del tablero
            if x[0] not in tam_tablero or x[1] not in tam_tablero:
                #print("Fuera del tablero")
                return False

            # validacion para que no cree un barco donde ya existe otro barco
            if tablero[x] == "O" or tablero[x] == "X":
                #print("Ya existe un barco en la posicion", x)
                return False
            
        return True

# COLOCAR UN BARCO
def colocar_barco(barco, tablero):
    #print("Barco a colocar")
    #print(barco)
    for i in barco:
        #print(i)
        tablero[i] = "O"

# COLOCAR TODOS LOS BARCOS
def colocar_barcos(tablero, eslora, cantidad):
    # coloca en el tablero los barcos generados de forma aleatoria segun eslora y cantidad
    c = 0
    while c < cantidad:
        barco = crear_barco_sin_validar(tablero, eslora)
        #print(barco)
        valida = validacion(barco,tablero)
        #print("Valido: ", valida)
        if valida == True:
            colocar_barco(barco, tablero)
            c += 1


# RECIBIR/EJECUTAR DISPARO
def recibir_disparo(tablero, coordenada, tablero_disparos):

     print("Disparo: ", coordenada)
     x = tablero[coordenada]
     #print("Lo que hay en la celda a la que se disparo:", x)

     if x == "O":
          tablero_disparos[coordenada] = "X"
          tablero[coordenada] = "X"
          print("Tocado! Va otra vez")
          return True
     elif x == "_":
          tablero_disparos[coordenada] = "A"
          print("Agua")
          return False
     elif x == "X" or x =="A":
          print("Ya ha disparado aqui. Prueba de nuevo")
          return True

def menu():
    print("-----------MENU-----------")    
    print("Escoge lo que quieres hacer:")
    print("1. Ver mi tablero: 'mt'")
    print("2. Ver tablero maquina: 'tm'")
    print("3. Salir: 'salir'")
    print("--------------------------")
    print("Introduce una coordenada en formato 'fila.columna':")
    return input()

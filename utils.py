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

# INTRODUCIR COORDENADAS
def introducir_coordenada(tablero_maquina):
    print("Introduce una coordenada en formato 'fila.columna':")
    while True:
        x = input()
        fil_col = x.split(".")
        try: 
            coord = []
            for e in fil_col:
                coord.append(int(e))
            coord = tuple(coord)

            tam_tablero = tuple(range(tablero_maquina.shape[0]))

            if coord[0] in tam_tablero and coord[1] in tam_tablero:
                return coord
            else:
                print("Coordenada no válida. Vuelve a ingresarla.")
        except Exception:
            print("Formato no válido. Vuelve a ingresar la coordenada.")

def menu():
    print("-----------MENU-----------")    
    print("Escoge lo que quieres hacer:")
    print("1. Ver mi tablero: 'mt'")
    print("2. Ver tablero maquina: 'tm'")
    print("3. Disparar: 'dis'")
    print("4. Salir: 'salir'")
    return input()

def juego():
    print("-----JUGANDO-----")
    print("Seguir jugando? (y/n)")  
    print("Volver al menu: 'm'")
    return input()

'''
def jugar(): 

    # Si disparo yo
    # Llamo a la funcion para disparar al tablero de la maquina

    tocado = True
    while tocado == True:
        coordenada = introducir_coordenada(tablero_maquina)
        tocado = recibir_disparo(tablero_maquina, coordenada, tablero_maquina_disparos)

    print("Como veo el tablero de la maquina luego de mi disparo")
    print(tablero_maquina_disparos)
    print()
    # Si dispara la maquina
    # Llamo a la funcion para disparar a mi tablero
    tocado = True
    while tocado == True:
        coordenada = tuple(map(int, random.randint(mi_tablero.shape[0], size = 2)))
        print("Dispara la maquina")
        tocado = recibir_disparo(mi_tablero, coordenada, mi_tablero_disparos)
    print("Como ve la maquina mi tablero luego de su disparo")
    print(mi_tablero_disparos)

'''


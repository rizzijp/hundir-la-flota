import numpy as np
from numpy import random
import utils as f
import time

# main
print("----- HUNDIR LA FLOTA -----")

# INICIALIZAR JUEGO
# Llamo a la funcion crear_tablero para crear mi tablero y el de la maquina
mi_tablero = f.crear_tablero()
tablero_maquina = f.crear_tablero()
# Creo los tableros para tener las vistas de los disparos
mi_tablero_disparos = f.crear_tablero()
tablero_maquina_disparos = f.crear_tablero()

# Llamo a la funcion colocar_barcos para colocar los barcos en mi tablero
# 3 barcos de eslora = 2
f.colocar_barcos(mi_tablero, 2, 3)
# 2 barcos de eslora = 3
f.colocar_barcos(mi_tablero, 3, 2)
# 1 barco de eslora = 4
f.colocar_barcos(mi_tablero, 4, 1)
#print("Mi tablero")
#print(mi_tablero)

# Llamo a la funcion colocar_barcos para colocar los barcos en el tablero de la maquina
# 3 barcos de eslora = 2
f.colocar_barcos(tablero_maquina, 2, 3)
# 2 barcos de eslora = 3
f.colocar_barcos(tablero_maquina, 3, 2)
# 1 barco de eslora = 4
f.colocar_barcos(tablero_maquina, 4, 1)
#print("Tablero maquina")
#print(tablero_maquina)

coordenada = f.menu()
while coordenada.lower() != "salir":
    if coordenada.lower() == "mt":
        print("Tu tablero:")
        print(mi_tablero)
        coordenada = f.menu()
    elif coordenada.lower() == "tm":
        print("Tablero maquina:")
        print(tablero_maquina_disparos)
        coordenada = f.menu()
    else:
        # Disparo yo
        tocado = True
        while tocado == True:
            while True:
                fil_col = coordenada.split(".")
                try: 
                    coord = []
                    for e in fil_col:
                        coord.append(int(e))
                    coord = tuple(coord)

                    tam_tablero = tuple(range(tablero_maquina.shape[0]))

                    if coord[0] in tam_tablero and coord[1] in tam_tablero:
                        break
                    else:
                        print("Coordenada no válida. Vuelve a ingresarla.")
                        coordenada = input()
                except Exception:
                    print("Formato no válido. Vuelve a ingresar la coordenada.")
                    coordenada = input()

            # Llamo a la funcion para disparar al tablero de la maquina
            tocado = f.recibir_disparo(tablero_maquina, coord, tablero_maquina_disparos)
            #print("Tablero maquina")
            print(tablero_maquina_disparos)
            print()
            # Si es tocado, va de nuevo
            if tocado == True:
                print("Introduce una coordenada en formato 'fila.columna':")
                coordenada = input()

        # Dispara la maquina
        # Llamo a la funcion para disparar a mi tablero
        tocado = True
        while tocado == True:
            # Espero 1 segundo para el siguiente disparo
            time.sleep(1)
            coordenada_rdm = tuple(map(int, random.randint(mi_tablero.shape[0], size = 2)))
            print("Dispara la maquina")
            tocado = f.recibir_disparo(mi_tablero, coordenada_rdm, mi_tablero_disparos)
        #print("Como ve la maquina mi tablero luego de su disparo")
        #print(mi_tablero_disparos)
        #print()
        coordenada = f.menu()
else:
    print("Hasta la próxima!")

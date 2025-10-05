import numpy as np
from numpy import random
import utils as f
import time

# main
print("-Hundir la flota-\n¿Listo para jugar? (y/n)")
respuesta = input()
while respuesta.lower() != "y" and respuesta.lower() != "n":
    print("String no válido, vuelve a ingresarlo.")
    respuesta = input("y/n")

if respuesta.lower() == "n":
    print("Vale, hasta luego.")
elif respuesta.lower() == "y":
    print("A por ello.")
    # INICIALIZAR JUEGO
    # Llamo a la funcion crear_tablero para crear mi tablero y el de la maquina
    mi_tablero = f.crear_tablero()
    tablero_maquina = f.crear_tablero()
    # Creo los tableros para tener las vistas de los disparos
    mi_tablero_disparos = f.crear_tablero()
    tablero_maquina_disparos = f.crear_tablero()

    # Llamo a la funcion colocar_barcos para colocar los barcos en mi tablero
    # 3 barcos de eslora = 2
    #print("Barcos con 2 esloras")
    f.colocar_barcos(mi_tablero, 2, 3)
    # 2 barcos de eslora = 3
    #print("Barcos con 3 esloras")
    f.colocar_barcos(mi_tablero, 3, 2)
    # 1 barco de eslora = 4
    #print("Barcos con 4 esloras")
    f.colocar_barcos(mi_tablero, 4, 1)
    # imprime tablero con los barcos colocados
    #print("Mi tablero")
    #print(mi_tablero)

    # Llamo a la funcion para colocar los barcos en el tablero de la maquina
    # 3 barcos de eslora = 2
    #print("Barcos con 2 esloras")
    f.colocar_barcos(tablero_maquina, 2, 3)
    # 2 barcos de eslora = 3
    #print("Barcos con 3 esloras")
    f.colocar_barcos(tablero_maquina, 3, 2)
    # 1 barco de eslora = 4
    #print("Barcos con 4 esloras")
    f.colocar_barcos(tablero_maquina, 4, 1)
    # imprime tablero con los barcos colocados
    #print("Tablero maquina")
    #print(tablero_maquina)

    # MUESTRO MENU
    opcion = f.menu()

    while opcion.lower() != "mt" and opcion.lower() != "tm" and opcion.lower() != "salir" and opcion.lower() != "dis":
        print("String no válido, vuelve a ingresarlo.")
        opcion = input()
    
    while opcion.lower() != "salir":
        if opcion.lower() == "mt":
            print("Tu tablero:")
            print(mi_tablero)
            opcion= f.menu()
        elif opcion.lower() == "tm":
            print("Tablero maquina:")
            print(tablero_maquina_disparos)
            opcion = f.menu()
        elif opcion.lower() == "dis":
            
            # JUEGO
            # Disparo yo
            # Llamo a la funcion para disparar al tablero de la maquina

            tocado = True
            while tocado == True:
                coordenada = f.introducir_coordenada(tablero_maquina)
                tocado = f.recibir_disparo(tablero_maquina, coordenada, tablero_maquina_disparos)
                #print("Tablero maquina")
                print(tablero_maquina_disparos)
                print()

            # Dispara la maquina
            # Llamo a la funcion para disparar a mi tablero
            tocado = True
            while tocado == True:
                # Espero 2 segundos para el siguiente disparo
                time.sleep(2)
                coordenada = tuple(map(int, random.randint(mi_tablero.shape[0], size = 2)))
                print("Dispara la maquina")
                tocado = f.recibir_disparo(mi_tablero, coordenada, mi_tablero_disparos)
            #print("Como ve la maquina mi tablero luego de su disparo")
            #print(mi_tablero_disparos)
            #print()

            while True:
                opcion = f.juego()
                if opcion.lower() == "y":
                
                    # JUEGO
                    # Disparo yo
                    # Llamo a la funcion para disparar al tablero de la maquina
                    tocado = True
                    while tocado == True:
                        coordenada = f.introducir_coordenada(tablero_maquina)
                        tocado = f.recibir_disparo(tablero_maquina, coordenada, tablero_maquina_disparos)
                        #print("Tablero maquina")
                        print(tablero_maquina_disparos)
                        print()

                    # Dispara la maquina
                    # Llamo a la funcion para disparar a mi tablero
                    tocado = True
                    while tocado == True:
                        # Espero 2 segundos para el siguiente disparo
                        time.sleep(2)
                        coordenada = tuple(map(int, random.randint(mi_tablero.shape[0], size = 2)))
                        print("Dispara la maquina")
                        tocado = f.recibir_disparo(mi_tablero, coordenada, mi_tablero_disparos)
                    #print("Como ve la maquina mi tablero luego de su disparo")
                    #print(mi_tablero_disparos)
                    #print()

                elif opcion.lower() == "m":
                    opcion = f.menu()
                    break
                elif opcion.lower() == "n":
                    opcion = "salir"
                    break
                else:
                    print("Opción no válida, vuelve a ingresarla.")


    if opcion.lower() == "salir":
        print("Hasta la próxima")

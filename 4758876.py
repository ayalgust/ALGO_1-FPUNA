"""
− Algoritmos 1
− Individual
− Gustavo Jesús Ayala Marin 4758876
− ITAREA 2 – Arreglos multidimensionales
"""
from Matriz import creamat, leemat, imprimat
import random
"""Se definen datos y parametros del problema"""
FIL=5
COL=6
G=5
Q=15
"""Creamos la matriz TIRIK"""
TIRIK = creamat(FIL,COL)
"""Asiganamos valores para el orden de TIRIK que leugo usaremos para cargar los casilleros de cantidad de carne"""
M = len(TIRIK)
N = len(TIRIK[0])
"""Generamos un Valor aleatorio y lo guardamos para definir la guarida en un lugar inicial
aleatorio"""
fil_ini = random.randint(0, M - 1)
col_ini = random.randint(0, N - 1)
"""Creamos la función que carga la cantidad de carne en cada cacillero"""
def carne_rand (MATRIZ):
    for I in range(M):
        for J in range(N):
            MATRIZ[I][J] = random.randint(0,G)
    MATRIZ[fil_ini][col_ini] = '*'
    return MATRIZ
"""Creamos la función del recorrido de Tirika"""
def recorrido_tirik (MATRIZ):
    peso_tirik = 0 #Creamos un contador para el peso de Tirika
    """Creamos variables para actualizar la posición de tirika 
    una vez que dejó la guarida"""
    fil_act = fil_ini
    col_act = col_ini
    while peso_tirik < Q: #iteramos según la condición del peso de tirika
        valor_mayor = 0
        pos_mayor = 0
        for i in range (fil_act-1,fil_act+2):
            for j in range (col_act-1,col_act+2):
                """ Ahora fijamos el recorrido solamente dentro de la matriz según el 
                Orden de la matriz"""
                if i in range (0,M) and j in range (0,N):
                    if MATRIZ[i][j] == '*': #Si el valor de la posición es * se ignora
                        continue
                    if MATRIZ[i][j] == '&': # Si el valos de la posición es & se actualiza a 0
                        MATRIZ[fil_act][col_act] = 0
                    if MATRIZ[i][j] > valor_mayor: # Comparamos nuestros valores para buscar el mayor
                        valor_mayor = MATRIZ[i][j]
                        pos_mayor = [i,j] #Guardamos la posición del Mayor Valor
        MATRIZ[pos_mayor[0]][pos_mayor[1]] = '&' # Actualizamos la posición de Tirika
        fil_act = pos_mayor[0]
        col_act = pos_mayor[1] #fijamos la nueva posición de tirika para el recorrido siguiente
        peso_tirik += valor_mayor #actualizamos el peso de Tirika
        print('--------------------------')
        imprimat(MATRIZ)
    print(f'TIRIKA ESTA LLENO EN LA POSICIÓN TIRIK[{fil_act}][{col_act}]')
    return MATRIZ
carne_rand(TIRIK)
imprimat(TIRIK)
recorrido_tirik(TIRIK)

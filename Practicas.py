from Matriz import leemat, creamat, imprimat
import random
# Solicitamos al usuario ingresar las filas y columnas
fil = int(input('Favor ingrese nro de filas: '))
col = int(input('Favor ingrese nro de columnas: '))
#validamos los datos ingresados
while fil <= 0 or col <= 0:
    print(f'La fila o columans no pueden ser menores o igual a 0')
    fil = int(input('Favor ingrese nro de filas: '))
    col = int(input('Favor ingrese nro de columnas: '))
#creamos la matriz
matrix = creamat(fil,col)
#Creamos la funcion para cargar la matriz con nros aleatorios
def random_mat(MATRIZ):
    for I in range(fil):
        for J in range(col):
            MATRIZ[I][J] = random.randint(0,20)
#creamos la funcion para sumar cada columna de la matriz
def List_sum_col(MATRIZ):
    sumcol = []
    for j in range(col):
        sum_aux = 0
        for k in range(fil):
            sum_aux += MATRIZ[k][j]
        sumcol.append(sum_aux)
    print(sumcol)
#llamamos a las funciones
print(f'La matriz generada es:')
random_mat(matrix)
imprimat(matrix)
print("-----------------------")
print(f'La suma en cada columna es:')
List_sum_col(matrix)
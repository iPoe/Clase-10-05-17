Hamburguesas = [['EMCALI', 72000, 81000, 12, 5],
             ['GASES DE OCCIDENTE', 14534, 13920, 11, 4],
             ['CLARO', 31000, 31000, 10, 5],
             ['MOVISTAR', 61320, 64300, 11, 6],
             ['DICEL', 79000, 62000, 9, 3]]

def facturasEncarecidas(servicios):
    """
    Descripcion: Funcion que retorna las empresas
    cuya factura se ha encarecido y la diferencia.
    Entrada: La matriz de servicios
    Salida: La matriz con los datos solicitados
    """
    nuevaLista = []
    for sublista in servicios:
        if(sublista[1] < sublista[2]):
            nuevaLista.append([sublista[0], sublista[2]-sublista[1]])

    return nuevaLista

def actualizarMatriz(servicios):
    """
    """
    empresa = eval(input("Ingrese el nombre de la empresa: "))
    mesAnterior = eval(input("Ingrese el valor del mes anterior: "))
    mesActual = eval(input("Ingrese el valor del mes actual: "))
    mes = eval(input("Ingrese el numero correspondiente al mes actual: "))
    estrato = eval(input("Ingrese el numero del estrato: "))

    estaEsta = False
    for sublista in servicios:
        if(empresa == sublista[0] and mes == sublista[3]):
            sublista[1] = mesAnterior
            sublista[2] = mesActual
            sublista[4] = estrato
            estaEsta = True

    if(estaEsta == False):
        servicios.append([empresa,mesAnterior,mesActual,mes,estrato])

    return servicios


Mesas = [[2, 0, 4, 7],
         [1, 3, 0, 0],
         [9, 10, 10, 5]]


def asignar(butacos, cp):
    """
    """
    fila = 0
    while(fila < len(butacos)):
        columna = 0
        while(columna < len(butacos[fila])):
            if(butacos[fila][columna] + cp <= 10):
                print("Fila: " + str(fila))
                print("Columna: " + str(columna))
                butacos[fila][columna] = butacos[fila][columna] + cp
                columna = len(butacos[fila])-1
                fila = len(butacos)-1
            columna = columna + 1
        fila = fila + 1
    




















            

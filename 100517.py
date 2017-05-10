## Parcial

servicios = [['EMCALI', 72000, 81000, 12, 5],
    ['GASES DE OCCIDENTE', 14534, 13920, 11, 4],
    ['CLARO', 31000, 31000, 10, 5],
    ['MOVISTAR', 61320, 64300, 11, 6],
    ['DICEL', 79000, 62000, 9, 3]]



def facturasencarecidas(servicios):
    """
    """
    nuevalista= []
    for sublista in servicios:
        if(sublista[1] < sublista[2]):
            nuevaLista.append([sublista[0], sublista[2]-sublista[1]])
            
    return nuevalista


def Actualizarmatriz(servicios):
    """
    """


    
    empresa = eval(input("Ingrese el nombre de la empresa: "))
    mesanterior = eval(input("Ingrese el valor del mes anterior: "))
    mesactual = eval(input("Ingrese el valor del mes actual: "))
    mes = eval(input("Ingrese el numero del mes actual: "))
    estrato = eval(input("Ingrese el numero del estrato: "))

    yaesta = False

    for sublista in servicios:
        if(empresa == sublista[0] and mes == sublista[3]):
            sublista[1] = mesanterior
            sublista[2] = mesactual
            sublista[4] = estrato
            yaesta = True

    if(yaesta == False):
        servicios.append([empresa,mesanterior,mesactual,mes,estrato])

    return servicios

Actualizarmatriz()
    
            













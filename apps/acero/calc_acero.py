from itertools import combinations_with_replacement as cwr
import numpy as np

# funcion para extraer listas de barras y de areas
def acero(a, b):
    aa = [4, 5, 6]
    bb = [5, 6, 7]
    cc = [6, 7, 8]
    dd = [7, 8, 9]
    ee = [8, 9, 10]
    ff = [9, 10, 11]
    gg = [10, 11, 14]
    hh = [11, 14, 18]

    # funcion para la permutacion donde (x= espacios)
    def ab(x):
        nb = list(cwr(aa, x)) + list(cwr(bb, x)) + list(cwr(cc, x)) + list(cwr(dd, x)) + list(cwr(ee, x)) + list(cwr(ff, x)) + list(cwr(gg, x)) + list(cwr(hh, x))
        nb = list(dict.fromkeys(nb))
        return nb

    pi = 3.141592653589793
    
    nd = [(4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (14, 14), (18, 18), ]
    ne = []

    # bucle para las cantidades de barras
    # donde se hallan las combinaciones y las areas
    for n in range((a+1), (b+1)):
        nd.extend(ab(n))
    for i in range(len(nd)):
        nc = 0
        for j in range(len(nd[i])):
            nc = nc + (pi/4) * (nd[i][j]*2.54/8)**2
        ne.append(nc)
    return nd, ne
#ne: areas [1]
#nd: barras [0]

#lista areas y lista barras
'''
areas = acero(a, b)[1]
barras = acero(a, b)[0]
'''

#acero para COLUMNA CORTA
def _acero_col(a):
    bar = []
    li = [4, 5, 6, 7, 8, 9, 10, 11, 14, 18]
    for j in range(10):
        nb = []
        for i in range(a):
            nb.append(li[j])
        bar.append(nb)
    pi = 3.141592653589793
    are = []
    for j in range(10):
        nc = 0
        for h in bar[j]:
            nc = nc + (pi/4) * (h*2.54/8)**2
        are.append(nc)
    return bar, are

#acero para COLUMNA en modulo ACERO Optimo
def _as_col(min, max):
    bar = []
    are = []
    for i in range(min, (max+1), 2):
        for j in _acero_col(i)[0]:
            bar.append(j)
        for j in _acero_col(i)[1]:
            are.append(j)
    return bar, are


#funcion para valores mayores al asc
# copiar y pegar donde se necesite
def filtro(asc, areas):
    def ac (n):
        if (n >= asc):
            return True
        else:
            return False
    ass = list(filter(ac, areas))
    return ass

#lista areas filtrada y area optima
'''
areasFiltr = filtro(asc, areas)
ass = min(areasFiltr)
'''

#barra optima
'''
bar = barras[areas.index(ass)]
'''

#acero sumunistrado manual
#barras
def _bar(string):
    if (string == ''):
        return None
    else:
        li = list(string.split(", "))
        lo = []
        for i in li:
            i = int(i)
            lo.append(i)       
        return lo
#areas
def _ass(a):
    nc = 0
    pi = 3.141592653589793
    for i in a:
        nc = nc + (pi/4)*(i*2.54/8)**2 
    return nc

#reorganizacion de barras
def _org_bar(bar):
    l = []
    for i in range(len(bar)):
        if i%2 == 0:
            l.insert(0, bar[i])
        else:
            l.append(bar[i])
    return l

''' ------- SEGUNDA PARTE : SEPARACION -------- '''

# diametro Máximo de las barras longitudinales
def _dB(bar):
    dB = max(bar)
    return dB

#PERFECTO
# diametro de estribo segun barras long
# dB: diametro maximo
def _est(dB):
    if (dB <= 10):
        est = 3
    else:
        est = 4
    return est

#PERFECTO
#separacion VIGAS
def _dbar(a):
    d = 0
    for i in a:
        d = d + i*2.54/8
    return d

def  _sep(a, b, rec, est, dbar):
    sep = (b-(2*rec)-(2*2.54*est/8)-dbar)/(len(a)-1)
    return sep

def _sep_vig(sep, dB, agg):
    if (sep < dB*2.54/8) or (sep < 2.5) or (sep < agg*2.54*4/3):
        separ = False
    else:
        separ = True
    return separ

#separacion COLUMNAS CORTAS
def _dbar_col(dB, nxy):
    d = nxy*dB*2.54/8
    return d

def  _sep_col(nxy, b, rec, est, dbar):
    sep = (b-(2*rec)-(2*2.54*est/8)-dbar)/(nxy-1)
    return sep

def _comp_s_col(sep, dB, agg):
    if (sep < 1.5*dB*2.54/8) or (sep < 4) or (sep < agg*2.54*4/3):
        separ = False
    else:
        separ = True
    return separ


#PERFECTO
import math

#Valor de (numero máximo de barras) segun el asc
def nmax(asc):
    r= math.ceil(asc/1.2667686977437442)
    return r


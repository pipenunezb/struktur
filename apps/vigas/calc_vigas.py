from itertools import combinations_with_replacement
import numpy as np

'''
#Datos de entrada
#1.1
CD = float(input())
CL = float(input())

#1.2
Wu = float(input())

#2
apoyo = input()
L = float(input())

#3.1
fc = int(input())
fy = int(input())
phi = float(input())
b = float(input())
d = float(input())

#8
ec = float(input())
'''

# PASOS PARA SOLUCION DE VIGAS

# 1. (CD y CL) o (Wu)
# 1.1 CD y CL
def CD_CL(CD, CL):
    Wu = (CD*1.2)+(CL*1.6)
    return Wu

def _FS(Wu, CD, CL, phi):
    FS = (Wu/(CD+CL))/phi
    return FS

# 1.2 Wu

# 2. Mu
'''if (apoyo=="voladizo"):
    AP = 1/8
elif (apoyo=="simplemente apoyado"):
    AP = 1/16
elif (apoyo=="un extremo continuo"):
    AP = 1/18.5
elif (apoyo=="ambos extremos continuos"):
    AP = 1/21
else:
    print("definir tipo de apoyo")'''

def _Mu(Wu, L, AP):
    Mu = (Wu*L*L)/AP
    return Mu

# 3. Cuantia (formula o tabla)

# 3.1 formula
def _ku(Mu, b, d):
    ku = Mu*100000/(b*d*d)
    return ku

def _cuantia(fc, fy, phi, ku):
    cuantia = ((0.85*fc)/fy)*(1-(1-((2*ku)/(phi*0.85*fc)))**0.5)
    return cuantia


# 3.2 tabla



# 4. Acero
def _asc(cuantia, b, d):
    asc = cuantia*b*d
    return asc
    
# recalcular d
def _y(bar, est, rec):
    y = 0
    z = 0
    pi = 3.1415926536
    for i in bar:
        y = y + ((i*2.54/8)/2)*(pi/4)*(i*2.54/8)**2
        z = z + (pi/4)*(i*2.54/8)**2
    e = est*2.54/8
    ans = (y/z) + e + rec
    return ans

# comprobaciones de area

def _comp_area(asc, ass):
    if (asc > ass):
        comp_area = "NO CUMPLE"
    else:
        comp_area = "CUMPLE"
    return comp_area

# comprobaciones de separacion



# 5. a
def _a(ass, fy, fc, b):
    a = ass*fy/(0.85*fc*b)
    return a

# 6. B1
def _B1(fc):
    if (fc<170):
        B1 = "Introducir un valor de f'c mayor o igual a 170"
    elif (fc<280):
        B1 = 0.85
    elif (fc<560):
        B1 = 0.85-(0.05/70)*(fc-280)
    else:
        B1 = 0.65
    return B1

# 7. c
def _c(a, B1):
    c = a/B1
    return c

# 8. es
def _es(ec, c, d):
    es = (ec/c)*(d-c)
    return es

# comprobacion de fluencia
def _comp_fluen(es):
    if (es<0.005):
        comp_fluen = "El Acero NO fluye"
    else:
        comp_fluen = "El Acero Fluye"
    return comp_fluen

# 9. recalcular phi
def _phi(es):
    if (es<0.002):
        phi = 0.65
    elif (es<0.005):
        phi = 0.65+(es-0.002)*(250/3)
    else:
        phi = 0.9
    return phi

# 10. Mr
def _Mr(phi, ass, fy, d, a):
    Mr = phi*ass*fy*(d-(a/2))/100000
    return Mr
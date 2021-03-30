import matplotlib.pyplot as plt
from apps.acero.calc_acero import _dB, _est
#Hola
#Filas de acero de la columna y cantidad de barras por fila
F = [3, 2, 2, 2, 3, 0]
#favor introducir los valores en orden!!
def _filas(F):
    if (F[5] == 0):
        if (F[4] == 0):
            if (F[3] == 0):
                if (F[2] == 0):
                    if (F[1] == 0):
                        filas = 1
                    else:
                        filas = 2
                else:
                    filas = 3
            else:
                filas = 4
        else:
            filas = 5
    else:
        filas = 6
    return filas
        
#designacion de las barras de cada fila
B = [6, 5, 5, 5, 6, 0]

#Areas por fila
def aCol(Fil, Bar):
    Area = ((3.1415926536/4)*(Bar*2.54/8)**2)*Fil
    return Area

Alist = []
for n in range(6):
    Alist.append(aCol(F[n], B[n]))
AT = sum(Alist)

# seccion - area bruta - cuantia
b = 40
h = 60

Ag = b*h
cuan = AT/Ag

#Alturas efectivas
rec = 4
dB = _dB(B)
dEst = _est(dB)*2.54/8
dF1 = B[0]*2.54/8

def _d1(B, F, rec, dEst, dF1):
    if (B[0] == 0 or F[0] == 0):
        d1 = 0
    else:
        d1 = rec+dEst+(dF1/2)
    return d1

def _d2(B, F, h, d1, filas):
    if (B[1] == 0 or F[1] == 0):
        d2 = 0
    else:
        d2 = ((h-2*d1)/(filas-1))+d1
    return d2

def _d3(B, F, h, d1, d2, filas):
    if (B[2] == 0 or F[2] == 0):
        d3 = 0
    else:
        d3 = ((h-2*d1)/(filas-1))+d2
    return d3

def _d4(B, F, h, d1, d3, filas):    
    if (B[3] == 0 or F[3] == 0):
        d4 = 0
    else:
        d4 = ((h-2*d1)/(filas-1))+d3
    return d4

def _d5(B, F, h, d1, d4, filas):    
    if (B[4] == 0 or F[4] == 0):
        d5 = 0
    else:
        d5 = ((h-2*d1)/(filas-1))+d4
    return d5

def _d6(B, F, h, d1, d5, filas):    
    if (B[5] == 0 or F[5] == 0):
        d6 = 0
    else:
        d6 = ((h-2*d1)/(filas-1))+d5
    return d6

#MATERIALES

fy = 4200
E = 2000000
fc = 280
b1 = 0.850

# puntos 2-10 funcion

def puntos(ptos, dlist):
    def pts(C, dlist):
    #valor c    
        c = C*h

        #funcion para lista de es
        def _es(d):
            if (d==0):
                es = 0
            else:
                es = ((c-d)/c)*0.003
            return es
    #lista es    
        eslist = []
        for n in dlist:
            eslist.append(_es(n))
    #minimo valor de es
        esmin = min(eslist)

        #funcion para lista de fs
        def _fs(es):
            if (E*es<-4200):
                fs =-4200
            elif (E*es>4200):
                fs = 4200
            else:
                fs = E*es
            return fs
    #lista fs    
        fslist = []
        for n in eslist:
            fslist.append(_fs(n))

    #Valor FC
        FC = 0.85*fc*b1*c*b/1000
    #lista Fs    
        Fslist =[]
        for n in range(6):
            Fslist.append(fslist[n]*Alist[n])
    #valor PN        
        Pn = FC+(sum(Fslist)/1000)
    #valor jc    
        jc = (h/2)-b1*c/2

        #funcion para lista ji
        def _ji(d):
            if (d==0):
                ji = 0
            else:
                ji = (h/2)-d
            return ji
    #lista ji    
        jilist = []
        for n in dlist:
            jilist.append(_ji(n))

        Fsji = []
        for n in range(6):
            Fsji.append(Fslist[n]*jilist[n])
    #valor Mn            
            Mn = (FC*jc)+(sum(Fsji)/1000)
        return Pn, Mn, esmin
    #lista de valores de Pn, Mn y es para cada punto
    cdif = 1/(ptos-2)
    PnMneslist = []
    for n in range(ptos-2):
        C = cdif*(n+1)
        PnMneslist.append(pts(C, dlist))

    #Pn y Mn extremos
    Pn1 = -AT*fy/1000
    Pnlast = (0.85*fc*(Ag-AT)+fy*AT)/1000
    Mn1 = Mnlast = 0

    #lista Pn
    Pnlist = [Pn1]
    for n in range(ptos-2):
        Pnlist.append(PnMneslist[n][0])
    Pnlist.append(Pnlast)
    
    #lista Mn
    Mnlist = [Mn1]
    for n in range(ptos-2):
        Mnlist.append(PnMneslist[n][1])
    Mnlist.append(Mnlast)
    
    #funcion para hallar phi
    def _phi(et):
        if (et <= -0.005):
            phi = 0.9
        elif (et >= -0.002):
            phi = 0.65
        else:
            phi = 0.65+(-et-0.002)*(250/3)
        return phi
    #lista phi
    philist = [0.9]
    for n in range(ptos-2):
        ll = PnMneslist[n][2]
        kk = _phi(ll)
        philist.append(kk)
    philist.append(0.65)
    #lista phiPn
    phiPnlist = []
    for n in range(ptos):
        phiPnlist.append(Pnlist[n]*philist[n])
        
    #lista phiMn
    phiMnlist = []
    for n in range(ptos):
        phiMnlist.append(Mnlist[n]*philist[n])
    
    return Pnlist, Mnlist, phiPnlist, phiMnlist

#listas
'''
DPn = puntos(50)[0]
DMn = puntos(50)[1]
DphiPn = puntos(50)[2]
DphiMn = puntos(50)[3]

plt.plot(DMn, DPn, label='Mn, Pn')
plt.plot(DphiMn, DphiPn, label='phiMn, phiPn')
plt.legend(loc=1)
plt.xlabel('M (KN*m)')
plt.ylabel('P (KN)')
plt.title('Diagrama de Interacción')
plt.grid()
'''
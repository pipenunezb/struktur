from apps.home.funciones import rdUp, rdDown, rd, trc

#Paso 1: hallar K y R
def _K(Pu, fc, b, h):
    K = Pu*1000/(fc*b*h)
    return K

def _R(Mu, fc, b, h):
    R = Mu*100000/(fc*b*h*h)
    return R


#Paso 2: determinar el valor de g, g1 y g2
def _g(h, dP):
    g = (h-(2*dP))/h
    return g

def _g1(g):
    g1 = trc(g, 1)
    return g1

def _g2(g):
    g2 = rdUp(g, 1)
    return g2

#en este punto el usuario debe escoger una distribucion de aceros y hallar la cuantia en los diagramas de interaccion

#Paso 3: definir cuantia

#A: si g solo tiene 1 decimal -> la cuantia sera introducida por el usuario
#B: si g tiene mas de 1 decimal -> interpolar con las cuantias de g1 y g2
def _cuan_int(cuan1, cuan2, g1, g2, g):
    cuantia = cuan1-(((g-g1)*(cuan1-cuan2))/(g2-g1))
    return cuantia
#comprobacion de cuantia minima y maxima
def _min_cuan(cuan):
    if (cuan < 0.01):
        cuan = 0.01
    else:
        cuan = cuan
    return cuan
def _max_cuan(cuan):
    if (cuan <= 0.04):
        return True
    else:
        return False


#Paso 4: cantidad de acero
def _asc(cuantia, b, h):
    asc = cuantia*b*h
    return asc
#ass depende de la eleccion del usuario (CHECK)


#Paso 5: comprobacion de separacion 
#lo referente a separaciones se encuentra en calc_acero.py entre las lineas 144 - 158
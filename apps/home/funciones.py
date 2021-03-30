import math

#Redondear MAS
def rdUp(n, d=0):
    mt = 10**d
    return math.ceil(n*mt)/mt

#Redondear MENOS
def rdDown(n, d=0):
    mt = 10**d
    return math.floor(n*mt)/mt

#Redondear
def rd(n, d=3):
    mt = 10**d
    if (n>= 0):
        r = math.floor(n*mt+0.5)/mt
    else:
        r = math.ceil(n*mt-0.5)/mt
    return r

#Truncar
def trc(n, d=0):
    mt = 10**d
    return int(n*mt)/mt
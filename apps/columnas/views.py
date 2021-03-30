from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'columnas/columnas.html')

def normas(request):
    return render(request, 'columnas/columnas_nor.html')

# VIEW DE LOS CALCULOS - RUTINA DE COLUMNAS
from apps.columnas.forms import calc
from apps.acero.calc_acero import _acero_col, filtro, _dB, _est, _dbar_col, _sep_col, _comp_s_col
from apps.columnas.calc_columnas import _K, _R, _g, _g1, _g2, _cuan_int, _min_cuan, _max_cuan, _asc
from apps.home.funciones import rdUp, rdDown, rd, trc

def calculos(request):
    submit_calc= request.POST.get("submit_calc")

    fc_=fy_=Pu=Mu=b=h=dP=rec=agg=cuan1=cuan2=cuan3=dist=''
    fc=fy=K=R=g=g1=g2=espacios=barb=barh=cuanti=cuantia=''
    max_cuan=asc=areas=barras=areasFilt=ass=bar=dB=est=ass_show=''
    dbarb=dbarh=sepb=seph=comp_sepb=comp_seph=separacionb=separacionh=''

    form_calc= calc(request.POST or None)

    if form_calc.is_valid():
        fc_= form_calc.cleaned_data.get("fc")
        fy_= form_calc.cleaned_data.get("fy")
        Pu= form_calc.cleaned_data.get("Pu")
        Mu= form_calc.cleaned_data.get("Mu")
        b= form_calc.cleaned_data.get("b")
        h= form_calc.cleaned_data.get("h")
        dP= form_calc.cleaned_data.get("dP")
        rec= form_calc.cleaned_data.get("rec")
        agg= form_calc.cleaned_data.get("agg")
        cuan1= form_calc.cleaned_data.get("cuan1")
        cuan2= form_calc.cleaned_data.get("cuan2")
        cuan3= form_calc.cleaned_data.get("cuan3")
        dist= form_calc.cleaned_data.get("dist")

        if (cuan1 == None) and (cuan2 == None) and (cuan3 == None):
        
            # fc y fy
            if (fc_ == '1'):
                fc = 210
            elif (fc_ == '2'):
                fc = 280
            else:
                fc = 350

            if (fy_ == '1'):
                fy = 2800
            else:
                fy = 4200

            #Paso 1: Hallar K y R
            K = rd(_K(Pu, fc, b, h))
            R = rd(_R(Mu, fc, b, h))

            #Paso 2: determinar g, g1 y g2
            g = rd(_g(h, dP))
            g1 = _g1(g)
            g2 = _g2(g)

        else:

            # fc y fy
            if (fc_ == '1'):
                fc = 210
            elif (fc_ == '2'):
                fc = 280
            else:
                fc = 350

            if (fy_ == '1'):
                fy = 2800
            else:
                fy = 4200

            #Paso 1: Hallar K y R
            K = rd(_K(Pu, fc, b, h))
            R = rd(_R(Mu, fc, b, h))

            #Paso 2: determinar g, g1 y g2
            g = rd(_g(h, dP))
            g1 = _g1(g)
            g2 = _g2(g)

            #seleccion de distribucion
            if (dist == '1'):
                barb = 6
                barh = 6
            elif (dist == '2'):
                barb = 4
                barh = 6
            elif (dist == '3'):
                barb = 3
                barh = 6
            elif (dist == '4'):
                barb = 2
                barh = 6
            elif (dist == '5'):
                barb = 6
                barh = 4
            elif (dist == '6'):
                barb = 4
                barh = 4
            elif (dist == '7'):
                barb = 3
                barh = 4
            elif (dist == '8'):
                barb = 2
                barh = 4
            elif (dist == '9'):
                barb = 6
                barh = 3
            elif (dist == '10'):
                barb = 4
                barh = 3
            elif (dist == '11'):
                barb = 3
                barh = 3
            elif (dist == '12'):
                barb = 2
                barh = 3
            elif (dist == '13'):
                barb = 6
                barh = 2
            elif (dist == '14'):
                barb = 4
                barh = 2
            elif (dist == '15'):
                barb = 3
                barh = 2
            elif (dist == '16'):
                barb = 2
                barh = 2
            espacios =(barb+barh-2)*2

            #Paso 3: definir cuantia
            if (g1 == g2):
                cuanti = cuan3
            else:
                cuanti = rd(_cuan_int(cuan1, cuan2, g1, g2, g), 4)
            #verificacion cuantia minima
            cuantia = _min_cuan(cuanti)
            #verificacion cuantia maxima
            if (_max_cuan(cuantia) == True):
                max_cuan = '[p ≤ 0.04] CUMPLE'
            else:
                max_cuan = '[p > 0.04] NO CUMPLE'

            #Paso 4: cantidad de acero
            asc = rd(_asc(cuantia, b, h), 4)
            
            #procedimiento vigas o columnas
            areas = _acero_col(espacios)[1]
            barras = _acero_col(espacios)[0]
            areasFilt = filtro(asc, areas)
            ass = min(areasFilt)
            bar = barras[areas.index(ass)]
            dB = _dB(bar)
            est = _est(dB)
            ass_show = rd(ass, 4)

            #Paso 5: comprobacion de separación
            dbarb = _dbar_col(dB, barb)
            dbarh = _dbar_col(dB, barh)

            sepb = rd(_sep_col(barb, b, rec, est, dbarb))
            seph = rd(_sep_col(barh, h, rec, est, dbarh))
            comp_sepb = _comp_s_col(sepb, dB, agg)
            comp_seph = _comp_s_col(seph, dB, agg)
            #comprobacion de separacion
            if comp_sepb == True:
                separacionb = 'CUMPLE'
            else:
                separacionb = 'NO CUMPLE'

            if comp_seph == True:
                separacionh = 'CUMPLE'
            else:
                separacionh = 'NO CUMPLE'

    context1= {'form_calc':form_calc, 'fc':fc, 'fy':fy, 'Pu':Pu, 'Mu':Mu, 'b':b, 'h':h, 'dP':dP, 'rec':rec, 'agg':agg, 'cuan1':cuan1, 'cuan2':cuan2, 'cuan3':cuan3, 'K':K, 'R':R, 'g':g, 'g1':g1, 'g2':g2, 'espacios':espacios, 'barb':barb, 'barh':barh, 'cuanti':cuanti, 'cuantia':cuantia, 'max_cuan':max_cuan, 'asc':asc, 'areas':areas, 'barras':barras, 'areasFilt':areasFilt, 'ass':ass, 'bar':bar, 'dB':dB, 'est':est, 'ass_show':ass_show, 'dbarb':dbarb, 'dbarh':dbarh, 'sepb':sepb, 'seph':seph, 'comp_sepb':comp_sepb, 'comp_seph':comp_seph, 'separacionb':separacionb, 'separacionh':separacionh, 'submit_calc':submit_calc}

    return render(request, 'columnas/columnas_calc.html', context1)

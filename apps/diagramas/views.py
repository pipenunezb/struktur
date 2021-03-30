from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'diagramas/diagramas.html')

def normas(request):
    return render(request, 'diagramas/diagramas_nor.html')

# VIEW DE LOS CALCULOS - RUTINA DE DIAGRAMAS
from apps.diagramas.forms import calc
from apps.acero.calc_acero import _dB, _est
import io
import urllib, base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_agg import FigureCanvasAgg
from apps.diagramas.calc_diagramas import _filas, aCol, _d1, _d2, _d3, _d4, _d5, _d6, puntos
from apps.home.funciones import rd

def calculos(request):
    submitbutton= request.POST.get("submit")

    #datos form
    F1=F2=F3=F4=F5=F6=B1=B2=B3=B4=B5=B6=b=h=rec=fc_=fy_=E=b1=''
    #proceso
    F=filas=B=Alist=AT=Ag=cuan=dB=dest=dEst=dfila1=dF1=d1=d2=d3=d4=d5=d6=d=fc=fy=''
    #show
    Ag_show=AT_show=d1_show=d2_show=d3_show=d4_show=d5_show=d6_show=''
    #plot grafico
    DPn=DMn=DphiPn=DphiMn=uri=''

    form= calc(request.POST or None)
    if form.is_valid():
        F1= form.cleaned_data.get("F1")
        F2= form.cleaned_data.get("F2")
        F3= form.cleaned_data.get("F3")
        F4= form.cleaned_data.get("F4")
        F5= form.cleaned_data.get("F5")
        F6= form.cleaned_data.get("F6")
        B1= form.cleaned_data.get("B1")
        B2= form.cleaned_data.get("B2")
        B3= form.cleaned_data.get("B3")
        B4= form.cleaned_data.get("B4")
        B5= form.cleaned_data.get("B5")
        B6= form.cleaned_data.get("B6")
        
        b= form.cleaned_data.get("b")
        h= form.cleaned_data.get("h")
        rec= form.cleaned_data.get("rec")
        fc_= form.cleaned_data.get("fc")
        fy_= form.cleaned_data.get("fy")
        E= form.cleaned_data.get("E")
        b1= form.cleaned_data.get("b1")
        
        #cantidad de filas y de barras por fila
        F = [F1, F2, F3, F4, F5, F6]
        filas = _filas(F)

        #Diametro de barras
        B = [B1, B2, B3, B4, B5, B6]

        #Areas de barras
        Alist = []
        for n in range(6):
            Alist.append(aCol(F[n], B[n]))
        AT = sum(Alist)
        AT_show = rd(AT)

        #seccion - area bruta - cuantia
        Ag = b*h
        Ag_show = rd(Ag)
        cuan = rd(AT/Ag, 4)

        #alturas efectivas
        dB = _dB(B)
        dest = _est(dB)
        dEst = dest*2.54/8
        dfila1 = B[0]
        dF1 = dfila1*2.54/8

        d1 = _d1(B, F, rec, dEst, dF1)
        d2 = _d2(B, F, h, d1, filas)
        d3 = _d3(B, F, h, d1, d2, filas)
        d4 = _d4(B, F, h, d1, d3, filas)
        d5 = _d5(B, F, h, d1, d4, filas)
        d6 = _d6(B, F, h, d1, d5, filas)

        d1_show = rd(d1)
        d2_show = rd(d2)
        d3_show = rd(d3)
        d4_show = rd(d4)
        d5_show = rd(d5)
        d6_show = rd(d6)

        d = [d1, d2, d3, d4, d5, d6]

        #materiales
        #fc y fy
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

        #listas de puntos
        DPn = puntos(50, d)[0]
        DMn = puntos(50, d)[1]
        DphiPn = puntos(50, d)[2]
        DphiMn = puntos(50, d)[3]

        plt.plot(DMn, DPn, label='Mn, Pn')
        plt.plot(DphiMn, DphiPn, label='phiMn, phiPn')
        plt.legend(loc=1)
        plt.xlabel('M (Tonf*cm)')
        plt.ylabel('P (Tonf)')
        plt.title('Diagrama de Interacción')
        plt.grid()

        #plt.show()
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        

    context= {'form': form, 'F1':F1, 'F2':F2, 'F3':F3, 'F4':F4, 'F5':F5, 'F6':F6, 'B1':B1, 'B2':B2, 'B3':B3, 'B4':B4, 'B5':B5, 'B6':B6, 'b':b, 'h':h, 'rec':rec, 'fc_':fc_, 'fy_':fy_, 'E':E, 'b1':b1, 'F':F, 'filas':filas, 'B':B, 'Alist':Alist, 'AT':AT, 'AT_show':AT_show, 'Ag':Ag, 'Ag_show':Ag_show, 'cuan':cuan, 'dB':dB, 'dest':dest, 'dEst':dEst, 'dfila1':dfila1, 'dF1':dF1, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'd6':d6, 'd1_show':d1_show, 'd2_show':d2_show, 'd3_show':d3_show, 'd4_show':d4_show, 'd5_show':d5_show, 'd6_show':d6_show, 'd':d, 'fc':fc, 'fy':fy, 'DPn':DPn, 'DMn':DMn, 'DphiPn':DphiPn, 'DphiMn':DphiMn, 'data':uri, 'submitbutton':submitbutton}
    plt.close()
    return render(request, 'diagramas/diagramas_calc.html', context)

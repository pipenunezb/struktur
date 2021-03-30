from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'acero/acero.html')

def normas(request):
    return render(request, 'acero/acero_nor.html')


# VIEW DE LOS CALCULOS - RUTINA DE ACERO
from apps.acero.forms import calc
from apps.acero.calc_acero import acero, _as_col, filtro, _org_bar, _dB, _est, _dbar, _sep, _sep_vig, _dbar_col, _sep_col, _comp_s_col
from apps.home.funciones import rd, rdUp, trc

def calculos(request):
    submitbutton= request.POST.get("submit")

    element=b=h=cuantia=rec=agg=asc=areas=barras=areasFilt=ass=bar=dB=est=sep=comp_sep=bar_show=''
    nb=nh=dbarb=dbarh=sepb=seph=comp_sepb=comp_seph=ass_show=n=''

    form= calc(request.POST or None)
    if form.is_valid():
        element= form.cleaned_data.get("element")
        b= form.cleaned_data.get("b")
        h= form.cleaned_data.get("h")
        cuantia= form.cleaned_data.get("cuantia")
        rec= form.cleaned_data.get("rec")
        agg= form.cleaned_data.get("agg")
        
        if (element == '1'):
            #vigas
            asc = rd(b*(h-(rec+2))*cuantia)

            #procedimiento vigas
            areas = acero(2, 12)[1]
            barras = acero(2, 12)[0]
            areasFilt = filtro(asc, areas)
            ass = min(areasFilt)
            bar = barras[areas.index(ass)]
            dB = _dB(bar)
            est = _est(dB)
            dbar = _dbar(bar)
            sep = rd(_sep(bar, b, rec, est, dbar))

            comp_sep = _sep_vig(sep, dB, agg)

            while comp_sep == False:
                areasFilt.remove(ass)
                ass = min(areasFilt)
                bar = barras[areas.index(ass)]
                dB = _dB(bar)
                est = _est(dB)
                dbar = _dbar(bar)
                sep = rd(_sep(bar, b, rec, est, dbar))
                comp_sep = _sep_vig(sep, dB, agg)
            bar_show = _org_bar(bar)
            
        else:
            #columnas
            asc = rd(b*h*cuantia)
            
            #procedimiento columnas
            areas = _as_col(4, 40)[1]
            barras = _as_col(4, 40)[0]
            areasFilt = filtro(asc, areas)
            ass = min(areasFilt)
            bar = barras[areas.index(ass)]
            dB = _dB(bar)
            est = _est(dB)

            nh = (2+(len(bar)/2))/(1+(b/h))
            nb = (len(bar)/2)+2-nh
            if (nh-trc(nh) == 0.5) and (nb-trc(nb) == 0.5):
                nb = int(rdUp(nb))
                nh = int(trc(nh))
            else:
                if ((nb-trc(nb)) > (nh-trc(nh))):
                    nb = int(rdUp(nb))
                    nh = int(trc(nh))
                else:
                    nb = int(trc(nb))
                    nh = int(rdUp(nh))
            if (nb == 1):
                nb = nb + 1
                nh = nh - 1
            if (nb == 0):
                nb = nb + 2
                nh = nh - 2
            if (nh == 1):
                nh = nh + 1
                nb = nb - 1
            if (nh == 0):
                nh = nh + 2
                nb = nb - 2

            dbarb = _dbar_col(dB, nb)
            dbarh = _dbar_col(dB, nh)
            sepb = rd(_sep_col(nb, b, rec, est, dbarb))
            seph = rd(_sep_col(nh, h, rec, est, dbarh))
            comp_sepb = _comp_s_col(sepb, dB, agg)
            comp_seph = _comp_s_col(seph, dB, agg)

            comp_sep = comp_seph and comp_sepb
            
            while comp_sep == False:
                areasFilt.remove(ass)
                ass = min(areasFilt)
                bar = barras[areas.index(ass)]
                dB = _dB(bar)
                est = _est(dB)
                nh = (2+(len(bar)/2))/(1+(b/h))
                nb = (len(bar)/2)+2-nh
                if (nh-trc(nh) == 0.5) and (nb-trc(nb) == 0.5):
                    nb = int(rdUp(nb))
                    nh = int(trc(nh))
                else:
                    if ((nb-trc(nb)) > (nh-trc(nh))):
                        nb = int(rdUp(nb))
                        nh = int(trc(nh))
                    else:
                        nb = int(trc(nb))
                        nh = int(rdUp(nh))
                if (nb == 1):
                    nb = nb + 1
                    nh = nh - 1
                if (nb == 0):
                    nb = nb + 2
                    nh = nh - 2
                if (nh == 1):
                    nh = nh + 1
                    nb = nb - 1
                if (nh == 0):
                    nh = nh + 2
                    nb = nb - 2

                dbarb = _dbar_col(dB, nb)
                dbarh = _dbar_col(dB, nh)
                sepb = rd(_sep_col(nb, b, rec, est, dbarb))
                seph = rd(_sep_col(nh, h, rec, est, dbarh))
                comp_sepb = _comp_s_col(sepb, dB, agg)
                comp_seph = _comp_s_col(seph, dB, agg)

                comp_sep = comp_seph and comp_sepb
        ass_show = rd(ass)
        n = len(bar)

    context= {'form': form, 'element':element, 'b':b, 'h':h, 'cuantia':cuantia, 'rec':rec, 'agg':agg, 'asc':asc, 'areas':areas, 'barras':barras, 'areasFilt':areasFilt, 'ass':ass, 'bar':bar, 'dB':dB, 'est':est, 'sep':sep, 'comp_sep':comp_sep, 'bar_show':bar_show, 'nb':nb, 'nh':nh, 'dbarb':dbarb, 'dbarh':dbarh, 'sepb':sepb, 'seph':seph, 'copm_sepb':comp_sepb, 'comp_seph':comp_seph, 'ass_show':ass_show, 'n':n, 'submitbutton':submitbutton}

    return render(request, 'acero/acero_calc.html', context)
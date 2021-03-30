from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'vigas/vigas.html')

def normas(request):
    return render(request, 'vigas/vigas_nor.html')


# VIEW DE LOS CALCULOS - RUTINA DE ACERO
from apps.vigas.forms import calc
from apps.home.funciones import rdUp, rdDown, rd, trc
from apps.acero.calc_acero import acero, filtro, _bar, _ass, _org_bar, _dB, _est, _dbar, _sep, _sep_vig
from apps.vigas.calc_vigas import CD_CL, _FS, _Mu, _ku, _cuantia, _asc, _y, _comp_area, _a, _B1, _c, _es, _comp_fluen, _phi, _Mr

def calculos(request):
    submitbutton= request.POST.get("submit")

    carga=CD=CL=Wu_=apoyo=L=fc_=fy_=phi=ec=b=h=dP=y=rec=agg=op_cuantia=cuan=op_acero=pbar=''
    fc=fy=Wu=FS=AP=tapoyo=Mu=d=ku=cuantia=''
    asc=areas=barras=areasFilt=ass=bar=dB=est=dbar=length=sep=comp_sep=''
    bar_show=ass_show=comp_area=separacion=a=B1=c=es=comp_fluen=Mr=comp_Mr=''
    dP_r=ku_t=check1=ku_r=y_r=yy=cmin1=cmin2=cmin=cmax=comp_cuan=cuanto=''

    form= calc(request.POST or None)
    if form.is_valid():
        carga= form.cleaned_data.get("carga")
        CD= form.cleaned_data.get("CD")
        CL= form.cleaned_data.get("CL")
        Wu_= form.cleaned_data.get("Wu_")
        apoyo= form.cleaned_data.get("apoyo")
        L= form.cleaned_data.get("L")
        fc_= form.cleaned_data.get("fc")
        fy_= form.cleaned_data.get("fy")
        phi= form.cleaned_data.get("phi")
        ec= form.cleaned_data.get("ec")
        b= form.cleaned_data.get("b")
        h= form.cleaned_data.get("h")
        y= form.cleaned_data.get("y")
        rec= form.cleaned_data.get("rec")
        agg= form.cleaned_data.get("agg")
        op_cuantia= form.cleaned_data.get("op_cuantia")
        cuan= form.cleaned_data.get("cuan")
        op_acero= form.cleaned_data.get("op_acero")
        pbar= form.cleaned_data.get("pbar")

        if (op_acero == '2'):
            pbar= 1
        if (op_cuantia == '2'):
            cuan= 1

    #fc y fy
        if (fc_ == '1'):
            fc = 210
        elif (fc_ == '2'):
            fc = 280
        elif (fc_ == '3'):
            fc = 350
        else:
            fc = ''

        if (fy_ == '1'):
            fy = 2800
        elif (fy_ == '2'):
            fy = 4200
        else:
            fy = ''
        
    # Paso 1 (cargas)
        if (carga == '1'):
            Wu = CD_CL(CD, CL)
            FS = rd(_FS(Wu, CD, CL, phi))
        else:
            Wu = Wu_
        
    # Paso 2 (Mu)
        if (apoyo=='1'):
            AP = 8
            tapoyo = 'simplemente apoyadas'
        elif (apoyo=='2'):
            AP = 8
            tapoyo = 'con un apoyo empotrado'
        elif (apoyo=='3'):
            AP = 12
            tapoyo = 'con dos apoyos empotrados'
        elif (apoyo=='4'):
            AP = 2
            tapoyo = 'en voladizo'
        else:
            AP = 1
        Mu = rd(_Mu(Wu, L, AP), 5)

    # Paso 3 (B1)
        B1 = rd(_B1(fc), 4)

        cmin1 = rd(0.8*(fc**0.5)/fy, 4)
        cmin2 = rd(14/fy, 4)
        if (cmin1 > cmin2):
            cmin = cmin1
        else:
            cmin = cmin2
        cmax = trc(0.85*(fc/fy)*B1*(3/8), 4)

    # IF 1
        if (cuan == None):

        # Paso 4 (cuantia)
            dP = rec + y
            d = h-dP
            ku = rd(_ku(Mu, b, d))

    # IF 2
        elif (pbar == ''):
            
        # Paso 4 (cuantia)
            dP = rec + y
            d = h-dP
            ku = rd(_ku(Mu, b, d))
            if (op_cuantia == '1'):
                cuantia = cuan
            if (op_cuantia == '2'):
                cuantia = rd(_cuantia(fc, fy, phi, ku),5)
                cuanto = cuantia
            
            if (cuantia < cmin):
                cuantia = cmin
                comp_cuan = 'CUMPLE'
            elif (cuantia >= cmin) and (cuantia <= cmax):
                comp_cuan = 'CUMPLE'
            else:
                comp_cuan = 'ρmax NO CUMPLE'
            

        # Paso 5 (acero)
            asc = rd(_asc(cuantia, b, d), 4)

    # IF 3                
        else:

        # Paso 4 (cuantia)
            dP = rec + y
            d = h-dP
            ku = rd(_ku(Mu, b, d))
            if (op_cuantia == '1'):
                cuantia = cuan
            if (op_cuantia == '2'):
                cuantia = rd(_cuantia(fc, fy, phi, ku), 5)
                cuanto = cuantia

            if (cuantia < cmin):
                cuantia = cmin
                comp_cuan = 'CUMPLE'
            elif (cuantia >= cmin) and (cuantia <= cmax):
                comp_cuan = 'CUMPLE'
            else:
                comp_cuan = 'ρmax NO CUMPLE'

        # Paso 5 (acero)
            asc = rd(_asc(cuantia, b, d), 4)
            if (op_acero == '1'):
                bar = _bar(pbar)
                ass = _ass(bar)
                dB = _dB(bar)
                est = _est(dB)
                dbar = _dbar(bar)
                length = len(bar)
                sep = rd(_sep(bar, b, rec, est, dbar))
                comp_sep = _sep_vig(sep, dB, agg)
            if (op_acero == '2'):
                areas = acero(2, 12)[1]
                barras = acero(2, 12)[0]
                areasFilt = filtro(asc, areas)
                ass = min(areasFilt)
                bar = barras[areas.index(ass)]
                dB = _dB(bar)
                est = _est(dB)
                dbar = _dbar(bar)
                length = len(bar)
                sep = rd(_sep(bar, b, rec, est, dbar))
                comp_sep = _sep_vig(sep, dB, agg)
                #ciclo de comprobacion de separación
                while comp_sep == False:
                    areasFilt.remove(ass)
                    ass = min(areasFilt)
                    bar = barras[areas.index(ass)]
                    dB = _dB(bar)
                    est = _est(dB)
                    dbar = _dbar(bar)
                    length = len(bar)
                    sep = rd(_sep(bar, b, rec, est, dbar))
                    comp_sep = _sep_vig(sep, dB, agg)
            
            dP_r = rd(_y(bar, est, rec), 4)
            y_r = dP_r - rec
            while (dP != dP_r):
            #parametros para pararse en los if
                check1 = 1
                cuan = None
                pbar = ''
                if (op_acero == '2'):
                    pbar= 1
                if (op_cuantia == '2'):
                    cuan= 1

                if (cuan == None):
                    dP = dP_r
                    d = h-dP
                    ku_r = rd(_ku(Mu, b, d))
                    ku_t = phi*cuantia*fy*(1-(cuantia*fy/(2*0.85*fc)))
                    ku = ku_r
                    if (ku_t >= ku_r) :
                        ku = ku_r
                        cuan = cuantia
                        asc = rd(_asc(cuantia, b, d), 4)
                        if (ass >= asc):
                            pbar = bar
                        else:
                            bar = None
                    else:
                        cuantia = None
                    break

                elif (pbar == ''):
                    dP = dP_r
                    d = h-dP
                    ku_t = ku
                    ku_r = rd(_ku(Mu, b, d))
                    ku = ku_r
                    cuantia = rd(_cuantia(fc, fy, phi, ku), 5)
                    cuanto = cuantia
                    cuan = cuantia
                    asc = rd(_asc(cuantia, b, d), 4)
                    if (ass >= asc):
                        pbar = bar
                    else:
                        bar: None
                    
                    if (cuantia < cmin):
                        cuantia = cmin
                        comp_cuan = 'CUMPLE'
                    elif (cuantia >= cmin) and (cuantia <= cmax):
                        comp_cuan = 'CUMPLE'
                    else:
                        comp_cuan = 'ρmax NO CUMPLE'

                    break
 
                else:
                    dP = dP_r
                    d = h-dP
                    ku_t = ku
                    ku_r = rd(_ku(Mu, b, d))
                    ku = ku_r
                    if (op_cuantia == '2'):
                        cuantia = rd(_cuantia(fc, fy, phi, ku), 5)
                        cuanto = cuantia
                    
                    if (cuantia < cmin):
                        cuantia = cmin
                        comp_cuan = 'CUMPLE'
                    elif (cuantia >= cmin) and (cuantia <= cmax):
                        comp_cuan = 'CUMPLE'
                    else:
                        comp_cuan = 'ρmax NO CUMPLE'
                    #duda
                    if (ku_t >= ku_r):
                        cuan = cuantia
                        asc = rd(_asc(cuantia, b, d), 4)
                        if (asc > ass):
                            areas = acero(2, 12)[1]
                            barras = acero(2, 12)[0]
                            areasFilt = filtro(asc, areas)
                            ass = min(areasFilt)
                            bar = barras[areas.index(ass)]
                            dB = _dB(bar)
                            est = _est(dB)
                            dbar = _dbar(bar)
                            length = len(bar)
                            sep = rd(_sep(bar, b, rec, est, dbar))
                            comp_sep = _sep_vig(sep, dB, agg)
                            #ciclo de comprobacion de separación
                            while comp_sep == False:
                                areasFilt.remove(ass)
                                ass = min(areasFilt)
                                bar = barras[areas.index(ass)]
                                dB = _dB(bar)
                                est = _est(dB)
                                dbar = _dbar(bar)
                                length = len(bar)
                                sep = rd(_sep(bar, b, rec, est, dbar))
                                comp_sep = _sep_vig(sep, dB, agg)
                            dP_r = rd(_y(bar, est, rec), 4)
                            y_r = dP_r - rec
                        
            ass = _ass(bar)
            dB = _dB(bar)
            est = _est(dB)
            dbar = _dbar(bar)
            length = len(bar)
            sep = rd(_sep(bar, b, rec, est, dbar))
            comp_sep = _sep_vig(sep, dB, agg)
            yy = rd(dP - rec - est*2.54/8, 4)

    
        # Comprobaciones, bar_show y ass_show
            bar_show = _org_bar(bar)
            ass_show = rd(ass, 4)

            comp_area = _comp_area(asc, ass_show)
            if comp_sep == True:
                separacion = 'CUMPLE'
            else:
                separacion = 'NO CUMPLE'
            # condicional if para rutina de comprobaciones

        # Paso 6 (a)
            a = rd(_a(ass_show, fy, fc, b), 4)

        # Paso 7 (c)
            c = rd(_c(a, B1), 4)

        # Paso 8 (es)
            es = rd(_es(ec, c, d), 4)
            comp_fluen = _comp_fluen(es)

        # Paso 9 (recalcular phi)
            phi = rd(_phi(es))

        # Paso 10 (Mr)
            Mr = rd(_Mr(phi, ass_show, fy, d, a), 5)
            if (Mr >= Mu):
                comp_Mr = 'CUMPLE'
            else:
                comp_Mr = 'NO CUMPLE'

    context= {'cuanto':cuanto, 'comp_cuan':comp_cuan, 'cmin1':cmin1, 'cmin2':cmin2, 'cmin':cmin, 'cmax':cmax, 'yy':yy, 'dP_r':dP_r, 'ku_t':ku_t, 'check1':check1, 'ku_r':ku_r, 'y_r':y_r, 'form':form, 'carga':carga, 'CD':CD, 'CL':CL, 'Wu_':Wu_, 'apoyo':apoyo, 'L':L, 'fc_':fc_, 'fy_':fy_, 'phi':phi, 'ec':ec, 'b':b, 'h':h, 'dP':dP, 'rec':rec, 'agg':agg, 'fc':fc, 'fy':fy, 'Wu':Wu, 'FS':FS, 'AP':AP, 'tapoyo':tapoyo, 'Mu':Mu, 'd':d, 'ku':ku, 'cuantia':cuantia, 'asc':asc, 'areas':areas, 'barras':barras, 'areasFilt':areasFilt, 'ass':ass, 'bar':bar, 'dB':dB, 'est':est, 'dbar':dbar, 'length':length, 'sep':sep, 'comp_sep':comp_sep, 'bar_show':bar_show, 'ass_show':ass_show, 'comp_area':comp_area, 'separacion':separacion, 'a':a, 'B1':B1, 'c':c, 'es':es, 'comp_fluen':comp_fluen, 'Mr':Mr, 'comp_Mr':comp_Mr, 'submitbutton':submitbutton}

    return render(request, 'vigas/vigas_calc.html', context)
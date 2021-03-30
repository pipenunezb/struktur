from django import forms

class calc(forms.Form):
    #---------- fc y fy ----------
    fc = forms.ChoiceField(choices= ((1, ('210 (Kgf/cm²)')), (2, ('280 (Kgf/cm²)')), (3, ('350 (Kgf/cm²)'))))
    fy = forms.ChoiceField(choices= ((1, ('2800 (Kgf/cm²)')), (2, ('4200 (Kgf/cm²)'))), initial=2)

    #---------- cargas ----------
    Pu = forms.FloatField(label='Pu (Tf)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    Mu = forms.FloatField(label='Mu (Tf*m)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    
    #---------- dimensiones ----------
    b = forms.FloatField(label='b (cm)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    h = forms.FloatField(label='h (cm)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    dP = forms.FloatField(label="d' (cm)", required=False, initial=6, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    rec = forms.FloatField(label='rec (cm)', required=False, initial=4, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    agg = forms.FloatField(label='tamaño max agregado (plg)', required=False, initial=1, widget=forms.TextInput(attrs={'class' : 'form-control lg input'}))
    
    #---------- cuantia ----------
    cuan1 = forms.FloatField(label='cuantia 1', required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg cuan1 input'}))
    cuan2 = forms.FloatField(label='cuantia 2', required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg cuan2 input'}))
    cuan3 = forms.FloatField(label='cuantia', required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg cuan3 input'}))
    
    #---------- seleccion de distribucion ----------
    CHOICES=[('','Distribución del acero'), (1,'opción 1'), (2,'opción 2'), (3,'opción 3'), (4,'opción 4'), (5,'opción 5'), (6,'opción 6'), (7,'opción 7'), (8,'opción 8'), (9,'opción 9'), (10,'opción 10'), (11,'opción 11'), (12,'opción 12'), (13,'opción 13'), (14,'opción 14'), (15,'opción 15'), (16,'opción 16')]
    dist = forms.ChoiceField(label='', required=False, choices=CHOICES)
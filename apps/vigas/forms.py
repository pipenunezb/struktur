from django import forms

class calc(forms.Form):
    #----------tipo de carga----------
    carga = forms.ChoiceField(label='', choices= (('', ('Tipo de carga')), (1, ('CD y CL')), (2, ('Wu'))))
    CD = forms.FloatField(label='CD (Tf/m)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    CL = forms.FloatField(label='CL (Tf/m)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    Wu_ = forms.FloatField(label='Wu (Tf/m)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    
    #----------tipo de apoyo----------
    apoyo = forms.ChoiceField(label='', choices= (('', ('Seleccione tipo de apoyo')), (1, ('Simplemente apoyado')), (2, ('Un apoyo empotrado')), (3, ('Dos apoyos empotrados')), (4, ('Voladizo'))))
    
    #----------f'c y fy----------
    fc = forms.ChoiceField(label="f'c", choices= ((1, ('210 (Kgf/cm²)')), (2, ('280 (Kgf/cm²)')), (3, ('350 (Kgf/cm²)'))))
    fy = forms.ChoiceField(label='fy', choices= ((1, ('2800 (Kgf/cm²)')), (2, ('4200 (Kgf/cm²)'))), initial=2)

    #----------Longitud----------
    L = forms.FloatField(label='L (m)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm input d-flex align-items-end'}))
    
    #----------b, h y dP----------
    b = forms.FloatField(label='b (cm)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    h = forms.FloatField(label='h (cm)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    y = forms.FloatField(label="", required=False, initial=2, widget=forms.TextInput(attrs={'class' : 'form-control y input'}))
    
    #----------phi y ec----------CAMBIAR SÍMBOLOS VISIBLES
    phi = forms.FloatField(label='ϕ (phi)', required=False, initial=0.9, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    ec = forms.FloatField(label='εc', required=False, initial=0.003, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    
    #----------rec y agg----------
    rec = forms.FloatField(label='rec (cm)', required=False, initial=4, widget=forms.TextInput(attrs={'class' : 'form-control sm input'}))
    agg = forms.FloatField(label='tamaño max agregado (plg)', required=False, initial=1, widget=forms.TextInput(attrs={'class' : 'form-control lg input'}))
    
    #----------como determinar cuantia y barras----------
    op_cuantia = forms.ChoiceField(label='', choices= (('', ('¿Cómo calcular la cuantía?')), (1, ('Con tablas de cuantia')), (2, ('Con fórmula'))))
    op_acero = forms.ChoiceField(label='', choices= (('', ('¿Cómo calcular el acero?')), (1, ('Con tabla de áreas')), (2, ('Cálculo automático'))))
    cuan = forms.FloatField(label='cuantía', required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg input'}))
    pbar = forms.CharField(label='Barras', required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg input', 'placeholder':'Ej: 4, 4, 6, 6'}))

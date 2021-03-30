from django import forms

class calc(forms.Form):
    #----------detalles del refuerzo----------
    F1 = forms.IntegerField(label='F1', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm F1 input'}))
    B1 = forms.IntegerField(label='B1', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm B1 input'}))
    F2 = forms.IntegerField(label='F2', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm F2 input'}))
    B2 = forms.IntegerField(label='B2', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm B2 input'}))
    F3 = forms.IntegerField(label='F3', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm F3 input'}))
    B3 = forms.IntegerField(label='B3', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm B3 input'}))
    F4 = forms.IntegerField(label='F4', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm F4 input'}))
    B4 = forms.IntegerField(label='B4', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm B4 input'}))
    F5 = forms.IntegerField(label='F5', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm F5 input'}))
    B5 = forms.IntegerField(label='B5', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm B5 input'}))
    F6 = forms.IntegerField(label='F6', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm F6 input'}))
    B6 = forms.IntegerField(label='B6', initial=0, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm B6 input'}))
    
    #----------sección b, h----------
    b = forms.FloatField(label='b (cm)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm b input'}))
    h = forms.FloatField(label='h (cm)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm h input'}))
    
    #----------alturas efectivas rec----------
    rec = forms.FloatField(label='recubrimiento (cm)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg rec input'}))
    
    #----------materiales f'c, fy, E y b1----------
    fc = forms.ChoiceField(label="f'c", choices= ((1, ('210 (kgf/cm²)')), (2, ('280 (kgf/cm²)')), (3, ('350 (kgf/cm²)'))))
    fy = forms.ChoiceField(label='fy', choices= ((1, ('2800 (kgf/cm²)')), (2, ('4200 (kgf/cm²)'))), initial=2)
    E = forms.FloatField(label='E kgf/cm²', initial=2000000, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm E input'}))
    b1 = forms.FloatField(label='β1', initial=0.85, required=False, widget=forms.TextInput(attrs={'class' : 'form-control sm b1 input'}))
    
    
    
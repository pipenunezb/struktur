from django import forms

class calc(forms.Form):
    element = forms.ChoiceField(choices= ((1, ('viga')), (2, ('columna'))))
    b = forms.FloatField(label='b (cm)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg input'}))
    h = forms.FloatField(label='h (cm)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg input'}))
    rec = forms.FloatField(label='rec (cm)', min_value=4, required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg input'}))
    agg = forms.FloatField(label='tamaño de agregado (plg)', required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg input'}))
    cuantia = forms.FloatField(label='cuantía', required=False, widget=forms.TextInput(attrs={'class' : 'form-control lg cuantia input'}))

from django import forms


class TerrorForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=2, label='Nombre')
    fecha_estreno = forms.DateField(label='Fecha de estreno', 
    widget=forms.TextInput(attrs={'placeholder': 'AAAA-MM-DD'})
    )
    duracion = forms.IntegerField()
    sinopsis = forms.CharField(max_length=1000, min_length=5, label='Sinopsis')
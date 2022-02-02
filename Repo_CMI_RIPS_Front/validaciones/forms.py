from django import forms


class ClienteForm(forms.Form):
    nit = forms.CharField(label='Ingrese el NIT: ', max_length=100,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ejemplo (12345452)"}))

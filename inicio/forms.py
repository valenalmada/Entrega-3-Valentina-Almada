from django import forms



class IngresarUBA(forms.Form):
    facultad=forms.CharField(max_length=100)
    carrera= forms.CharField(max_length=100)


class BuscarCarrera(forms.Form):
    carrera=forms.CharField(max_length=100, required=False)
    
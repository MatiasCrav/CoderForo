from django import forms


class FormProfesor(forms.Form):
    nombre = forms.CharField(max_length=255)
    apellido = forms.CharField(max_length=255)
    email = forms.EmailField()
    web = forms.CharField(max_length=255)
    descripcion = forms.CharField(widget=forms.Textarea)
    comision = forms.IntegerField()

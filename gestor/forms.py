from  django import forms

class Form1(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.DateField()
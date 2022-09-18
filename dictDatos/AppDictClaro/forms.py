from django import forms


class TablaFormulario(forms.Form):

    nombre = forms.CharField()


class TablaCampoFormulario(forms.Form):

    tabla = forms.CharField()
    campo = forms.CharField()
    descripcion = forms.CharField()
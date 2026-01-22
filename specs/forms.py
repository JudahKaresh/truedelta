from django import forms

class IntlCheck(forms.Form):
    includeIntl = forms.BooleanField(label = "See international models (basic specs only, 2007-2018)")

class CompareCheck(forms.Form):
    compare = forms.BooleanField(label = "Compare two vehicles")
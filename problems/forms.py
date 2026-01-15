from django import forms

class MyForm(forms.Form):
    category = forms.ChoiceField(
        choices = [
            ('bloop','Bloop'),
            ('shmoop','Shmoop'),
        ]
    )
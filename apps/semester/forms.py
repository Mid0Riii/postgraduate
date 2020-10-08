from django import forms

class DepartureForm(forms.ModelForm):
    depc_dep_avai = forms.BooleanField(required=True)
    depc_arr_avai = forms.BooleanField()
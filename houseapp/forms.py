from django import forms
from .models import HouseData

class HouseForm(forms.ModelForm):
    class Meta:
        model = HouseData
        fields = "__all__"
    
    CRIM = forms.IntegerField()
    INDUS = forms.IntegerField()
    NOX = forms.IntegerField()
    DIS = forms.IntegerField()
    RAD = forms.IntegerField()
    TAX = forms.IntegerField()
    B = forms.IntegerField()

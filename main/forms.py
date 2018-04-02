from django import forms
from .models import Test


class TestForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(max_value=100, min_value=5)
    birth = forms.DateField(help_text='your birth date', required=False)


class TestForm2(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'age', 'birth')
        exclude = ['']

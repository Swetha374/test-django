from django import forms

class AdvancedSearchForm(forms.Form):
    country = forms.CharField(required=False)
    min_pop1980 = forms.IntegerField(required=False)
    max_pop1980 = forms.IntegerField(required=False)

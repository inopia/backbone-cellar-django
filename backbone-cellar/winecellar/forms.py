from django import forms

class Wine(forms.Form):
   name = forms.CharField(max_length=256)
   year = forms.IntegerField()
   grapes = forms.CharField(max_length=256)
   country = forms.CharField(max_length=256)
   region = forms.CharField(max_length=256)
   description = forms.CharField(max_length=8192)

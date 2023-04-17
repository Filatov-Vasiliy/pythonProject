from django import forms
from .models import *


class CarForm(forms.Form):
    name = forms.CharField()
    type_cars = forms.CharField()
    color = forms.CharField()
    power = forms.IntegerField()
    company = forms.ChoiceField(choices=tuple(Company.objects.values_list('id', 'name')))


class StatusForm(forms.Form):
        name = forms.CharField()


class DriversForm(forms.Form):
    print(StatusDrivers.objects.values_list('id', 'name'))
    name = forms.CharField()
    number = forms.IntegerField()
    email = forms.EmailField()
    status = forms.ChoiceField(choices=tuple(StatusDrivers.objects.values_list('id', 'name')))


class CompanyForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    number = forms.IntegerField()
    country = forms.CharField(max_length=30)

from django import forms
from .models import Household,Person,Vehicle

class householdform(forms.ModelForm):

    class Meta:
        model = Household
        fields = ('address', 'zipcode','city','state','bedrooms',)

class personform(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('first_name','last_name','email','age','gender',)

class vehicleform(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ('make','model_name','year','liceance_plate',)

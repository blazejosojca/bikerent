from django.contrib.auth.models import User
from bike.models import Bike, Localization

from django import forms


class BikeFormCreate(forms.ModelForm):

    class Meta:
        model = Bike
        exclude = ['is_rented',
                   'is_functional',
                   'renting_history']


class BikeFormUpdate(forms.ModelForm):

    class Meta:
        model = Bike
        exclude = ['is_rented',
                   'renting_history']


class LocalizationForm(forms.ModelForm):
    class Meta:
        model = Localization
        fields = ['city',
                  'street',
                  'building_number']


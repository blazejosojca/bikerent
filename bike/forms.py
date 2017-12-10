from bike.models import Bike, Localization, Renting, Client
from django import forms
from .models import Bike


class BikeFormCreate(forms.ModelForm):

    class Meta:
        model = Bike
        exclude = ['is_rented',
                   'renting_history']


class BikeFormUpdate(forms.ModelForm):

    class Meta:
        model = Bike
        exclude = ['renting_history']


class LocalizationForm(forms.ModelForm):
    class Meta:
        model = Localization
        fields = '__all__'


class RentingForm(forms.ModelForm):

    class Meta:
        model = Renting
        fields = '__all__'


class RentingUpdateForm(forms.ModelForm):
    class Meta:
        model = Renting
        fields = '__all__'





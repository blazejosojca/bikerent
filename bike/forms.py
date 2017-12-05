from django.contrib.auth.models import User
from bike.models import Bike, Localization, Renting, Client
from django import forms


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
        fields = ['city',
                  'street',
                  'building_number']


class RentingForm(forms.ModelForm):

    class Meta:
        model = Renting
        fields = '__all__'


class ReturnRentingForm(forms.ModelForm):

    class Meta:
        model = Renting
        fields = '__all__'

    start_date = forms.DateField(disabled=True)
    start_time = forms.TimeField(disabled=True)
    return_date = forms.DateField(widget=forms.DateInput)
    return_time = forms.TimeField(widget=forms.DateTimeInput)

    def clean_related_bike(self):
        return self.initial('related_bike')





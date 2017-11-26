from django.contrib.auth.models import User
from bike.models import Bike, Localization
from django.core.validators import RegexValidator

from django import forms

class BikeForm(forms.ModelForm):
    frame_number = forms.RegexField(regex=r'^[A-Z0-9]{3,15}$',
                                    error_messages=(
                                        "Frame number must consists numbers and letters"
                                    ))

    class Meta:
        model = Bike
        fields = ['producer_name',
                  'model_name',
                  'frame_number',
                  'bike_type']


class LocalizationForm(forms.ModelForm):
    class Meta:
        model = Localization
        fields = ['city',
                  'street',
                  'building_number',
                  ]



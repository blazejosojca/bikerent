from django.contrib.auth.models import User
from bike.models import Bike, Localization

from django import forms

class AddingBikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['producer_name',
                  'model_name',
                  'frame_number',
                  'bike_type']




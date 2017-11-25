from django.shortcuts import render
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import (
    ListView,
    CreateView,
    FormView,
    View
)

from .models import Bike, Localization
from .forms import AddingBikeForm


class BikesListView(ListView):
    template_name = "bike/bikes_list.html"
    ctx = "bike_list"

    def get_queryset(self):
        return Bike.objects.all()


class AddingBikeFormView(CreateView):
    template_name = 'bike/bike_form.html'
    model = Bike
    fields = ['producer_name',
              'model_name',
              'frame_number',
              'bike_type']

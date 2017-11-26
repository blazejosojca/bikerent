from django.shortcuts import render
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import (
    ListView,
    CreateView,
    FormView,
    View,
    DetailView
)

from .models import Bike, Localization


class BikesListView(ListView):
    template_name = "bike/bikes_list.html"
    ctx = "bike_list"

    def get_queryset(self):
        return Bike.objects.all()


class CreateBikeView(CreateView):
    template_name = 'bike/bike_form.html'
    model = Bike
    fields = ['producer_name',
              'model_name',
              'frame_number',
              'bike_type']


class CreateLocalizationView(CreateView):
    template_name = 'bike/localization_form.html'
    model = Localization
    fields = ['city',
              'street',
              'building_number',
              'phone_number',
              'email']


class DetailBikeView(View):

    def get(self, request, pk):
        bike = Bike.objects.get(pk=pk)
        return TemplateResponse(request, "bike/detail_bike_view.html", {
            'bike': bike,
            'bike_list': Bike.objects.all(),
            })


from django.shortcuts import render
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import (
    ListView,
    View
)

from .models import Bike, Localization

class BikesListView(ListView):
    template_name = "bike/bikes_list.html"
    ctx = "bike_list"
    
    def get_queryset(self):
        return Bike.objects.all()

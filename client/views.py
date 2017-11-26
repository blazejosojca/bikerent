from django.shortcuts import render
from .models import Client
from django.template.response import TemplateResponse
from bike.models import Bike, Localization
from django.views.generic import ListView, View


def HomePageView(request):
    ctx = {
        "info": "Hello World! "
    }
    return TemplateResponse(request,
                            "client/client_homepage.html",
                            ctx)



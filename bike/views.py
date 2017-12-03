from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    FormView,
    View,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Bike, Localization


def HomepageView(request):
        ctx = {
            "info": "Hello World!"
        }
        return TemplateResponse(request,
                                "bike/index.html",
                                ctx)


class ListBikesView(ListView):
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


class GeneralBikeView(View):

    def get(self, request, pk):
        bike = Bike.objects.get(pk=pk)
        return TemplateResponse(request, "bike/bike_general.html", {
            'bike': bike,
            'bike_list': Bike.objects.all(),
            })


class UpdateBikeView(UpdateView):
    model = Bike
    fields = ['producer_name',
              'model_name',
              'frame_number',
              'bike_type']
    template_name = 'bike/bike_update_form.html'


class DeleteBikeView(DeleteView):
    model = Bike
    success_url = 'bike/bikes_list.html'


class ServiceBikeView(DetailView):

    model = Bike

    def get_context_data(self, **kwargs):
        context = super(ServiceBikeView, self).get_context_data(**kwargs)
        return context

class UpdateServiceBikeView(UpdateView):
    pass


class HistoryBikeView(DetailView):
    pass


class RentingBikeView(View):
    pass


class UpdateRentingBikeView(View):
    pass


class ListClientView(ListView):
    pass


class DetailClientView(DetailView):
    pass


class ListStaffView(ListView):
    pass


class DetailStaffView(DetailView):
    pass


class LoginStaffView(ListView):
    pass


class LogoutStaffView(DetailView):
    pass


class LocalizationView(CreateView):
    pass


class CreateLocalizationView(CreateView):
    template_name = 'bike/localization_form.html'
    model = Localization
    fields = ['city',
              'street',
              'building_number',
              'phone_number',
              'email']


class UpdateLocalizationView(CreateView):
    pass


class DeleteLocalizationView(CreateView):
    pass




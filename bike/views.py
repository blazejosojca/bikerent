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
from .forms import BikeFormCreate, BikeFormUpdate


def HomepageView(request):
        ctx = {
            "info": "Hello World!"
        }
        return TemplateResponse(request,
                                "bike/index.html",
                                ctx)


class ListBikesView(ListView):
    template_name = "bike/bike_list.html"
    ctx = "bike_list"

    def get_queryset(self):
        return Bike.objects.all()


class CreateBikeView(CreateView):
    model = Bike
    form_class = BikeFormCreate
    template_name = 'bike/bike_form.html'
    success_url = reverse_lazy('bike:bike-list')


class DetailBikeView(DetailView):

    model = Bike

    def get_context_data(self, **kwargs):
        context = super(DetailBikeView, self).get_context_data(**kwargs)
        return context


class UpdateBikeView(UpdateView):
    model = Bike
    form_class = BikeFormUpdate
    template_name = 'bike/bike_update_form.html'
    success_url = reverse_lazy('bike:bike-list')


class DeleteBikeView(DeleteView):
    model = Bike
    success_url = reverse_lazy('bike:bike-list')


class CreateRentingBikeView(View):
    pass


class UpdateRentingBikeView(View):
    pass


class HistoryBikeView(DetailView):
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




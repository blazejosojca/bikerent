from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    View,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from client.models import Client
from .models import Bike, Localization, Renting
from .forms import (
    BikeFormCreate,
    BikeFormUpdate,
    RentingForm,
    LocalizationForm,
    RentingUpdateForm,
)

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import authenticate


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


class CreateBikeView(PermissionRequiredMixin, CreateView):
    model = Bike
    form_class = BikeFormCreate
    template_name = 'bike/bike_form.html'
    permission_required = ['add_bike']
    raise_exception = True


class DetailBikeView(DetailView):

    model = Bike

    def get_context_data(self, **kwargs):
        context = super(DetailBikeView, self).get_context_data(**kwargs)
        return context


def get_queryset(self):
        return Bike.objects.all()


class UpdateBikeView(UpdateView):
    model = Bike
    form_class = BikeFormUpdate
    template_name = 'bike/bike_update_form.html'


class DeleteBikeView(DeleteView):
    model = Bike
    success_url = reverse_lazy('bike:bike-list')


class CreateRentingBikeView(CreateView):
    model = Renting
    template_name = 'bike/renting_form.html'
    form_class = RentingForm
    success_url = reverse_lazy('bike:list-bike-renting')


class ListRentingBikeView(ListView):
    template_name = "bike/renting_list.html"
    ctx = "renting_list"

    def get_queryset(self):
        return Renting.objects.filter(return_date__isnull=True)


class UpdateRentingBikeView(UpdateView):
    model = Renting
    template_name = 'bike/renting_form.html'
    form_class = RentingUpdateForm
    success_url = reverse_lazy('bike:list-bike-renting')
# TODO stworzyć widok edycji wypożyczenia bez generyków, ściągać id roweru


class DeleteRentingBikeView(DeleteView):
    model = Renting
    success_url = reverse_lazy('bike:list-bike-renting')


class HistoryBikeView(View):
    template_name = 'bike/bike_renting_list.html'

    def get(self, request, pk):
        bike = Bike.objects.get(pk=pk)
        return render(request, self.template_name, {'bike': bike,

                                                    'renting_list': Renting.objects.filter(related_bike=pk)})


class LocalizationsList(ListView):
        template_name = "bike/localizations_list.html"
        ctx = "localization_list"

        def get_queryset(self):
            return Localization.objects.all()


class CreateLocalizationView(CreateView):
    template_name = 'bike/localization_form.html'
    model = Localization
    form_class = LocalizationForm
    success_url = reverse_lazy('bike:local-list')


class UpdateLocalizationView(UpdateView):
    model = Localization
    form_class = LocalizationForm
    template_name = 'bike/localization_form.html'
    success_url = reverse_lazy('bike:local-list')


class DeleteLocalizationView(DeleteView):
    model = Localization
    success_url = reverse_lazy('bike:local-list')




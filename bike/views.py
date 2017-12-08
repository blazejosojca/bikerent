from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    View,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Bike, Localization, Renting
from .forms import (
    BikeFormCreate,
    BikeFormUpdate,
    RentingForm
)


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
    form_class = RentingForm
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
                                                        'renting_list':Renting.objects.filter(related_bike=pk)})

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




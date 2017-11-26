from django.shortcuts import render
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


class UpdateBikeView(UpdateView):
    pass


class DeleteBikeView(DeleteView):
    pass


class ServiceBikeView(DetailView):
    pass


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

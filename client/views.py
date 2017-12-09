from django.shortcuts import render
from .models import Client
from django.template.response import TemplateResponse
from django.views.generic import (
    ListView,
    View,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)


class ListClient(View):
    pass


class CreateClient(CreateView):
    pass


class ClientDetails(DetailView):
    pass


class DeleteClient(DeleteView):
    pass


class UpdateClient(UpdateView):
    pass




from django.shortcuts import render
from .models import Client
from django.template.response import TemplateResponse
from django.views.generic import (
    ListView,
    View,
    DetailView,
    DeleteView,
    UpdateView,
)


class StartClientView(View):
    pass


class RegisterClientView(View):
    pass


class LoginClientView(View):
    pass


class LogoutClientView(View):
    pass


class ViewAccountClientView(DetailView):
    pass


class UpdateAccountClientView(UpdateView):
    pass


class DeleteAccountClientView(DeleteView):
    pass

from django.shortcuts import render
from .models import Client
from django.template.response import TemplateResponse
from bike.models import Bike, Localization
from django.views.generic import ListView, View

"""
urlpatterns = [
    url(r'^clients/$', views.StartClientView.as_view(), name="client-start"),
    url(r'^clients/register/$', views.RegisterClientView.as_view(), name="client-register"),
    url(r'^clients/login/$', views.LoginClientView.as_view(), name="client-login"),
    url(r'^clients/logout/(?P<pk>[0-9]+)/$', views.LogoutClientView.as_view(), name="client-logout"),
    url(r'^clients/account/(?P<pk>[0-9]+)/$', views.ViewAccountClientView.as_view(), name="client-account"),
    url(r'^clients/update/(?P<pk>[0-9]+)/$', views.UpdateAccountCleintView.as_view(), name="client-update"),
    url(r'^clients/delete_account/(?P<pk>[0-9]+)/$', views.DeleteAccountClientView.as_view(), name="client-delete"),
]
"""

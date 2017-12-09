from django.conf.urls import url
from . import views

app_name = "client"

urlpatterns = [
    url(r'^clients/$', views.ListClient.as_view(), name="client-list"),
    url(r'^clients/create/$', views.CreateClient.as_view(), name="client-create"),
    url(r'^clients/details/(?P<pk>[0-9]+)$', views.ClientDetails.as_view(), name="client-detail"),
    url(r'^clients/delete/(?P<pk>[0-9]+)/$', views.DeleteClient.as_view(), name="client-delete"),
    url(r'^clients/update/(?P<pk>[0-9]+)/$', views.UpdateClient.as_view(), name="client-update"),
]

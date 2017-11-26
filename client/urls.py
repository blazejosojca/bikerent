from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^client/index/$', views.ClientStartView.as_view(), name="client-start"),
    url(r'^client/register/$', views.RegisterClientView.as_view(), name="create-bike"),
    url(r'^client/$', views.CreateLocalizationView.as_view(), name="create-localization"),
    url(r'^bikes/(?P<pk>[0-9]+)/$', views.DetailBikeView.as_view(), name="bike-details"),
    url(r'^bikes/update/(?P<pk>[0-9]+)/$', views.UpdateBikeView.as_view(), name="bike-edit"),
    url(r'^bikes/delete/(?P<pk>[0-9]+)/$', views.DeleteBikeView.as_view(), name="bike-service"),

]

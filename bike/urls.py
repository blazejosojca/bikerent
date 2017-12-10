from django.conf.urls import url
from . import views

app_name = "bike"

urlpatterns = [
    url(r'^bikes/$', views.ListBikesView.as_view(), name="bike-list"),
    url(r'^bikes/add/$', views.CreateBikeView.as_view(), name="create-bike"),
    url(r'^localizations/add/$', views.CreateLocalizationView.as_view(), name="create-localization"),
    url(r'^localizations/$', views.LocalizationsList.as_view(), name="local-list"),
    url(r'^localizations/update/(?P<pk>[0-9]+)/$', views.UpdateLocalizationView.as_view(), name="update-localization"),
    url(r'^localizations/delete/(?P<pk>[0-9]+)/$', views.DeleteLocalizationView.as_view(), name="delete-localization"),
    url(r'^bikes/details/(?P<pk>[0-9]+)/$', views.DetailBikeView.as_view(), name="bike-detail"),
    url(r'^bikes/update/(?P<pk>[0-9]+)/$', views.UpdateBikeView.as_view(), name="bike-edit"),
    url(r'^bikes/delete/(?P<pk>[0-9]+)/$', views.DeleteBikeView.as_view(), name="bike-delete"),
    url(r'^bikes/history/(?P<pk>[0-9]+)/$', views.HistoryBikeView.as_view(), name="bike-history"),
    url(r'^bikes/create/renting/$', views.CreateRentingBikeView.as_view(), name="create-bike-renting"),
    url(r'^bikes/delete/renting/(?P<pk>[0-9]+)/$', views.DeleteRentingBikeView.as_view(), name="delete-bike-renting"),
    url(r'^bikes/update/renting/(?P<pk>[0-9]+)/$', views.UpdateRentingBikeView.as_view(), name="edit-bike-renting"),
    url(r'^bikes/history/renting/(?P<pk>[0-9]+)/$', views.HistoryBikeView.as_view(), name="history-bike-renting"),
    url(r'^bikes/list/renting/$', views.ListRentingBikeView.as_view(), name="list-bike-renting"),

]

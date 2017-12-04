from django.conf.urls import url
from . import views

app_name = "bike"

urlpatterns = [
    url(r'^bikes/$', views.ListBikesView.as_view(), name="bike-list"),
    url(r'^bikes/add/$', views.CreateBikeView.as_view(), name="create-bike"),
    url(r'^localizations/add/$', views.CreateLocalizationView.as_view(), name="local-list"),
    url(r'^localizations/(?P<pk>[0-9]+)/$', views.LocalizationView.as_view(), name="create-localization"),
    url(r'^localizations/update/(?P<pk>[0-9]+)/$', views.UpdateLocalizationView.as_view(), name="update-localization"),
    url(r'^localizations/delete/(?P<pk>[0-9]+)/$', views.DeleteLocalizationView.as_view(), name="delete-localization"),
    url(r'^bikes/details/(?P<pk>[0-9]+)/$', views.DetailBikeView.as_view(), name="bike-detail"),
    url(r'^bikes/update/(?P<pk>[0-9]+)/$', views.UpdateBikeView.as_view(), name="bike-edit"),
    url(r'^bikes/delete/(?P<pk>[0-9]+)/$', views.DeleteBikeView.as_view(), name="bike-delete"),
    url(r'^bikes/history/(?P<pk>[0-9]+)/$', views.HistoryBikeView.as_view(), name="bike-history"),
    url(r'^bikes/renting/(?P<pk>[0-9]+)/$', views.RentingBikeView.as_view(), name="bike-renting"),
    url(r'^bikes/renting/(?P<pk>[0-9]+)/$', views.CreateRentingBikeView.as_view(), name="create_bike-renting"),
    url(r'^bikes/renting/(?P<pk>[0-9]+)/$', views.DeleteRentingBikeView.as_view(), name="delete-bike-renting"),
    url(r'^bikes/renting/update/(?P<pk>[0-9]+)/$', views.UpdateRentingBikeView.as_view(), name="edit-bike-renting"),
    url(r'^clients/$', views.ListClientView.as_view(), name="clients-list"),
    url(r'^clients/(?P<pk>[0-9]+)/$', views.DetailClientView.as_view(), name="client-details"),
    url(r'^staff/$', views.ListStaffView.as_view(), name="staff-list"),
    url(r'^staff/(?P<pk>[0-9]+)/$', views.DetailStaffView.as_view(), name="staff-details"),
    url(r'^staff/login/$', views.LoginStaffView.as_view(), name="staff-login"),
    url(r'^staff/logout/(?P<pk>[0-9]+)/$', views.LogoutStaffView.as_view(), name="staff-logout"),

]

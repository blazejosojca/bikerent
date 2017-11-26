from django.conf.urls import url
from . import views

app_name = "bike"

urlpatterns = [
    url(r'^bikes/$', views.ListBikesView.as_view(), name="bikes-list"),
    url(r'^bikes/add/$', views.CreateBikeView.as_view(), name="create-bike"),
    url(r'^add_localization/$', views.CreateLocalizationView.as_view(), name="create-localization"),
    url(r'^bikes/(?P<pk>[0-9]+)/$', views.DetailBikeView.as_view(), name="bike-details"),
    url(r'^bikes/update/(?P<pk>[0-9]+)/$', views.UpdateBikeView.as_view(), name="bike-edit"),
    url(r'^bikes/delete/(?P<pk>[0-9]+)/$', views.DeleteBikeView.as_view(), name="bike-service"),
    url(r'^bikes/service/(?P<pk>[0-9]+)/$', views.ServiceBikeView.as_view(), name="bike-service"),
    url(r'^bikes/service/update/(?P<pk>[0-9]+)/$', views.UpdateServiceBikeView.as_view(), name="bike-edit-service"),
    url(r'^bikes/history/(?P<pk>[0-9]+)/$', views.HistoryBikeView.as_view(), name="bike-history"),
    url(r'^bikes/renting/(?P<pk>[0-9]+)/$', views.RentingBikeView.as_view(), name="bike-renting"),
    url(r'^bikes/renting/update/(?P<pk>[0-9]+)/$', views.UpdateRentingBikeView.as_view(), name="bike-edit-renting"),
    url(r'^clients/$', views.ListClientView.as_view(), name="clients-list"),
    url(r'^clients/(?P<pk>[0-9]+)/$', views.DetailClientView.as_view(), name="client-details"),
    url(r'^staff/$', views.ListStaffView.as_view(), name="staff-list"),
    url(r'^staff/(?P<pk>[0-9]+)/$', views.DetailStaffView.as_view(), name="staff-details"),
]

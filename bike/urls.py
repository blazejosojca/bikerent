from django.conf.urls import url
from . import views

app_name = "bike"

urlpatterns = [
    url(r'^bikes/$', views.BikesListView.as_view(), name="bikes-list"),
    url(r'^bikes/add/$', views.CreateBikeView.as_view(), name="create-bike"),
    url(r'^add_localization/$', views.CreateLocalizationView.as_view(), name="create-localization"),
    url(r'^bikes/(?P<pk>[0-9]+)/$', views.DetailBikeView.as_view(), name="bike-detail"),
    url(r'^bikes/update/(?P<pk>[0-9]+)/$', views.DetailBikeView.as_view(), name="bike-edit"),
    url(r'^bikes/delete/(?P<pk>[0-9]+)/$', views.DetailBikeView.as_view(), name="bike-service"),    url(r'^bikes/(?P<pk>[0-9]+)/$', views.DetailBikeView.as_view(), name="bike-detail")


]

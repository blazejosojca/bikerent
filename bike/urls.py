from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bikes_list/$', views.BikesListView.as_view(), name="bikes_list")
]

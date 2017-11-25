from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bikes_list/$', views.BikesListView.as_view(), name="bikes_list"),
    url(r'^add_bike/$', views.CreateBikeView.as_view(), name="create_bike"),
    url(r'^add_localization/$',views.CreateLocalizationView.as_view(), name="create_localization")
]

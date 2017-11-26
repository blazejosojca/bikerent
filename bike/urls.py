from django.conf.urls import url
from . import views

app_name = "bike"

urlpatterns = [
    url(r'^bikes/$', views.BikesListView.as_view(), name="bikes_list"),
    url(r'^add_bike/$', views.CreateBikeView.as_view(), name="create_bike"),
    url(r'^add_localization/$',views.CreateLocalizationView.as_view(), name="create_localization"),
    url(r'^bikes/(?P<pk>[0-9]+)/$', views.DetailBikeView.as_view(), name="bike-detail")
]

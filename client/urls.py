from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView, name="index"),
    # .url(r'register/$', views.User)


]

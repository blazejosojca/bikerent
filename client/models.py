from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Client(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.IntegerField(default=0)
    mail = models.EmailField(max_length=64)

    def __str__(self):
        return "{} {}".format(self.first_name,
                              self.last_name)

    def get_absolute_url(self):
        return reverse('client:client-list')

    @property
    def client_name(self):
        return "{} {}".format(self.first_name,
                              self.last_name)

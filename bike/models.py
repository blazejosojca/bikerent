from datetime import date
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from client.models import Client


TYPES = (
    (0, "unknown"),
    (1, "city bike"),
    (2, "cross bike"),
    (3, "trekking bike"),
    (4, "mountain terrain bike"),
    (5, "bike for kids")
)

POSITION = (
    ('BOSS', 'boss'),
    ('SERVICE', 'serviceman'),
)

STATUS = (
    ('excellent', 'excellent'),
    ('good', 'good'),
    ('poor', 'poor'),
    ('trash', 'trash'),
)


class Bike(models.Model):
    producer_name = models.CharField(max_length=64)
    model_name = models.CharField(max_length=64)
    frame_number = models.IntegerField(default=0)
    bike_type = models.TextField(choices=TYPES)
    is_rented = models.BooleanField(default=False)
    is_functional = models.BooleanField(default=True)
    renting_history = models.ManyToManyField(Client, through='Renting')

    def get_absolute_url(self):
        return reverse("bikes_list")

    def __str__(self):
        return "{} {} {}".format(self.producer_name,
                                 self.model_name,
                                 self.bike_type)


class Renting(models.Model):
    related_bike = models.ForeignKey(Bike)
    related_client = models.ForeignKey(Client)


class Service(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start = models.DateField(_("Date"), default=date.today)
    current_service = models.DateField(_("Date"), default=date.today)
    next_service = models.DateField(_("Date"), default=date.today)
    status = models.CharField(max_length=64, )


class Localization(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    building_number = models.CharField(max_length=64)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("bike_base")

    def __str__(self):
        return "{} {} {}".format(self.city,
                                 self.street,
                                 self.building_number,
                                 self.email,
                                 self.phone_number,
                                 )


class Staff(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    position = models.IntegerField(choices=POSITION)
    phone_number = models.IntegerField(default=0)
    mail = models.CharField(max_length=64)

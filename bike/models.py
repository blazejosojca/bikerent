from datetime import date
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from client.models import Client


TYPES = (
    ("Unknown", "unknown"),
    ("city", "city bike"),
    ("cross", "cross bike"),
    ("trekking", "trekking bike"),
    ("mtb", "mountain terrain bike"),
    ("kids", "bike for kids")
)

POSITION = (
    ('BOSS', 'boss'),
    ('SERVICE', 'serviceman'),
)

STATUS = (
    ('checked', 'everything is okay'),
    ('service', 'still in service'),
)


class Bike(models.Model):
    producer_name = models.CharField(max_length=64)
    model_name = models.CharField(max_length=64)
    frame_number = models.CharField(max_length=24)
    bike_type = models.CharField(max_length=24, choices=TYPES)
    is_rented = models.BooleanField(default=False)
    is_functional = models.BooleanField(default=True)
    service_date = models.DateField(_("Last service date"), default=date.today)
    next_service_date = models.DateField(_("Next service date"), default=date.today, blank=True
                                         )
    renting_history = models.ManyToManyField(Client, through='Renting')

    def get_absolute_url(self):
        return reverse("bike:bike-detail",
                       kwargs={'pk': self.pk})

    def __str__(self):
        return "{} {} {}".format(self.producer_name,
                                 self.model_name,
                                 self.bike_type)

    @property
    def bike_name(self):
        return "{} - {} - {}".format(self.producer_name,
                                     self.model_name,
                                     self.pk)


class Renting(models.Model):
    related_bike = models.ForeignKey(Bike)
    related_client = models.ForeignKey(Client)
    start_time = models.DateTimeField(auto_now=True)
    return_time = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.related_bike,
                              self.related_client)


class Localization(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    building_number = models.CharField(max_length=64)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("bike:bike_base")

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

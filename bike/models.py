from datetime import date
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.timezone import now
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


class Bike(models.Model):
    producer_name = models.CharField(max_length=64)
    model_name = models.CharField(max_length=64)
    frame_number = models.CharField(max_length=24)
    bike_type = models.CharField(max_length=24, choices=TYPES)
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
                                 self.pk)

    def bike_name(self):
        return "{} {}".format(self.producer_name,
                              self.model_name)


class Renting(models.Model):
    related_bike = models.ForeignKey(Bike)
    related_client = models.ForeignKey(Client)
    start_date = models.DateField(default=date.today)
    start_time = models.TimeField(default=now)
    rented = models.BooleanField(default=False)
    return_date = models.DateField(null=True, blank=True)
    return_time = models.TimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("bike:bike_list")

    def __str__(self):
        return "{} {}".format(self.related_bike,
                              self.related_client)

    def rent_info(self):
        return "{} {} {} {}".format(self.related_bike,
                                    self.related_client,
                                    self.start_date,
                                    self.return_date)



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




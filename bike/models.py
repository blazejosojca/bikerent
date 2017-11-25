from django.db import models
from django.urls import reverse

TYPES = (
    (0, "unknowns"),
    (1, "city bike"),
    (2, "cross bike"),
    (3, "trekking bike"),
    (4, "mountain terrain bike"),
    (5, "bike for kids")
)


class Bike(models.Model):
    producer_name = models.CharField(max_length=64)
    model_name = models.CharField(max_length=64)
    frame_number = models.IntegerField(default=0)
    bike_type = models.IntegerField(choices=TYPES)
    is_rented = models.BooleanField(default=False)
    is_functional = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("bikes_detail",
                       kwargs={'pk': self.pk})

    def __str__(self):
        return "{} {} {}".format(self.producer_name,
                                 self.model_name,
                                 self.bike_type)


class Localization(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    building_number = models.CharField(max_length=64)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    #bike_quant = models.IntegerField(default=0)


from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.IntegerField(default=0)
    mail = models.CharField(max_length=64)


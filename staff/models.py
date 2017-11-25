from django.db import models

POSITION = (
    ('0', 'boss'),
    ('1', 'serviceman'),
    ('2', 'receptionist')

)


class Staff(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    position = models.IntegerField(choices=POSITION)
    phone_number = models.IntegerField(default=0)
    mail = models.CharField(max_length=64)

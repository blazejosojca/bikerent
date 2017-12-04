from django.contrib import admin
from .models import (
    Bike,
    Localization,
    Renting,
    Staff
)

admin.site.register(Bike)
admin.site.register(Localization)
admin.site.register(Renting)
admin.site.register(Staff)

from django.contrib import admin
from .models import (
    Bike,
    Localization,
    Renting,
    Service,
    Staff
)

admin.site.register(Bike)
admin.site.register(Localization)
admin.site.register(Renting)
admin.site.register(Service)
admin.site.register(Staff)

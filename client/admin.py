from django.contrib import admin
from .models import Client, MyUser

admin.site.register(Client)
admin.site.register(MyUser)

# Register your models here.

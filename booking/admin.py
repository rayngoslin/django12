from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Room, Booking

admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Booking)
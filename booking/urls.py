from django.urls import path
from .views import booking_list, room_list, create_booking

urlpatterns = [
    path('bookings/', booking_list, name='booking_list'),
    path('rooms/', room_list, name='room_list'),
    path('bookings/new/', create_booking, name='create_booking'),
]
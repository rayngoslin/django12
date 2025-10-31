from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Room, Customer
from django import forms

# 1. View для списку бронювань
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

# 2. View для перегляду кімнат
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

# 3. View для створення бронювання (з формою)
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'room', 'check_in', 'check_out']

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

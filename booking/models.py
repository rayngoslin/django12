from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Room {self.number}"

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.customer.name} - {self.room.number} ({self.check_in} to {self.check_out})"

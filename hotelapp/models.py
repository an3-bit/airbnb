from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    # image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"

PAYMENT_METHODS = [
        ('mpesa', 'Mpesa'),
        ('card', 'Debit Card'),
    ]

class Booking(models.Model):
    arrival_date = models.DateField()
    departure_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='mpesa')
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.room} from {self.arrival_date} to {self.departure_date} - Paid: {self.paid}"
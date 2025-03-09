from django.db import models

PAYMENT_METHODS = [
        ('mpesa', 'Mpesa'),
        ('card', 'Debit Card'),
    ]

class Booking(models.Model):
    arrival_date = models.DateField()
    departure_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking from {self.arrival_date} to {self.departure_date} - Paid: {self.paid}"
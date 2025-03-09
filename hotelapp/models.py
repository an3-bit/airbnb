from django.db import models

class Booking(models.Model):
    arrival_date = models.DateField()
    departure_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking from {self.arrival_date} to {self.departure_date}"

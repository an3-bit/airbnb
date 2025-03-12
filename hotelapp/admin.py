from django.contrib import admin

from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("arrival_date", "departure_date", "total_cost", "payment_method", "paid", "created_at")
    list_filter = ("paid", "payment_method", "arrival_date", "departure_date")
    search_fields = ("arrival_date", "departure_date", "payment_method")
    ordering = ("-created_at",)
    list_editable = ("paid",)


from django.contrib import admin

from .models import Booking, Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price_per_night', 'is_available')
    list_filter = ('room_type', 'is_available')
    search_fields = ('room_number', 'room_type')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("arrival_date", "departure_date", "total_cost", "payment_method", "paid", "created_at")
    list_filter = ("paid", "payment_method", "arrival_date", "departure_date")
    search_fields = ("arrival_date", "departure_date", "payment_method")
    ordering = ("-created_at",)
    list_editable = ("paid",)


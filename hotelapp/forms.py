from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    arrival_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = ['arrival_date', 'departure_date']

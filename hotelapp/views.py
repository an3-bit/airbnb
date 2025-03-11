from django.shortcuts import render,redirect
from .forms import BookingForm
from .models import Booking

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def room(request):
    return render(request, 'room.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, 'blog.html')


def book_room(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('payment', booking_id=booking.id)  # Redirect to payment
    else:
        form = BookingForm()
    
    return render(request, 'booking.html', {'form': form})

def booking_success(request):
    return render(request, 'success.html')

def payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    
    if request.method == "POST":
        # Process payment logic here (Mpesa/Debit Card)
        booking.paid = True
        booking.save()
        return redirect('payment_success')  # Redirect after payment
    
    return render(request, 'payment.html', {'booking': booking})

def payment_view(request):
    return render(request, 'payment.html')

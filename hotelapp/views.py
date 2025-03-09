from django.shortcuts import render,redirect
from .forms import BookingForm

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
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})

def booking_success(request):
    return render(request, 'success.html')

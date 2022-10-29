from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def home(request):
    send_mail('Sending mail through django code',
              'hi,hope you this mail fall in your inbox',
              'prashanth.marolix@gmail.com',
              ['Bongonimanikanth@gmail.com','prashanthambala6@gmail.com'],
              fail_silently=False)
    return render(request,'app/home.html')


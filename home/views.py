from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request,'example.html')

def image(request):
    return render(request,'image.html')

def login(request):
    return render(request,'login.html')


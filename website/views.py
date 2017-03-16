from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Device

# Create your views here.
TEMPLATE_PATH = '/Users/dhruvilmehta/PycharmProjects/FindMyPhone-Django2/website/templates/website/'

username = 'student'


def index(request):
    user_login(request)
    return render(request, TEMPLATE_PATH + 'home.html', {})


def user_login(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                user_details = {'username': username}
                print(user_details)
                login(request, user)
                print('Success')
                return render(request, TEMPLATE_PATH + 'googlemaps.html', user_details)
            else:
                print('Account blocked')
                return render(request, TEMPLATE_PATH + 'home.html', {})
        else:
            print('Wrong details entered')
            return render(request, TEMPLATE_PATH + 'home.html', {})
    else:
        print('POST method not working')
        return render(request, TEMPLATE_PATH + 'home.html', {})


def get_location(request):
    # recieve_data(request)
    return render(request, TEMPLATE_PATH + 'googlemaps.html', {})


def recieve_data(request):
    location = {}
    if request.method == 'POST':
        current_latitude = request.POST.get('current_latitude')
        print(current_latitude)
        current_longitude = request.POST.get('current_longitude')
        print(current_longitude)
        location = {'latitude': current_latitude, 'longitude': current_longitude}
        user = User.objects.get(username=username)
        device = Device.objects.get(user=user)
        device.latitude = current_latitude
        device.longitude = current_longitude
        device.save()
        return render(request, TEMPLATE_PATH + 'googlemaps.html', location)
    else:
        print('POST method not identified')
        return render(request, TEMPLATE_PATH + 'googlemaps.html', {})

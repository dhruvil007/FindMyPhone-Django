from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Device
import requests
import json

# Create your views here.
TEMPLATE_PATH = '/Users/dhruvilmehta/PycharmProjects/FindMyPhone-Django2/website/templates/website/'

username = 'student'


def index(request):
    user_login(request)
    return render(request, TEMPLATE_PATH + 'home.html', {})


def user_login(request):
    if request.method == 'POST':
        global username
        print("Hey hey hey")
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
    print('' + request.user.username)
    user = request.user
    device = Device.objects.get(user=user)
    registration_id = device.registration_id
    print(registration_id)
    data = {'to': registration_id,
            'data': {'message': 'Press the button at the bottom to locate the phone.',
                     'ring': 'false',
                     'location': 'true'}}
    make_post_request(data)
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


def make_post_request(data):
    url = 'http://fcm.googleapis.com/fcm/send'
    headers = {'Content-Type': 'application/json',
               'Authorization': 'key=AIzaSyD6OB2ifrTrO4oMTUhJZwv7eexR39tFY0A',
               'Connection': 'close'}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response)


def make_phone_ring(request):
    user = request.user
    # user = User.objects.get(username='dhruvil')
    device = Device.objects.get(user=user)
    registration_id = device.registration_id
    print(registration_id)
    data = {'to':registration_id,
            'data':{'message':'Press the button at the bottom to locate the phone.',
                    'ring':'true',
                    'location': 'false'}}
    make_post_request(data)
    return HttpResponse("Done")


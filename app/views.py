from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework import status
import requests
import json
from rest_framework.response import Response
from .models import Device
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['POST',])
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('' + username + ' ' + password)
        registration_id = request.POST.get('token')
        user = authenticate(username=username, password=password)
        if user:
            print('User is correct')
            print('' + registration_id)
            device = Device.objects.get_or_create(user=user, registration_id=registration_id)
            return Response('login successful', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('login unsuccessful', status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def make_post_request(data):
    url = 'http://fcm.googleapis.com/fcm/send'
    headers = {'Content-Type': 'application/json',
               'Authorization': 'key=AIzaSyD6OB2ifrTrO4oMTUhJZwv7eexR39tFY0A',
               'Connection': 'close'}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response)


def make_phone_ring(request):
    # user = request.user
    user = User.objects.get(username='dhruvil')
    device = Device.objects.get(user=user)
    registration_id = device.registration_id
    print(registration_id)
    data = {'to':registration_id,
            'data':{'message':'Press the button at the bottom to locate the phone.',
                    'ring':'true'}}
    make_post_request(data)
    return HttpResponse("Done")


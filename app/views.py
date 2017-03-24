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
@api_view(['POST', ])
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


@csrf_exempt
@api_view(['POST', ])
def receive_location(request):
    # location= {}
    if request.method == 'POST':
        current_latitude = request.POST.get('latitude')
        print(current_latitude)
        current_longitude = request.POST.get('longitude')
        print(current_longitude)
        username = request.POST.get('username')
        print(username)
        location = {'latitude': current_latitude, 'longitude': current_longitude}
        user = User.objects.get(username=username)
        device = Device.objects.get(user=user)
        device.latitude = current_latitude
        device.longitude = current_longitude
        device.save()
        # js_data = json.dumps(location)
        # return render(request, TEMPLATE_PATH + 'googlemaps.html', location)
        return Response("success", status=status.HTTP_200_OK)
    else:
        return Response("failure", status=status.HTTP_405_METHOD_NOT_ALLOWED)

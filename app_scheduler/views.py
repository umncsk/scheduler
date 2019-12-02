# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Django Rest Framework views
from django.contrib.auth.models import User
from rest_framework import viewsets, status, generics
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_scheduler.models import User
from app_scheduler.serializers import UserSerializer

class DetailSchedule(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    # queryset = User.objects.all().order_by('-date_joined')
    queryset = User.objects.all()
    serializer_class = UserSerializer


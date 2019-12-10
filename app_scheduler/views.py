# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Django Rest Framework views
from django.contrib.auth.models import User
from rest_framework import viewsets
# from rest_framework.parsers import JSONParser
from app_scheduler.models import User, Group
from app_scheduler.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    # queryset = User.objects.all().order_by('-date_joined')
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

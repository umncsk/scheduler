from django.urls import path, include
from . import views
from django.contrib import admin

app_name = "scheduler"

urlpatterns = [
    path('', views.index, name='index'),
    path('scheduler/', views.execute, name="execute"),
    path("makeorg/", views.makeorg, name="makeorg"),
    path("join/", views.joinorg, name="joinorg")
]

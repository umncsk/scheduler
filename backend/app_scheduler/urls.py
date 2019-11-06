from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

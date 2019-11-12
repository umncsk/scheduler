from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    path('', views.UserSchedule.as_view()),
    path('<int:pk>/', views.DetailSchedule.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stringsapp import views

urlpatterns = [
    path('phonenumbers/', views.phonenumbers),
]

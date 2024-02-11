from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name = 'home'),
    path('result/<str:id>/',check_result, name = 'check_result'),
]
from django.urls import path
from registration import views

urlpatterns = [
    path('login/',views.signin),
    path('signup/',views.signUp),
]
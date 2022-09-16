from django.urls import path
from AppDictClaro import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
]
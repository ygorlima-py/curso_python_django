from django.urls import path
from .views import home, exemplo

urlpatterns = [
    path('home/', home),
    path('exemplo/', exemplo)
]

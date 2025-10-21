from django.urls import path
from .views import home, exemplo

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('exemplo/', exemplo, name='exemplo')
]

from django.urls import path
from .views import blog, exemplo, post

app_name = 'blog'

urlpatterns = [
    path('', blog, name='home'),
    path('post/<int:id>', post, name='post'),
    path('exemplo/', exemplo, name='exemplo')
]

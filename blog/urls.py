from django.urls import path
from .views import blog, exemplo, post

app_name = 'blog'

urlpatterns = [
    path('post/<int:post_id>/', post, name='post'),
    path('', blog, name='home'),
    path('exemplo/', exemplo, name='exemplo')
]

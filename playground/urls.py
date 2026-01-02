from django.urls import path
from . import views

# URL Conf for 'playground' app
# Each app has its own URL configuration to manage its specific routes and views.
urlpatterns = [
    path('hello/', views.say_hello, name='say_hello')
]
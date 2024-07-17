from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('mail/', send_mail, name='send_mail')
]

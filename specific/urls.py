from django.urls import path
from specific.views import *

app_name='connect2'

urlpatterns = [
    path('page2', page2, name='page2'),
]

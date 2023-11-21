from django.urls import path
from app2.views import *

app_name='connect2'

urlpatterns = [
    path('page2/',page2,name='page2'),
]

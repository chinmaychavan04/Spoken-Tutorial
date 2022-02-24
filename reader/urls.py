from django.urls import include, path
from .views import *

urlpatterns = [
    path('text/',textIp,name="textIp"),
    path('pdf/',pdfIp,name="pdfIp"),
    path('video/',videoIp,name="videoIp"),
    path('',home,name="home"),
]
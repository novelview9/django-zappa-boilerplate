from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
import requests

def index(*args, **kwargs):
    return JsonResponse(dict(site='betweenjobs server'))

def test(*args, **kwargs):
    result = requests.get('https://naver.com')
    return JsonResponse(dict(site=str(result.content)))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('test', test),
]


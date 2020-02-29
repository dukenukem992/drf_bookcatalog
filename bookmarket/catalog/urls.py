from django.contrib import admin
from django.urls import path, include

from .views import *

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()

router.register(r'books',BookView)
router.register(r'authors',AuthorView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/',include('djoser.urls.jwt'))
]

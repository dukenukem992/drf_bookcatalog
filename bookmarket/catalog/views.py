from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .serializer import *

from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission, IsAuthenticated
# Create your views here.

class BookView(mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.CreateModelMixin,
               viewsets.GenericViewSet):

            #    permission_classes = [IsAuthenticated]

               serializer_class = BookSerializer
               queryset = Book.objects.all()



class AuthorView(
    mixins.ListModelMixin,mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,mixins.DestroyModelMixin,
    mixins.CreateModelMixin,viewsets.GenericViewSet):
    
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()



# class BookViewDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'id'

# class BookViewList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
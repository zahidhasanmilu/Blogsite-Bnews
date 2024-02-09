from django.shortcuts import render

# messages
from django.contrib import messages

# models
from App_Blog.models import Blog
from App_Login.models import User_Profile

# serializers
from rest_framework import generics
from rest_framework import serializers
from apiApp.serializers import BlogSerializers, User_ProfileSerializers


class BlogApiList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class User_ProfileApiList(generics.ListAPIView):
    queryset = User_Profile.objects.all()
    serializer_class = User_ProfileSerializers

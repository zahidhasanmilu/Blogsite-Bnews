from rest_framework import serializers

from App_Blog.models import Blog
from App_Login.models import User_Profile

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('__all__')
        

class User_ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = ('__all__')
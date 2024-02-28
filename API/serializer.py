from rest_framework import serializers
from blog.models import Book
from account.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
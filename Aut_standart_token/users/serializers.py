from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *

class UserLoginSerializer(serializers.Serializer):
    user: User = None
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self,data):
        user = authenticate(**data)
        if user:
            return user
        return False
class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()
    class Meta:
        model = User
        fields = '__all__'

    def save (self,*args,**kwargs):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password!= password2:
            raise serializers.ValidationError({password: 'пароли не совпадают'})
        user.set_password(password)
        user.save()

        def __init__(self):
            self.user = user
        return self.user
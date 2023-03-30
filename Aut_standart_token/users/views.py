from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from.models import *
from.serializers import *

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['data'] = serializer.data
            user =serializer.user
            token = Token.objects.create(user=user)
            print(Token)
            return Response({'user token': token.key}, status=HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

class LoginUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]
    def post(self, request: WSGIRequest, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return JsonResponse({'error':{
                'code': 401,
                'message': 'Aunthentication failed'
            }
            })
        user = serializer.validated_data
        print('dknbgjnf', user)
        if user:
            token_object, token_created = Token.objects.get_or_create(user=user)
            token = token_object if token_object else token_created

            return Response({'user token': token.key}, status=HTTP_200_OK)
        return Response({'error':{'message': 'Aunthentication failed'}})

class LogoutUserView(ListAPIView):
    def get(self,request:WSGIRequest, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except(AttributeError, ObjectDoesNotExist):
            return JsonResponse({'error':{'code':401,'message': 'Logout failed'}}, status=401)
        logout(request)
        return JsonResponse({
            'data':
                {'message':'logout'}
        }, status=200)
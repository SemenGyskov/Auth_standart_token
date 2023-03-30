from django.urls import path
from .views import *
urlpatterns = [
    path('product/',ProductAPIView.as_view()),
    path('product/<int:pk>/',ProductUpdateAPIView.as_view()),
    path('producer/',ProducerAPIView.as_view()),
    path('producer/<int:pk>/',ProducerUpdateAPIView.as_view()),
    path('country/',CountryAPIView.as_view()),
    path('country/<int:pk>/',CountryUpdateAPIView.as_view()),
    path('order/',OrderAPIView.as_view()),
    path('order/<int:pk>/',OrderUpdateAPIView.as_view()),
    path('cart/',CartAPIView.as_view()),
    path('cart/<int:pk>/',CartUpdateAPIView.as_view()),

]

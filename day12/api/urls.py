from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken

from api import views

urlpatterns = [
    # path('login/', ObtainJSONWebToken.as_view()),
    path('demo/', views.UserDetailAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('com/', views.ComputerListAPIView.as_view()),
]
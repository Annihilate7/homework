from django.urls import path

from app import views

urlpatterns = [
    path('stu/', views.StudentAPIView.as_view()),
    path('stu/<str:id>/', views.StudentAPIView.as_view()),
    path('stu_del/', views.StudentAPIView.as_view()),
    path('stu_del/<str:id>/', views.StudentAPIView.as_view()),
]
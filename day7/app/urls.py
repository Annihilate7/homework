from django.urls import path

from app import views

urlpatterns = [
    path("users/", views.user),

    path("user_view/", views.UserView.as_view()),
    path("user_view/<str:id>/", views.UserView.as_view()),

    path("user_del/", views.UserView.as_view()),
    path("user_del/<str:username>/", views.UserView.as_view()),

    path("student/", views.StudentAPIView.as_view()),
]
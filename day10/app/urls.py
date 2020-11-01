from django.urls import path

from app import views

urlpatterns = [
    path('books/', views.BookGenericAPIView.as_view()),
    path('books/<str:id>/', views.BookGenericAPIView.as_view()),
    path('register/', views.UserSetAPIView.as_view({'post': 'register'})),
    path('login/', views.UserGetAPIView.as_view({'post': 'login'})),
]
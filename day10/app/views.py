import re

from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework.response import Response

from app.models import Book, User
from app.serializers import BookModelSerializer, UserModelSerializer


class BookGenericAPIView(GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin):
    queryset = Book.objects.filter()
    serializer_class = BookModelSerializer

    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserSetAPIView(viewsets.ViewSet):

    def register(self, request, *args, **kwargs):
        request_data = request.data
        username = request_data.get('username')
        if not re.search(u'^[_a-zA-Z0-9\u4e00-\u9fa5]+$', username):
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '用户名含有非法字符'
            })
        if User.objects.filter(username=request_data.get('username')):
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '用户名已存在，换一个试试？'
            })
        user_model_serializer = UserModelSerializer(data=request_data)
        user_model_serializer.is_valid(raise_exception=True)
        user_obj = user_model_serializer.save()
        return Response({
            'status': status.HTTP_200_OK,
            'message': '注册成功',
            'result': UserModelSerializer(user_obj).data
        })


class UserGetAPIView(viewsets.ViewSet):

    def login(self, request, *args, **kwargs):
        request_data = request.data
        user_obj = User.objects.filter(username=request_data.get('username'), password=request_data.get('password'))
        if user_obj:
            user_data = UserModelSerializer(request_data).data
            return Response({
                'status': status.HTTP_200_OK,
                'message': '登陆成功',
                'result': user_data
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': '登陆失败，请检查用户名或密码！'
        })
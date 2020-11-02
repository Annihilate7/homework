from rest_framework.response import Response
from rest_framework.views import APIView

from app.authentications import MyAuth
from app.models import User
from app.permission import MyPermission
from app.throttle import SendMessageRate


class UserAPIView(APIView):

    # def get(self, request, *args, **kwargs):
    #     user = User.objects.first()
    #     print(user)
    #     print(user.phone)
    #     print(user.groups.first())
    #     print(user.user_permissions.first())
    #
    #     return Response('everything is ok')

    # authentication_classes = [MyAuth]
    # permission_classes = [MyPermission]

    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        print("读请求")
        return Response("读请求")

    def post(self, request, *args, **kwargs):
        print("写请求")
        return Response("写请求")
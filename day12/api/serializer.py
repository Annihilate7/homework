import re

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from api.models import User, Computer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserModelSerializer(ModelSerializer):

    content = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["content", "password", "username", "phone", "email"]

        extra_kwargs = {
            "username": {
                "read_only": True
            },
            "phone": {
                "read_only": True
            },
            "email": {
                "read_only": True
            },
        }

    def validate(self, attrs):
        content = attrs.get("content")
        password = attrs.get("password")

        if re.match(r'1[3-9][0-9]{9}', content):
            user_obj = User.objects.filter(phone=content).first()
        elif re.match(r'.+@.+', content):
            user_obj = User.objects.filter(email=content).first()
        else:
            user_obj = User.objects.filter(username=content).first()


        if user_obj and user_obj.check_password(password):

            payload = jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)
            self.obj = user_obj
            self.token = token

        return attrs


class ComputerModelSerializer(ModelSerializer):
    class Meta:
        model = Computer
        fields = ("name", "price", "brand")

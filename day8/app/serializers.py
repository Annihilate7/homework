from django.conf import settings
from rest_framework import serializers

from app.models import Student


class StudentSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField()

    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):
        return "%s%s%s" % ("http://127.0.0.1:8000/", settings.MEDIA_URL, str(obj.pic))


class StudentDeSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField()
    gender = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
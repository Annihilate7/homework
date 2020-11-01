from rest_framework import serializers, exceptions

from app.models import Book, User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

        extra_kwargs = {
            'password': {
                "write_only": True
            }
        }


class BookListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        for index,obj in enumerate(instance):
            self.child.updata(obj, validated_data[index])

        return instance


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        book_list_serializer = BookListSerializer
        fields = ("book_name", "price", "p", "press_name", "author_list")

        extra_kwargs = {
            "book_name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "必须提供图书名",
                    "min_length": "图书名不能少于两个字符"
                },
            },
            "p": {
                "read_only": True
            },
            "press_name": {
                "read_only": True
            },
            "author_list": {
                "read_only": True
            }
        }
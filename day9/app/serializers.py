from rest_framework import serializers, exceptions

from app.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_name', 'price', 'pho', 'author', 'presses', 'authors', 'Presses')

        extra_kwargs = {
            "book_name": {
                "required": True,
                "min_length": 1,
                "error_messages": {
                    "required": "图书名必须提供",
                    "min_length": "图书名不能少于一个字符",
                }
            },
            'pic':{
                'read_only': True
            },
            'author': {
                'read_only': True
            },
            'presses': {
                'read_only': True
            },
            "authors": {
                "write_only": True
            },
            "Presses": {
                "write_only": True
            },
        }

    def validate(self, attrs):
        return attrs

    def validate_book_name(self, value):
        # book = Book.objects.filter(book_name=value)
        # if book:
        #     raise exceptions.ValidationError('图书已存在')
        return value
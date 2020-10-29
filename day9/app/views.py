from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Book
from app.serializers import BookModelSerializer


class BookAPIView(APIView):

    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            book = Book.objects.get(pk=book_id, is_delete=False)
            book_data = BookModelSerializer(book).data
            return Response({
                'status': 200,
                'message': '查询单本图书成功',
                'result': book_data
            })
        books = Book.objects.filter(is_delete=False)
        books_data = BookModelSerializer(books, many=True).data
        return Response({
            'status': 200,
            'message': '查询所有图书成功',
            'result': books_data
        })

    def post(self, request, *args, **kwargs):
        request_data = request.data
        if isinstance(request_data, dict):
            flag = False
        elif isinstance(request_data, list):
            flag = True
        else:
            return Response({
                'status': 400,
                'message': '参数有误，添加失败'
            })
        serializer = BookModelSerializer(data=request_data, many=flag)
        serializer.is_valid(raise_exception=True)
        books = serializer.save()

        return Response({
            'status': 200,
            'message': '图书添加成功',
            'result': BookModelSerializer(books, many=flag).data
        })

    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            book_ids = [book_id]
        else:
            book_ids = request.data.get('ids')
        books = Book.objects.filter(pk__in=book_ids, is_delete=False).update(is_delete=True)
        if books:
            return Response({
                'status': 200,
                'message': '删除成功'
            })
        return Response({
            'status': 400,
            'message': '删除失败，图书不存在'
        })

    def put(self, request, *args, **kwargs):
        book_id = kwargs.get("id")
        request_data = request.data
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                'status': 400,
                'message': '图书不存在'
            })
        serializer = BookModelSerializer(data=request_data, instance=book)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': 200,
            'message': '修改成功',
            'result': BookModelSerializer(book).data
        })

    def patch(self, request, *args, **kwargs):
        book_id = kwargs.get("id")
        request_data = request.data
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                'status': 400,
                'message': '图书不存在'
            })
        serializer = BookModelSerializer(data=request_data, instance=book, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': 200,
            'message': '修改成功',
            'result': BookModelSerializer(book).data
        })
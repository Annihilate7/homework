from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Student
from app.serializers import StudentSerializer, StudentDeSerializer


class StudentAPIView(APIView):

    def get(self, request, *args, **kwargs):
        stu_id = kwargs.get('id')
        if stu_id:
            try:
                stu_obj = Student.objects.get(pk=stu_id)
                stu_serializer = StudentSerializer(stu_obj).data
                return Response({
                    'status': 200,
                    'message': '查询单个学生成功',
                    'results': stu_serializer,
                })
            except:
                return Response({
                    'status': 400,
                    'message': '此学生不存在，查询失败'
                })
        else:
            stu_obj = Student.objects.all()
            stu_serializer = StudentSerializer(stu_obj, many=True).data
            return Response({
                'status': 200,
                'message': '查询所有学生成功',
                'results': stu_serializer,
            })

    def post(self, request, *args, **kwargs):

        request_data = request.data
        if not isinstance(request_data, dict) or request_data == {}:
            return Response({
                "status": 400,
                "message": "参数有误"
            })
        stu_de_ser = StudentDeSerializer(data=request_data)

        if stu_de_ser.is_valid():
            stu_ser = stu_de_ser.save()
            return Response({
                'status': 200,
                'message': '学生添加成功',
                'results': StudentSerializer(stu_ser).data
            })
        else:
            return Response({
                'status': 400,
                'message': '学生添加失败',
                'result': stu_de_ser.errors
            })

    def delete(self, request, *args, **kwargs):
        stu_id = kwargs.get('id')
        if stu_id:
            try:
                stu_obj = Student.objects.get(pk=stu_id)
                stu_ser = StudentSerializer(stu_obj).data
            except:
                return Response({
                    'status': 400,
                    'message': '此学生不存在，删除失败'
                })
            try:
                stu_obj.delete()
                return Response({
                    'status': 200,
                    'message': '删除单个学生成功',
                    'result': stu_ser
                })
            except:
                return Response({
                    'status': 400,
                    'message': '删除单个学生失败'
                })
        else:
            stu_obj = Student.objects.all()
            stu_ser = StudentSerializer(stu_obj, many=True).data
            try:
                stu_obj.delete()
                return Response({
                    'status': 200,
                    'message': '删除所有学生成功',
                    'result': stu_ser
                })
            except:
                return Response({
                    'status': 400,
                    'message': '删除所有学生失败'
                })
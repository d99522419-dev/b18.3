from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import StudentSerializer,TeacherSerializer,GroupSerializer
from main.models import Student,Teacher,Group
from rest_framework import status
from rest_framework.permissions import  IsAuthenticated, AllowAny, IsAdminUser

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def students_list(request):
    students = Student.objects.all()
    serializers = StudentSerializer(students, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def teachers_list(request):
    teachers = Teacher.objects.all()
    serializers = TeacherSerializer(teachers, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def groups_list(request):
    groups = Group.objects.all()
    serializers = GroupSerializer(groups, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def student_detail(request,pk):
    student = Student.objects.get(pk=pk)
    serializers = StudentSerializer(student)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def teachers_detail(request,pk):
    teachers = Teacher.objects.get(pk=pk)
    serializers = TeacherSerializer(teachers)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def groups_detail(request,pk):
    groups = Group.objects.get(pk=pk)
    serializers = GroupSerializer(groups)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def student_create(request):
    serializers = StudentSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def teacher_create(request):
    serializers = TeacherSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def group_create(request):
    print(request.data)
    serializers = GroupSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def student_delete(request,pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return Response({"detail":"No content"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def teacher_delete(request,pk):
    teacher = Teacher.objects.get(pk=pk)
    teacher.delete()
    return Response({"detail":"No content"}, status=status.HTTP_204_NO_CONTENT)    


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def group_delete(request,pk):
    group = Group.objects.get(pk=pk)
    group.delete()
    return Response({"detail":"No content"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def student_update(request,pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def teacher_update(request,pk): 
    teacher = Teacher.objects.get(pk=pk)
    serializer = TeacherSerializer(teacher, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def group_update(request,pk):
    group = Group.objects.get(pk=pk)
    serializer = GroupSerializer(group, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

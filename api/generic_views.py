from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from api.serializers import StudentModelSerializer,GroupModelSerializer, TeacherModelSerializer
from main.models import Student, Group, Teacher

from rest_framework.permissions import IsAuthenticated, AllowAny,IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.decorators import permission_classes, api_view


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = (IsAuthenticated,)
    

class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = (IsAdminUser,)
    
class StudentUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = (IsAdminUser,)
    
    
    
class StudentDestroyView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = (IsAdminUser,)
    
    
class StudentRetrieveView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = (IsAdminUser,)
    
    
class GroupListCreateView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    permission_classes = (IsAdminUser,)
    
    
class GroupDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_permissions(self):
        if self.request.method in ["PUT", "PATH" "DELETE"]:
            return [IsAdminUser()]
        return super().get_permissions()
    
    
class TeacherListCreateView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherModelSerializer
    permission_classes = (IsAuthenticated,)
        
    def get_permissions(self):
            if self.request.method in "POST":
                return [IsAdminUser()]
            return super().get_permissions()
    
    
class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherModelSerializer
    permission_classes = (IsAuthenticated,)
        
    def get_permissions(self):
            if self.request.method in ["PUT", "PATH" "DELETE"]:
                return [IsAdminUser()]
            return super().get_permissions()
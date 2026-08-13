from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from main.models import Student, Group, Teacher
from .serializers import StudentModelSerializer, TeacherModelSerializer, GroupModelSerializer
from .paginations import SimplePagePagination
from rest_framework.permissions import  IsAuthenticated, AllowAny, IsAdminUser
from .permission import IsSuperUser, IsOwner



class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    pagination_class = SimplePagePagination
    permission_classes = (IsAuthenticated,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend )
    filters_fields = ("age", "group", "group__mentor")
    search_fields = ("first_name", "last_name", "group__name")
    ordering_fields = ("id", "first_name", "last_name", "age")

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            return [IsAdminUser()]
        elif self.action in [ "delete"]:
            return [IsSuperUser()]
        return super().get_permissions()


class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend )
    filters_fields = ("course", "mentor")
    search_fields = ("mentor__name", "course", "name")
    ordering_fields = ("contract", "name", "start_date")

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()


class TeacherView(ReadOnlyModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend )
    filters_fields = ("direction")
    search_fields = ("direction", "first_name")
    ordering_fields = ("direction", "first_name")

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()
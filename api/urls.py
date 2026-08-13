from django.urls import path,include
from .api_views import students_list, teachers_list, groups_list,student_create,teacher_create,group_create,student_detail,teachers_detail,groups_detail,student_update,teacher_update,group_update,student_delete,teacher_delete,group_delete
from rest_framework.routers import DefaultRouter



from api import generic_views, viewsets

router = DefaultRouter()
router.register("students", viewsets.StudentView, basename="students")
router.register("groups", viewsets.GroupView, basename="groups")
router.register("teachers", viewsets.TeacherView, basename="teachers")

urlpatterns = [
    path('', include('api.yasg')),
    path('', include(router.urls)),
    path('auth/', include('api.auth.urls')),
    
    
    #<-----> STUDENT  FBV<-----> 
    # path('students/', students_list),
    # path('student/create/', student_create),
    # path('students/<int:pk>/', student_detail),
    # path('student/update/<int:pk>/', student_update),
    # path('student/delete/<int:pk>/', student_delete),

    # <-----> STUDENT CBV<-----> #
    # path('students/', generic_views.StudentListView.as_view()),
    # path('student/create/', generic_views.StudentCreateView.as_view()),
    # path('students/<int:pk>/', generic_views.StudentRetrieveView.as_view()),
    # path('student/update/<int:pk>/',generic_views.StudentUpdateView.as_view()),
    # path('student/delete/<int:pk>/', generic_views.StudentDestroyView.as_view()),
    
    # <-----> TEACHER FBV<-----> #
    # path('teachers/', teachers_list),
    # path('teachers/create/', teacher_create),
    # path('teacher/<int:pk>/', teachers_detail),
    # path('teacher/update/<int:pk>/', teacher_update),
    # path('teacher/delete/<int:pk>/', teacher_delete),
    
    # # <-----> TEACHER CBV<-----> #
    # path('Teacher/', generic_views.TeacherListCreateView.as_view()),
    # path('Teacher/<int:pk>/',generic_views.TeacherListCreateView.as_view()),

    # <-----> GROUP FBV<-----> #
    # path('groups/', groups_list),
    # path('groups/create/', group_create),
    # path('groups/<int:pk>/', groups_detail),
    # path('group/update/<int:pk>/', group_update),
    # path('group/delete/<int:pk>/', group_delete)
    
    # <-----> GROUP CBV<-----> #
    # path('groups/', generic_views.GroupListCreateView.as_view()),
    # path('groups/<int:pk>/',generic_views.GroupListCreateView.as_view()),
]
 
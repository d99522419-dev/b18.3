"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import main,about,student_detail,create_student,update_student, update_teacher, update_group
from django.urls import include



urlpatterns = [
    path("main/", main, name="main"),
    path("about/",about),
    path("student-create/", create_student , name="student_create"),
    path("student-detail/<int:id>/", student_detail, name="student_detail"),
    path('students/<int:pk>/update/', update_student, name='update_student'),
    path('teacher/<int:pk>/update/', update_teacher, name='update_teacher'),
    path('group/<int:pk>/update/', update_group, name='update_group'),
    path('admin/', admin.site.urls),
    path("api/v1/", include("api.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
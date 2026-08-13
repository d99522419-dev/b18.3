from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from .models import Student, Group,StudentMark,Teacher

# Register your models here.

class StudentMarkInline(admin.TabularInline):
    model = StudentMark
    extra = 1
    
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id","first_name" , "last_name" , "age" , "phone_number" , "group", "get_avatar")
    search_fields = ("id","first_name" , "last_name" ,"phone_number")
    list_filter = ("group" , )
    # exclude = ("age" , "parent_phone_number",)
    # list_per_page = 2
    @admin.display(description="Аватар")
    def get_avatar(self, student):
        if student.avatar:
            return mark_safe(
                f'<img src="{student.avatar.url}" width="100" height="100" />'
                )
        return "Нет аватара"
    
    
class GroupAdmin(admin.ModelAdmin):
    list_display = ( "name" , "course" , "start_date" , "students_count" , "mentor")
    search_fields = ( "name" , "course" , "mentor__first_name")
    list_filter = ("mentor",)
    readonly_fields = ("created_at",)                                       


class StudentMarkAdmin(admin.ModelAdmin):
    list_display = ("id","first_name", "student","last_name" , "phone_number" , "group", "get_avatar")
    list_display_links  = ("id","first_name",)
    search_fields = ("first_name", "last_name" ,"phone_number")
    list_filter = ("group",)
    
    # def has_change_permission(self, request, obj = ...):
    #     return False
    # def has_add_permission(self, request):
    #     return False
    # def has_delete_permission(self, request, obj = ...):
    #     return False
    # def has_view_permission(self, request, obj = ...):
    #     return False
    
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "direction")
    search_fields = ("first_name", "direction")
    list_filter = ("direction",)
    
admin.site.register(Student , StudentAdmin)
admin.site.register(Group , GroupAdmin)
admin.site.register(StudentMark , )
admin.site.register(Teacher , TeacherAdmin)

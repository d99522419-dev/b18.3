from django.shortcuts import render, redirect

# Create your views here.
from main.models import Student, Group, Teacher, StudentMark


def about(request):
    return render(request, 'about.html')

def main(request):
    students_list = Student.objects.all()
    return render(request, 'index.html', {
        "students_list": students_list
    })
    

def student_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'student_detail.html', {
        "student": student
    })

def create_student(request):        
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        phone_number = request.POST.get("phone_number")
        parent_phone_number = request.POST.get("parent_phone_number")
        group_id = request.POST.get("group")
        avatar = request.FILES.get("avatar")       
        
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            phone_number=phone_number,
            parent_phone_number=parent_phone_number,
            group_id=group_id,
            avatar=avatar
        )
        return redirect('main')
    
    groups = Group.objects.all()
    return render(request, 'create_student.html', {"groups": groups})


def create_teacher(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        direction = request.POST.get("direction")
        avatar = request.FILES.get("avatar")       
        
        Teacher.objects.create(
            first_name=first_name,
            direction=direction,
            avatar=avatar
        )
        return redirect('main')
    return render(request, 'create_teacher.html')


def create_student_mark(request):
    if request.method == "POST":
        mark = request.POST.get("mark")
        student_id = request.POST.get("student")

        StudentMark.objects.create(
            mark=mark,
            student_id=student_id
        )
        return redirect('main')
    
    students = Student.objects.all()
    return render(request, 'create_mark.html', {"students": students})


def update_student(request,pk):
    student = Student.objects.get(id=pk)
    groups = Group.objects.all()

    if request.method == "POST":
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.age = request.POST.get("age")
        student.phone_number = request.POST.get("phone_number")
        student.parent_phone_number = request.POST.get("parent_phone_number")
        student.group_id = request.POST.get("group")

        if request.FILES.get('avatar'):
            student.avatar = request.FILES.get('avatar')

        student.save()
        return redirect('main')
    
    return render(request, 'update_student.html', {'student': student, 'groups': groups})


def update_teacher(request,pk):
    teacher = Teacher.objects.get(id=pk)
    
    if request.method == "POST":
        teacher.first_name = request.POST.get("first_name")
        teacher.last_name = request.POST.get("last_name")
        teacher.age = request.POST.get("age")
        teacher.phone_number = request.POST.get("phone_number")
        
        if request.FILES.get('avatar'):
            teacher.avatar = request.FILES.get('avatar')

        teacher.save()
        return redirect('main') 

    return render(request, 'update_teacher.html', {'teacher': teacher})

def update_group(request,pk):
    group = Group.objects.get(id=pk)
    
    if request.method == "POST":
        group.name = request.POST.get("name")
        group.save()
        return redirect('main') 

    return render(request, 'update_group.html', {'group': group})   
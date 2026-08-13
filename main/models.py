from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.  
class Student(models.Model):
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', blank=True, null=True)
    first_name = models.CharField(max_length=300,verbose_name= "Имя")
    last_name = models.CharField(max_length=200,verbose_name= "Фамилия")
    age = models.IntegerField(verbose_name= "Возраст",blank=True,null=True)
    phone_number = models.CharField(max_length=20,verbose_name= "Номер телефона")
    parent_phone_number = models.CharField(max_length=20,verbose_name= "Номер телефона родителей",blank=True, null=True)
    group = models.ForeignKey("Group" , on_delete=models.CASCADE,verbose_name='Группа',blank=True, null=True)
    
    
    # def clean(self):
    #     if self.marks.count() > 5:
    #         raise ValidationError("У студента не может быть больше 5 оценок.")

    # def save(self):
    #     self.full_clean()
    #     super().save()
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

class StudentMark(models.Model):
    mark = models.PositiveBigIntegerField(verbose_name="")
    student = models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name='Студент', related_name='marks',)
    
    class Meta: 
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

class Group(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(verbose_name='Дата начала',null=True,blank=True )
    end_date = models.DateField(verbose_name='Дата окончания',null=True,blank=True)
    course = models.CharField(max_length=100,verbose_name='Курс',null=True,blank=True)
    students_count = models.IntegerField(verbose_name='Количество учеников',null=True,blank=True)
    contract = models.FloatField(verbose_name='Контракт',default=8000,null=True,blank=True)
    mentor = models.ForeignKey("Teacher", on_delete=models.SET_NULL,verbose_name="Ментор",null=True,blank=True,related_name="groups")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания',null=True,blank=True)
    
    def __str__(self):
        return self.name
    class Meta :
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        

class Teacher(models.Model):
    DIRECTION_CHOICES = (
        ("be" , "Back-End"),
        ("fe","Front-End"),
        ("smm","SMM")
    )
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', blank=True, null=True)
    first_name = models.CharField(verbose_name='Имя')
    direction = models.CharField(verbose_name="направление",choices=DIRECTION_CHOICES)

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
    def __str__(self):
        return f"{self.first_name} - {self.direction}"
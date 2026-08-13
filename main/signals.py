import os

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete,pre_delete

from main.models import Student,Teacher



@receiver(pre_delete, sender=Student)
def delete_student_image(sender, instance: Student, **kwargs):
    if instance.avatar:
        print(f'{settings.BASE_DIR}{instance.avatar.url}')
        os.remove(f'{settings.BASE_DIR}{instance.avatar.url}')
        
        
        
@receiver(pre_delete, sender=Teacher)
def delete_teacher_image(sender, instance: Teacher, **kwargs):
    if instance.avatar:
        print(f'{settings.BASE_DIR}{instance.avatar.url}')
        os.remove(f'{settings.BASE_DIR}{instance.avatar.url}') 
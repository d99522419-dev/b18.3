from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
import random

from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from datetime import timedelta


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, email, password, **extra_fields):
        if email is None :
            raise ValueError("Email must be set")
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        
    username = None
    email = models.EmailField(verbose_name=_('Email'), unique=True,blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name=_('Номер телефона'), unique=True, blank=True, null=True)
    avatar = ResizedImageField(size=[500,500], crop=['middle','center',], upload_to='avatars/',
                               force_format='WEBP',quality=90, verbose_name='Аватар',
                               null=True , blank=True )
    date_of_birth = models.DateField(verbose_name=_('Дата рождения'), null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f'{self.first_name} - {str(self.email)}'


class OTPCode(models.Model):

    email = models.EmailField()
    code = models.CharField(max_length=6)
    create_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def sava(self, *args, **kwagregs):
        if not self.expired_at:
            self.expired_at = timezone.now() + timedelta(minutes=5)
        super().save(*args, **kwagregs)

    def is_expired(self):
        return timezone.now() - timedelta(minutes=5)

    def str(self):
        return f"{self.email} - {self.code}"

class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_code():
        return str(random.randint(100000, 999999))

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=5)
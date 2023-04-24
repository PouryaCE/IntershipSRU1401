from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser):
    gender_choices = (
        ('m', 'male'),
        ('f', 'female'),
        ('n', None)
    )
    username = models.CharField(max_length=100, unique=True)
    national_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True, max_length=200)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    birthday_date = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=gender_choices, default='n')
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number", "email"]


    objects = UserManager()

    def __str__(self):
        return f'{self.first_name}-{self.last_name}-{self.national_code}'

    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True


    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        return self.is_admin
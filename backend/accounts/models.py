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
    


class Role(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


class Operation(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


class RoleOperation(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role")
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name="operation")


class ExtraUserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_to_info')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_to_info')
    student_id = models.CharField(max_length=10, null=True, blank=True)
    field = models.CharField(max_length=200, null=True, blank=True)
    city_name = models.CharField(max_length=200, null=True, blank=True)
    proffesor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proffesor', null=True, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher', null=True, blank=True)
    region = models.PositiveSmallIntegerField(null=True, blank=True)
    job_title = models.CharField(max_length=200, null=True, blank=True)



class StudentActivity(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    is_done =  models.BooleanField(default=False)
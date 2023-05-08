from django.db import models
from accounts.models import Student, OfficeManager
# Create your models here.
from accounts.models import User


class Report (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    attachments = models.FileField()
    deadline_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class FormsRollCall(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_to_forms")
    enter_time = models.DateTimeField()
    exit_time = models.DateTimeField()


class ReportStudent (models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_to_report")
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="report_to_student")
    is_done = models.BooleanField(default=False)


class Summery (models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="summery_to_student")
    content = models.CharField(max_length=100)


class Request (models.Model):
    text = models.TextField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="office_request_school")


class Request_Office(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_request_office")
    office_manager = models.ForeignKey(OfficeManager, on_delete=models.CASCADE, related_name="office_request_student")

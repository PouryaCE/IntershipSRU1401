from django.contrib import admin
from .models import Report, FormsRollCall, ReportStudent, Summery, Request, Request_Office
# Register your models here.
admin.site.register(Report)
admin.site.register(FormsRollCall)
admin.site.register(ReportStudent)
admin.site.register(Summery)
admin.site.register(Request)
admin.site.register(Request_Office)
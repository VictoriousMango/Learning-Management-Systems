from django.contrib import admin
from administration.models import Users, Courses, Assessments, Submissions

# Register your models here.
admin.site.register(Users)
admin.site.register(Courses)
admin.site.register(Assessments)
admin.site.register(Submissions)


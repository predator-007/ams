from django.contrib import admin
from .models import StudentList, attendance ,tattendance
# Register your models here.
admin.site.register(StudentList)

admin.site.register(attendance)

admin.site.register(tattendance)

from django import forms
from home_app.models import StudentList,attendance

class attendanceform(forms.ModelForm):
    class Meta:
        model = attendance
        fields = ['sroll','sname','status']

class addstudentform(forms.ModelForm):
    class Meta:
        model = StudentList
        fields =['ssec','sroll','sname']
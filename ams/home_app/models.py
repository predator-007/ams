from django.db import models
from django.utils.timezone import now
from datetime import date
class StudentList(models.Model):
    ssec = models.CharField(max_length= 10 , default= "enter sec in 'sec_a' format")
    sroll = models.CharField(max_length=10 , default = "enter rno in '18H51A05C.' format",unique=True)
    sname = models.CharField(max_length=25 , )
    semail = models.EmailField(max_length=254,default="")
    def __str__(self):
        return self.sroll


class tattendance(models.Model):
    sroll = models.CharField(max_length=10 , default = "")
    sname = models.CharField(max_length=25 , default = "")
    date = models.CharField(max_length=25 , default = "")
    status = models.CharField(max_length=25 , default = "")
    subject = models.CharField(max_length=25 , default = "")
    """class Meta:
        unique_together = ['date','sroll']"""
    def __str__(self):
        return self.sname + ' '+str(self.date)
        

class attendance(models.Model):
    sroll = models.CharField(max_length=10 , default = "")
    sname = models.CharField(max_length=25 , default = "")
    date = models.CharField(max_length=25 , default = "")
    status = models.CharField(max_length=25 , default = "")
    subject = models.CharField(max_length=25 , default = "")
    """class Meta:
        unique_together = ['date','sroll']"""
    def __str__(self):
        return self.sname + ' '+str(self.date)
    
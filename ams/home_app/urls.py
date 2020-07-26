from django.urls import path

from . import views

urlpatterns = [
    path("", views.home ,name="home"),
    path("welcome",views.welcome , name="welcome"),
    path("viewslist", views.viewslist , name="viewslist"),
    path("addstudent", views.addstudent ,name = "addstudent"),
    path("delete/<task_id>", views.deletestudent, name="deletestudent"),
    path("edit/<task_id>", views.editstudent, name="editstudent"),
    path("editattendance",views.editattendance , name="editattendance"),
    path("takeattendance",views.takeattendance , name="takeattendance"),
    path('viewstudentshome',views.viewstudentshome , name="viewstudentshome"),
    path("edittattendance/<task_id>",views.edittattendance , name="edittattendance"),
    path("studentattendance",views.studentattendance,name="studentattendance"),
    path("studentoverallattendance",views.studentoverallattendance,name="studentoverallattendance"),
    path("downloadstudents/<section>",views.downloadstudents , name="downloadstudents"),
    path("downloadstudentattendance/<isroll>", views.downloadstudentattendance, name="downloadstudentattendance"),
    
]

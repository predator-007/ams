from django.shortcuts import render,redirect
from django.http import HttpResponse
from home_app.models import StudentList,attendance,tattendance
from home_app.forms import attendanceform,addstudentform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import csv
from django.contrib.auth.models import User
import datetime
from django.core.mail import EmailMessage

def home(request):
    return render(request,"home.html")

@login_required
def welcome(request):
    return render(request,"welcome.html")

@login_required
def viewstudentshome(request):
    isection = request.POST.get('section')
    slist = StudentList.objects.filter(ssec=isection).order_by('sroll')
    context={
            'slist':slist,
            'isection':isection,   
    }
    return render(request ,"viewstudentshome.html",context)

@login_required
def viewslist(request):
    slist = StudentList.objects.all
    return render(request, "viewstudentlist.html",{'slist':slist})

@login_required
def addstudent(request):
    if request.method == "POST":
        if request.POST.get('ssec') and request.POST.get('sroll') and request.POST.get('sname'):
            obj = StudentList()
            obj.ssec = request.POST.get('ssec')
            obj.sroll = request.POST.get('sroll')
            obj.sname = request.POST.get('sname')
            obj.semail = request.POST.get('semail')
            obj.save()
            messages.success(request,("student added succesfully "))
            return redirect("addstudent")
        else:
            return redirect("addstudent")
    else:
        slist = StudentList.objects.all
        return render(request, "addstudent.html",{'slist':slist})


@login_required
def deletestudent(request,task_id):
    obj = StudentList.objects.get(pk=task_id)
    obj.delete()
    return redirect('addstudent')


@login_required
def editstudent(request,task_id):
    if request.method == "POST":
        obj = StudentList.objects.get(pk=task_id)
        obj.ssec = request.POST.get('ssec')
        obj.sroll = request.POST.get('sroll')
        obj.sname = request.POST.get('sname')
        obj.save()
        messages.success(request,("student edited!"))
        return redirect('addstudent')
    else:
        obj = StudentList.objects.get(pk=task_id)
        return render(request, 'editstudent.html', {'obj': obj} )

@login_required
def takeattendance(request):
    if request.method == "POST": 
        tattendance.objects.all().delete()       
        section = request.POST.get("section")
        sub = request.POST.get("subject")
        x=datetime.date.today()
        d=x.strftime("%Y-%m-%d")
        slists = StudentList.objects.filter(ssec=section).order_by('sroll')
        for slist in slists.iterator():
            att_obj = tattendance()
            att_obj.sroll = slist.sroll
            att_obj.sname = slist.sname
            att_obj.status = "Present"
            att_obj.subject = sub
            att_obj.date = d
            att_obj.save()
        obj1= tattendance.objects.all()
        return render(request, "takeattendance.html",{'obj1':obj1})
    else:
        obj1= tattendance.objects.all()
        return render(request, "takeattendance.html",{'obj1':obj1})

@login_required
def edittattendance(request,task_id):
    obj = tattendance.objects.get(pk=task_id)
    if obj.status=="Present":
        obj.status = "Absent"
    else:
        obj.status = "Present"
    obj.save()          
    return redirect('takeattendance')


@login_required
def studentattendance(request):
    if request.method=="POST":
        isroll=request.POST.get("sroll")
        idate = request.POST.get('date')
        isubject = request.POST.get("subject")
        obj1=attendance.objects.filter(date=idate)
        obj3=obj1.filter(sroll=isroll)
        obj2=obj3.filter(subject=isubject)
        return render(request,"studentattendance.html",{'obj2':obj2})
    else:
        obj=[]
        return render(request,"studentattendance.html",{'obj':obj})


@login_required
def editattendance(request):
    obj1 = tattendance.objects.all()
    #toemail=[]
    for obj in obj1:
        att_obj = attendance()
        att_obj.sroll = obj.sroll
        att_obj.sname = obj.sname
        att_obj.status = obj.status
        att_obj.subject = obj.subject
        att_obj.date = obj.date
        if obj.status=="Absent":
            slists = StudentList.objects.filter(sroll=obj.sroll)
            for s in slists.iterator():
                e= s.semail
            #toemail.append(e)
            msg = EmailMessage("Absent Remainder","Hello "+obj.sname+" you were absent for "+obj.subject+
            " subject on "+obj.date+".",to=[e])
            msg.send()
        att_obj.save()
    tattendance.objects.all().delete()             
    return redirect('takeattendance')
    


@login_required
def downloadstudents(request,section):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    writer = csv.writer(response)
    writer.writerow(['Section', 'Roll NO', 'Name'])
    slist = StudentList.objects.filter(ssec=section).order_by('sroll').values_list('ssec', 'sroll', 'sname')
    for st in slist:
        writer.writerow(st)
    return response
    return redirect('viewstudentshome')


@login_required
def studentoverallattendance(request):
    isroll = request.POST.get("sroll")
    objs = attendance.objects.filter(sroll=isroll)
    c1=0
    c2=0
    sub=[]
    sub1={}
    sub2={}
    for obj in objs.iterator():
        if obj.subject not in sub:
            sub.append(obj.subject)
        if obj.subject not in sub1:
            if obj.status == "Present":
                sub1[obj.subject]=1
                c1+=1
            else:
                sub1[obj.subject]=0
            sub2[obj.subject]=1
        else:
            if obj.status == "Present":
                sub1[obj.subject]+=1
                c1+=1
            sub2[obj.subject]+=1
        c2+=1
    print(c1,c2)
    psub=[]
    for k in sub:
        if sub1[k]==0:
            p=0
        else:
            p=(sub1[k]/sub2[k])*100
        p=round(p,2)
        psub.append(p)
    print(psub)
    if c1==0:
        ptotal=0
    else:
        ptotal=(c1/c2)*100
    ptotal=round(ptotal,2)
    print(ptotal)

    context={
                'isroll':isroll,
                'sub':sub,
                'sub1':sub1,
                'sub2':sub2,
                'psub':psub,
                'ptotal':ptotal,
        }
    return render(request,"studentoverallattendance.html",context)
    
    
@login_required
def downloadstudentattendance(request,isroll):
    objs = attendance.objects.filter(sroll=isroll)
    c1=0
    c2=0
    sub=[]
    sub1={}
    sub2={}
    for obj in objs.iterator():
        if obj.subject not in sub:
            sub.append(obj.subject)
        if obj.subject not in sub1:
            if obj.status == "Present":
                sub1[obj.subject]=1
                c1+=1
            else:
                sub1[obj.subject]=0
            sub2[obj.subject]=1
        else:
            if obj.status == "Present":
                sub1[obj.subject]+=1
                c1+=1
            sub2[obj.subject]+=1
        c2+=1
    psub=[]
    for k in sub:
        if sub1[k]==0:
            p=0
        else:
            p=(sub1[k]/sub2[k])*100
        p=round(p,2)
        psub.append(p)
    print(psub)
    if c1==0:
        ptotal=0
    else:
        ptotal=(c1/c2)*100
    ptotal=round(ptotal,2)
    print(ptotal)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="StudentAttenance.csv"'
    writer = csv.writer(response)
    sub.append("")
    writer.writerow(sub)
    tsub1=list(sub1.values())
    tsub1.insert(0,"Classes attended")
    tsub2=list(sub2.values())
    tsub2.insert(0,"Total classes")
    writer.writerow(tsub1)
    writer.writerow(tsub2)
    tpsub=psub[:]
    tpsub.insert(0,"percentage")
    writer.writerow(tpsub)
    tptotal=[]
    tptotal.append("Total Percentage")
    tptotal.append(ptotal)
    writer.writerow(tptotal)
    return response
    
       
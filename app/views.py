from django.shortcuts import render,redirect
from app.forms import Schedule_New_Course_Form,Student_Registration_Form
from app.models import Course_Model,Student_Model,Enrolled_Courses
from django.contrib import messages

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def admin_login_page(request):
    return render(request,"admin_login.html")


def validate_admin(request):
    username=request.POST.get("uname")
    password=request.POST.get("upass")
    if username=="Raj" and password=="Raj123":
        return render(request,"welcome_admin.html")
    else:
        return render(request,"admin_login.html",{"error":"Invalid Credentials"})


def schedule_new_class_page(request):
    return render(request,"schedule_new_class.html")


def admin_schedule_new_class(request):
    schedule_course=Schedule_New_Course_Form(request.POST)
    if schedule_course.is_valid():
        schedule_course.save()
        return render(request,"schedule_new_class.html",{"success":"Course Scheduled Successfully"})
    else:
        return render(request,"schedule_new_class.html",{"error":schedule_course.errors})


def welcome_admin(request):
    return render(request,"welcome_admin.html")


def admin_view_scheduled_classes(request):
    cm=Course_Model.objects.all()
    return render(request,"view_all_classes.html",{"details":cm})


def admin_delete_class(request):
    course_id=int(request.GET.get("cid"))
    cm1=Course_Model.objects.get(id=course_id).delete()
    fun=admin_view_scheduled_classes(request)
    return fun


def save_student(request):
    sr=Student_Registration_Form(request.POST)
    if sr.is_valid():
        sr.save()
        return render(request,"student_registration.html",{"success":"Registered Successfully"})
    else:
        return render(request,"student_registration.html",{"error":"Something Went Wrong. Please try Again"})

s_name=""
s_id=None
def validate_student(request):
    global s_name,s_id
    email=request.POST.get("email")
    password=request.POST.get("password")
    try:
        sm=Student_Model.objects.get(email=email,password=password)
        s_name=sm.name
        s_id=sm.idno
        return render(request,"student_home.html",{"name":s_name})

    except Student_Model.DoesNotExist:
        return render(request,"student_login.html",{"error":"Invalid Credentials"})

msg=""
def student_enroll_course_page(request):
    cm = Course_Model.objects.all()
    return render(request, "student_enroll_course_page.html", {"details": cm})


def student_enroll_course(request):
    course_id=request.GET.get("cid")
    cm=Course_Model.objects.get(id=int(course_id))
    try:
        ec1 = Enrolled_Courses.objects.get(student_id=s_id, course_name=cm.name, faculty_name=cm.faculty_name)
        cm = Course_Model.objects.all()
        return render(request, "student_enroll_course_page.html", {"details": cm,"enrolled":"Already Enrolled"})
    except Enrolled_Courses.DoesNotExist:
        ec = Enrolled_Courses(course_name=cm.name, faculty_name=cm.faculty_name, date=cm.date, time=cm.time,
                              fees=cm.fees, duration=cm.duration)
        ec.save()
        ec.student_id.set(str(s_id))
        cm = Course_Model.objects.all()
        return render(request, "student_enroll_course_page.html", {"details": cm, "enroll_now": "Enrolled Successfully"})


def student_view_enroll_courses(request):
    ec=Enrolled_Courses.objects.filter(student_id=s_id)
    return render(request,"student_view_enrolled_courses.html",{"courses":ec})


def student_cancel_enrolled_course_page(request):
    ec = Enrolled_Courses.objects.filter(student_id=s_id)
    return render(request, "student_cancel_enrolled_courses_page.html", {"courses": ec})


def student_cancel_enrolled_course(request):
    enrolled_course_id=request.GET.get("id")
    Enrolled_Courses.objects.get(id=enrolled_course_id).delete()
    ec = Enrolled_Courses.objects.filter(student_id=s_id)
    return render(request, "student_cancel_enrolled_courses_page.html", {"courses": ec,"unenrolled":"UnEnrolled Successfully"})

course_id=None
def admin_update_class_page(request):
    global course_id
    course_id = int(request.GET.get("cid"))
    cm = Course_Model.objects.filter(id=course_id)
    return render(request,"admin_update_scheduled_class.html",{"data":cm})


def admin_update_scheduled_class(request):
    name=request.POST.get("name")
    f_name=request.POST.get("faculty_name")
    date=request.POST.get("date")
    time=request.POST.get("time")
    fees=request.POST.get("fees")
    duration=request.POST.get("duration")
    cm=Course_Model.objects.get(id=course_id)
    cm.name=name
    cm.faculty_name=f_name
    cm.date=date
    cm.time=time
    cm.fees=fees
    cm.duration=duration
    cm.save()
    cm = Course_Model.objects.all()
    return render(request,"view_all_classes.html",{"updated":"Updated Successfully","details": cm})
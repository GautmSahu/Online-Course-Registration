"""Online_Course_Registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name="index"),
    path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
    path('validate_admin/',views.validate_admin,name="validate_admin"),
    path('schedule_new_class_page/',views.schedule_new_class_page,name="schedule_new_class_page"),
    path('admin_schedule_new_class/',views.admin_schedule_new_class,name="admin_schedule_new_class"),
    path('welcome_admin/',views.welcome_admin,name="welcome_admin"),
    path('admin_view_scheduled_classes/',views.admin_view_scheduled_classes,name="admin_view_scheduled_classes"),
    path('admin_delete_class/',views.admin_delete_class,name="admin_delete_class"),
    path('student_registration/',TemplateView.as_view(template_name="student_registration.html"),name="student_registration"),
    path('save_student/',views.save_student,name="save_student"),
    path('student_login_page/',TemplateView.as_view(template_name="student_login.html"),name="student_login_page"),
    path('validate_student/',views.validate_student,name="validate_student"),
    path('student_home/',TemplateView.as_view(template_name="student_home.html"),name="student_home"),
    path('student_enroll_course_page/',views.student_enroll_course_page,name="student_enroll_course_page"),
    path('student_enroll_course/',views.student_enroll_course,name="student_enroll_course"),
    path('student_view_enroll_courses/',views.student_view_enroll_courses,name="student_view_enroll_courses"),
    path('student_cancel_enrolled_course_page/',views.student_cancel_enrolled_course_page,name="student_cancel_enrolled_course_page"),
    path('student_cancel_enrolled_course/',views.student_cancel_enrolled_course,name="student_cancel_enrolled_course"),
    path('admin_update_class/',views.admin_update_class_page,name="admin_update_class"),
    path('admin_update_scheduled_class/',views.admin_update_scheduled_class,name="admin_update_scheduled_class")

]

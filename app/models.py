from django.db import models

class Course_Model(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default=None)
    faculty_name=models.CharField(max_length=100,default=None)
    date=models.DateField(default=None)
    time=models.CharField(max_length=10,default=None)
    fees=models.FloatField(default=None)
    duration=models.IntegerField(default=None)

# class CommonModel(models.Model):
#     idno= models.AutoField(primary_key=True)
#     name=models.CharField(max_length=50)
#     contact=models.IntegerField(unique=True)
#     subject=models.CharField(max_length=60)
#
#     class Meta:
#         abstract=True

# class Faculty_Model(CommonModel):
#     salary=models.FloatField()
#     subject = models.ManyToManyField(Course_Model)

class Student_Model(models.Model):
    idno= models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    contact=models.IntegerField(unique=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50,default=None)

class Enrolled_Courses(models.Model):
    course_name = models.CharField(max_length=50, default=None)
    faculty_name = models.CharField(max_length=100, default=None)
    date = models.DateField(default=None)
    time = models.CharField(max_length=10, default=None)
    fees = models.FloatField(default=None)
    duration = models.IntegerField(default=None)
    student_id=models.ManyToManyField(Student_Model)


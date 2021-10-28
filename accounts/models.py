from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_Student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    fullname=models.CharField(max_length=100)
    EmpCode=models.CharField(max_length=100)
    Designation=models.CharField(max_length=100)
    Phone=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    SubjectHandling=models.CharField(max_length=100)
    JoiningDate=models.DateField()


    def __str__(self):
        return self.fullname

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    FullName=models.CharField(max_length=100)
    Regno=models.CharField(max_length=100   )
    Rollno=models.CharField(max_length=100)
    Section=models.CharField(max_length=10)
    Course=models.CharField(max_length=100,default="MCA")
    AcademicYear=models.CharField(max_length=100)
    DOB=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100 ,default="Male")
    Fathername=models.CharField(max_length=100)
    Mothername=models.CharField(max_length=100)
    community=models.CharField(max_length=100)
    Address=models.CharField(max_length=150)
    studentphone=models.CharField(max_length=100)
    parentphone=models.CharField(max_length=100)
    DateofAdmission=models.CharField(max_length=100)
    Hosteller=models.CharField(max_length=100)
    Occupation=models.CharField(max_length=100)
    State = models.CharField(max_length=20)

    def __str__(self):
        return self.FullName
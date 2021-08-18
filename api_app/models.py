from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100,)
    Standard=models.CharField(max_length=20)
    Gender=models.CharField(max_length=10)
    DOB=models.DateField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    name=models.ForeignKey(Student,on_delete=models.CASCADE)
    attendence=models.DateField()
    def __str__(self):
        return self.name
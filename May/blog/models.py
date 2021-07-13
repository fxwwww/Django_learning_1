from django.db import models

# Create your models here.
class Student(models.Model):
    studentname = models.CharField(max_length=32)
    studentid=models.CharField(max_length=32)
    password= models.CharField(max_length=32)

    def __str__(self):
        return '{},{}'.format(self.studentid,self.studentname)
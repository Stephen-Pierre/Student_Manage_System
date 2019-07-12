from django.db import models

# Create your models here.


class Grades(models.Model):

    grades_name = models.CharField(max_length=20, null=False)


class Students(models.Model):
    student_name = models.CharField(max_length=15, null=False)
    student_grade = models.ForeignKey('Grades', on_delete=models.CASCADE)

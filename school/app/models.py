from django.db import models

# Create your models here.

class Students(models.Model):

    stu_no = models.CharField(max_length=20, primary_key=True,unique=True)
    stu_name = models.CharField(max_length=20)
    stu_age = models.IntegerField()
    stu_tel = models.CharField(max_length=11)
    classes = models.ForeignKey('Classes')
    college = models.ForeignKey('College')
    course = models.ManyToManyField('Course')

class Course(models.Model):
    course_id = models.CharField(max_length=10,primary_key=True,unique=True)
    course_name =models.CharField(max_length=20)
    teachers = models.ForeignKey('Teachers')

# class Choice(models.Model):
#     students = models.ForeignKey('Students',on_delete='CASCADE')
#     course = models.ForeignKey('Course', on_delete='CASCADE')
class Classes(models.Model):
    classes_id = models.CharField(max_length=20,primary_key=True)
    classes_name = models.CharField(max_length=20)
    students_sum = models.IntegerField()
    teachers = models.ManyToManyField('Teachers')

class Teachers(models.Model):
    teachers_id = models.CharField(max_length=20,primary_key=True)
    teachers_name = models.CharField(max_length=10)

class College(models.Model):
    college_id = models.CharField(max_length=10,primary_key=True)
    college_name = models.CharField(max_length=20)
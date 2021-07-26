from django.db import models

class ClassRoom (models.Model):
    classRoomName = models.CharField(max_length=30,null=True)
    '''def __str__(self):
        return self.classRoomName'''

class Subject (models.Model):
    subjectName = models.CharField(max_length=30,null=True)
    classRoomName = models.CharField(max_length=30,default="",null=True)
    '''def __str__(self):
        return self.subjectName'''

class Grade (models.Model):
    gradeName = models.CharField(max_length=30,null=True)
    '''def __str__(self):
        return self.gradeName'''


class Student (models.Model):
    studentName = models.CharField(max_length=30,null=True)
    birthdate = models.DateField(null=True)
    #studentSubjects = models.ManyToManyField(Subject)
    studentSubjects = models.CharField(max_length=30, default="",null=True)
    studentGrade = models.CharField(max_length=20,default="",null=True)
    '''def __str__(self):
        return self.studentName'''

class Teacher (models.Model):
    teacherName = models.CharField(max_length=30,null=True)
    #teacherSubjects = models.ManyToManyField(Subject)
    teacherSubjects = models.CharField(max_length=30, default="",null=True)
    '''def __str__(self):
        return self.teacherName'''

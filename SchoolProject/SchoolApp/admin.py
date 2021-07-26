from django.contrib import admin
from .models import Student, Subject,Teacher,ClassRoom,Grade

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.register(Grade)
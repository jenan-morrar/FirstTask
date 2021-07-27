from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject,Student,ClassRoom,Teacher,Grade

def index (request):
    return  render(request,'index.html')

def about (request):
    return render(request,'about.html')

def contact (request):
    return  render(request,'contact.html')

def news (request):
    return  render(request,'news.html')

# For List entities
def student (request):
    studs = Student.objects.all()
    return  render(request,'student.html',{'studs':studs})

def teacher (request):
    techs = Teacher.objects.all()
    #teacherSubjects = Subject.objects.all()
    context = {'techs':techs}
    return  render(request,'teacher.html',context)

def subject (request):
    subs = Subject.objects.all()
    return  render(request,'subject.html',{'subs':subs})

def classRoom (request):
    cRooms = ClassRoom.objects.all()
    return  render(request,'classRoom.html',{'cRooms':cRooms})

def grade (request):
    grds = Grade.objects.all()
    return  render(request,'grade.html',{'grds':grds})

# For Add/Update entities
def studentForm (request):
    studs = Student.objects.all()
    subs = Subject.objects.all()
    grds = Grade.objects.all()
    context = {'studs': studs, 'subs': subs, 'grds': grds}
    if request.method == "POST":
        studentInfo = Student.objects.create (studentName=request.POST.get('StudentName'), birthdate=request.POST.get('Birthdate'), studentSubjects=request.POST.get('StudentSubject'), studentGrade=request.POST.get('StudentGrade'))
    return  render(request,'studentForm.html',context)

def teacherForm (request):
    if request.method == "POST":
       teacherInfo = Teacher.objects.create (teacherName=request.POST.get('TeacherName'), teacherSubjects=request.POST.get('TeacherSubjects'))
    return  render(request,'teacherForm.html')

def subjectForm (request):
    clsRoom = ClassRoom.objects.all()
    if request.method == "POST":
      subjectInfo = Subject.objects.create (subjectName=request.POST.get('SubjectName'),classRoomName=request.POST.get('ClassRoomName'))
      print(request.POST.get('ClassRoomName'))

    return  render(request,'subjectForm.html',{'clsRoom':clsRoom})

def classRoomForm (request):
    if request.method == "POST":
      roomName = ClassRoom.objects.create(classRoomName=request.POST.get('RoomName'))
    return render(request, 'classRoomForm.html')

def gradeForm (request):
    if request.method == "POST":
      gradeName = Grade.objects.create(gradeName=request.POST.get('GradeName'))
    return render(request, 'gradeForm.html')



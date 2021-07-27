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
    if request.method == "POST":
       studentInfo = Student.objects.create (studentName=request.POST.get('StudentName'), birthdate=request.POST.get('Birthdate'), studentSubjects=request.POST.get('StudentSubject'), studentGrade=request.POST.get('StudentGrade'))
    return  render(request,'studentForm.html')

def teacherForm (request):
    if request.method == "POST":
       teacherInfo = Teacher.objects.create (teacherName=request.POST.get('TeacherName'), teacherSubjects=request.POST.get('TeacherSubjects'))
    return  render(request,'teacherForm.html')

def subjectForm (request):
    if request.method == "POST":
      subjectInfo = Subject.objects.create (subjectName=request.POST.get('SubjectName'),classRoomName=request.POST.get('ClassRoomName'))
    return  render(request,'subjectForm.html')

def classRoomForm (request):
    if request.method == "POST":
      roomName = ClassRoom.objects.create(classRoomName=request.POST.get('RoomName'))
    return render(request, 'classRoomForm.html')

def gradeForm (request):
    if request.method == "POST":
      gradeName = Grade.objects.create(gradeName=request.POST.get('GradeName'))
    return render(request, 'gradeForm.html')


"""def forms (request):
    if request.method == 'POST':
        if 'classRoomButton' in request.POST:
            roomName = ClassRoom.objects.create(classRoomName= request.POST.get('RoomName'))
            return render(request,'forms.html')
        if 'GradeButton' in request.POST:
            gradeName = Grade.objects.create(gradeName=request.POST.get('GradeName'))
            return render(request,'forms.html')
    return render(request,'forms.html')"""


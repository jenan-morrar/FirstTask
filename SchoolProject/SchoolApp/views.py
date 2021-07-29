from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject,Student,ClassRoom,Teacher,Grade
from .forms import gradeForms
from django.contrib import messages

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
    subs = Subject.objects.all()
    grds = Grade.objects.all()
    context = {'subs': subs, 'grds': grds}
    if request.method == "POST":
        #studentInfo = Student.objects.create (studentName=request.POST.get('StudentName'), birthdate=request.POST.get('Birthdate'), studentSubjects=request.POST.get('StudentSubject'), studentGrade=request.POST.get('StudentGrade'))
        studentGrade = request.POST.get('StudentGrade')
        studentGradeObject = Grade.objects.get(gradeName=studentGrade)
        studentInfo = Student.objects.create(studentName=request.POST.get('StudentName'), birthdate=request.POST.get('StudentBirthdate'),studentGrade=studentGradeObject )
        studentSubject=request.POST.get('StudentSubject')
        studentSubjectObject = Subject.objects.get(subjectName=studentSubject)
        studentInfo.studentSubjects.add(studentSubjectObject)
        #studentInfo.studentGrade.add(studentGradeObject)
    return  render(request,'studentForm.html',context)

def teacherForm (request):
    subs = Subject.objects.all()
    if request.method == "POST":
       #teacherInfo = Teacher.objects.create (teacherName=request.POST.get('TeacherName'), teacherSubjects=request.POST.get('TeacherSubjects'))
       teacherInfo = Teacher.objects.create(teacherName=request.POST.get('TeacherName'))
       subject = request.POST.get('TeacherSubjects')
       subjectObject = Subject.objects.get(subjectName=subject)
       teacherInfo.teacherSubjects.add(subjectObject)
    return  render(request,'teacherForm.html', {'subs':subs})

def subjectForm (request):
    clsRoom = ClassRoom.objects.all()
    if request.method == "POST":
      subjectInfo = Subject.objects.create (subjectName=request.POST.get('SubjectName'))
      subjectClassRoom = request.POST.get('SubjectClassRoom')
      subjectClassRoomObject = ClassRoom.objects.get(classRoomName=subjectClassRoom)
      subjectInfo = Subject.objects.create(subjectName=request.POST.get('SubjectName'),classRoomName=subjectClassRoomObject)
      #subjectInfo.classRoomName.add(subjectClassRoomObject)

    return  render(request,'subjectForm.html',{'clsRoom':clsRoom})

def classRoomForm (request):
    if request.method == "POST":
      roomName = ClassRoom.objects.create(classRoomName=request.POST.get('RoomName'))
    return render(request, 'classRoomForm.html')

def gradeForm (request):
    if request.method == "POST":
        if request.POST.get('AddGrade'):
           gradeName = Grade.objects.create(gradeName=request.POST.get('GradeName'))
           return render(request, 'gradeForm.html')
        elif request.POST.get('UpdateGrade'):
              grdName = Grade.objects.get(gradeName='UpdateGradeName')
              form = gradeForms(request.POST,instance=grdName)
              if form.is_valid():
                  form.save()
                  messages.success(request,"Grade Updated Successfully")
                  return render(request, 'gradeForm.html', {'grdName': grdName})
    return render(request, 'gradeForm.html')



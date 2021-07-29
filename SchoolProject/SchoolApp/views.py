from django.shortcuts import render

from .models import Subject, Student, ClassRoom, Teacher, Grade


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    return render(request, 'news.html')


# For List entities
def student(request):
    studs = Student.objects.all()
    return render(request, 'student.html', {'studs': studs})


def teacher(request):
    techs = Teacher.objects.all()
    # teacherSubjects = Subject.objects.all()
    context = {'techs': techs}
    return render(request, 'teacher.html', context)


def subject(request):
    subs = Subject.objects.all()
    return render(request, 'subject.html', {'subs': subs})


def classRoom(request):
    cRooms = ClassRoom.objects.all()
    return render(request, 'classRoom.html', {'cRooms': cRooms})


def grade(request):
    grds = Grade.objects.all()
    return render(request, 'grade.html', {'grds': grds})


# For Add/Update entities
def studentForm(request):
    subs = Subject.objects.all()
    grds = Grade.objects.all()
    context = {'subs': subs, 'grds': grds}
    if request.method == "POST":
        if request.POST.get('AddStudent'):
            # studentInfo = Student.objects.create (studentName=request.POST.get('StudentName'), birthdate=request.POST.get('Birthdate'), studentSubjects=request.POST.get('StudentSubject'), studentGrade=request.POST.get('StudentGrade'))
            studentGrade = request.POST.get('StudentGrade')
            studentGradeObject = Grade.objects.get(gradeName=studentGrade)
            studentInfo = Student.objects.create(studentName=request.POST.get('StudentName'),
                                                 birthdate=request.POST.get('StudentBirthdate'),
                                                 studentGrade=studentGradeObject)
            studentSubject = request.POST.get('StudentSubject')
            studentSubjectObject = Subject.objects.get(subjectName=studentSubject)
            studentInfo.studentSubjects.add(studentSubjectObject)
            # studentInfo.studentGrade.add(studentGradeObject)
        elif request.POST.get('UpdateStudent'):
            studentName = request.POST.get('UpdateStudentName')
            to_edit = Student.objects.get(studentName=studentName)
            updatedStudentName = request.POST.get('NewStudentName')
            updatedStudentBirthdate = request.POST.get('NewStudentBirthdate')
            #updatedStudentSubject = request.POST.get('NewStudentSubject')
            #updatedStudentSubjectObject = Subject.objects.get(subjectName=updatedStudentSubject)
            updatedStudentGrade =request.POST.get('NewStudentGrade')
            updatedStudentGradeObject = Grade.objects.get(gradeName=updatedStudentGrade)
            studentSubject = request.POST.get('NewStudentSubject')
            studentSubjectObject = Subject.objects.get(subjectName=studentSubject)
            to_edit.studentSubjects.add(studentSubjectObject)
            to_edit.studentName = updatedStudentName
            to_edit.birthdate = updatedStudentBirthdate
            to_edit.studentGrade = updatedStudentGradeObject
            to_edit.save()
    return render(request, 'studentForm.html', context)


def teacherForm(request):
    subs = Subject.objects.all()
    if request.method == "POST":
      if request.POST.get('AddTeacher'):
        # teacherInfo = Teacher.objects.create (teacherName=request.POST.get('TeacherName'), teacherSubjects=request.POST.get('TeacherSubjects'))
        teacherInfo = Teacher.objects.create(teacherName=request.POST.get('TeacherName'))
        subject = request.POST.get('TeacherSubjects')
        subjectObject = Subject.objects.get(subjectName=subject)
        teacherInfo.teacherSubjects.add(subjectObject)
      elif request.POST.get('UpdateTeacher'):
          teacherName = request.POST.get('UpdateTeacherName')
          to_edit = Teacher.objects.get(teacherName=teacherName)
          updatedTeacherName = request.POST.get('NewTeacherName')
          updatedTeacherSubject = request.POST.get('NewTeacherSubject')
          updatedTeacherSubjectObject = Subject.objects.get(subjectName=updatedTeacherSubject)
          to_edit.teacherName = updatedTeacherName
          to_edit.teacherSubjects.add(updatedTeacherSubjectObject)
          to_edit.save()
    return render(request, 'teacherForm.html', {'subs': subs})


def subjectForm(request):
    clsRoom = ClassRoom.objects.all()
    if request.method == "POST":
      if request.POST.get('AddSubject'):
        subjectClassRoom = request.POST.get('SubjectClassRoom')
        subjectClassRoomObject = ClassRoom.objects.get(classRoomName=subjectClassRoom)
        subjectInfo = Subject.objects.create(subjectName=request.POST.get('SubjectName'),
                                             classRoomName=subjectClassRoomObject)
      elif request.POST.get('UpdateSubject'):
          SubjectName = request.POST.get('UpdateSubjectName')
          to_edit = Subject.objects.get(subjectName=SubjectName)
          updatedSubjectName = request.POST.get('NewSubjectName')
          updatedSubjectClass = request.POST.get('NewSubjectClassRoom')
          updatedSubjectClassObject = ClassRoom.objects.get(classRoomName=updatedSubjectClass)
          to_edit.subjectName = updatedSubjectName
          to_edit.classRoomName = updatedSubjectClassObject
          to_edit.save()


    return render(request, 'subjectForm.html', {'clsRoom': clsRoom})


def classRoomForm(request):
    if request.method == "POST":
        if request.POST.get('AddClassRoom'):
            roomName = ClassRoom.objects.create(classRoomName=request.POST.get('RoomName'))
        elif request.POST.get('UpdateClassRoom'):
            className = request.POST.get('UpdateRoomName')
            to_edit = ClassRoom.objects.get(classRoomName=className)
            updatedClass = request.POST.get('NewRoomName')
            to_edit.classRoomName = updatedClass
            to_edit.save()

    return render(request, 'classRoomForm.html')


def gradeForm(request):
    if request.method == "POST":
        if request.POST.get('AddGrade'):
            gradeName = Grade.objects.create(gradeName=request.POST.get('GradeName'))
            return render(request, 'gradeForm.html')
        elif request.POST.get('UpdateGrade'):
            gradeName = request.POST.get('UpdateGradeName')
            to_edit = Grade.objects.get(gradeName=gradeName)
            updatedGrade = request.POST.get('NewGradeName')
            to_edit.gradeName = updatedGrade
            to_edit.save()
            """ grade = Grade.objects.get('UpdateGradeName')
            print(grade)
            to_update = Grade.objects.filter(gradeName='UpdateGradeName').update(gradeName=request.POST.get('NewGradeName'))"""

            """  grdName = Grade.objects.get(gradeName='UpdateGradeName')
              form = gradeForms(request.POST,instance=grdName)
              if form.is_valid():
                  form.save()
                  messages.success(request,"Grade Updated Successfully")
                  return render(request, 'gradeForm.html', {'grdName': grdName})"""

    return render(request, 'gradeForm.html')

from django.shortcuts import render, redirect
from django.views.generic.edit import View
from django.contrib import messages
from .models import Subject, Student, ClassRoom, Teacher, Grade


class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class about(View, ):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')


class news(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news.html')


# For List entities
class student(View):
    def get(self, request, *args, **kwargs):
        studs = Student.objects.all()
        return render(request, 'student.html', {'studs': studs})


class teacher(View):
    def get(self, request, *args, **kwargs):
        techs = Teacher.objects.all()
        # teacherSubjects = Subject.objects.all()
        context = {'techs': techs}
        return render(request, 'teacher.html', context)


class subject(View):
    def get(self, request, *args, **kwargs):
        subs = Subject.objects.all()
        return render(request, 'subject.html', {'subs': subs})


class classRoom(View):
    def get(self, request, *args, **kwargs):
        cRooms = ClassRoom.objects.all()
        return render(request, 'classRoom.html', {'cRooms': cRooms})


class grade(View):
    def get(self, request, *args, **kwargs):
        grds = Grade.objects.all()
        return render(request, 'grade.html', {'grds': grds})


# For Add/Update entities
class studentForm(View):
    template_name = 'studentForm.html'
    subs = Subject.objects.all()
    grds = Grade.objects.all()
    studentSearch = "Enter Student Name"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {'subs': self.subs, 'grds': self.grds, 'studentSearch': self.studentSearch})

    def post(self, request, *args, **kwargs):
        if request.POST.get('search'):
            studentName = request.POST.get('UpdateStudentName')
            self.studentSearch = Student.objects.get(studentName=studentName)
            return render(request, self.template_name,
                          {'subs': self.subs, 'grds': self.grds, 'studentSearch': self.studentSearch})
        if request.POST.get('AddStudent'):
            if Student.objects.filter(studentName=request.POST.get('StudentName')).exists():
                messages.error(request, 'The Student already exists!', extra_tags='add')
            else:
                studentGrade = request.POST.get('StudentGrade')
                studentGradeObject = Grade.objects.get(gradeName=studentGrade)
                studentInfo = Student.objects.create(studentName=request.POST.get('StudentName'),
                                                     birthdate=request.POST.get('StudentBirthdate'),
                                                     studentGrade=studentGradeObject)
                studentSubject = request.POST.get('StudentSubject')
                studentSubjectObject = Subject.objects.get(subjectName=studentSubject)
                studentInfo.studentSubjects.add(studentSubjectObject)
                messages.success(request, 'The Student was successfully added!', extra_tags='add')
        elif request.POST.get('UpdateStudent'):
            if Student.objects.filter(studentName=request.POST.get('UpdateStudentName')).exists():
                studentName = request.POST.get('UpdateStudentName')
                to_edit = Student.objects.get(studentName=studentName)
                updatedStudentName = request.POST.get('NewStudentName')
                updatedStudentBirthdate = request.POST.get('NewStudentBirthdate')
                updatedStudentGrade = request.POST.get('NewStudentGrade')
                updatedStudentGradeObject = Grade.objects.get(gradeName=updatedStudentGrade)
                studentSubject = request.POST.get('NewStudentSubject')
                studentSubjectObject = Subject.objects.get(subjectName=studentSubject)
                to_edit.studentSubjects.add(studentSubjectObject)
                to_edit.studentName = updatedStudentName
                to_edit.birthdate = updatedStudentBirthdate
                to_edit.studentGrade = updatedStudentGradeObject
                to_edit.save()
                messages.success(request, 'The Student was successfully Updated!', extra_tags='add')

            else:
                messages.error(request, 'The Student is not exists!', extra_tags='add')

        return redirect('studentForm')


class teacherForm(View):
    template_name = 'teacherForm.html'
    subs = Subject.objects.all()
    teacherSearch = "Enter Teacher Name"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'subs': self.subs, 'teacherSearch': self.teacherSearch})

    def post(self, request, *args, **kwargs):
        if request.POST.get('search'):
            teacherName = request.POST.get('UpdateTeacherName')
            self.teacherSearch = Teacher.objects.get(teacherName=teacherName)
            return render(request, self.template_name, {'subs': self.subs, 'teacherSearch': self.teacherSearch})
        if request.POST.get('AddTeacher'):
            if Teacher.objects.filter(teacherName=request.POST.get('TeacherName')).exists():
                messages.error(request, 'The Teacher already exists!', extra_tags='add')
            else:
                teacherInfo = Teacher.objects.create(teacherName=request.POST.get('TeacherName'))
                subject = request.POST.get('TeacherSubjects')
                subjectObject = Subject.objects.get(subjectName=subject)
                teacherInfo.teacherSubjects.add(subjectObject)
                messages.success(request, 'The Teacher was successfully added!', extra_tags='add')
        elif request.POST.get('UpdateTeacher'):
            if Teacher.objects.filter(teacherName=request.POST.get('UpdateTeacherName')).exists():
                teacherName = request.POST.get('UpdateTeacherName')
                to_edit = Teacher.objects.get(teacherName=teacherName)
                updatedTeacherName = request.POST.get('NewTeacherName')
                updatedTeacherSubject = request.POST.get('NewTeacherSubject')
                updatedTeacherSubjectObject = Subject.objects.get(subjectName=updatedTeacherSubject)
                to_edit.teacherName = updatedTeacherName
                to_edit.teacherSubjects.add(updatedTeacherSubjectObject)
                to_edit.save()
                messages.success(request, 'The Teacher was successfully Updated!', extra_tags='add')
            else:
                messages.error(request, 'The Teacher is not exists!', extra_tags='add')

        return redirect('teacherForm')


class subjectForm(View):
    template_name = 'subjectForm.html'
    clsRoom = ClassRoom.objects.all()
    subjectSearch = "Enter Subject Name"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'clsRoom': self.clsRoom, 'subjectSearch': self.subjectSearch})

    def post(self, request, *args, **kwargs):
        if request.POST.get('search'):
            SubjectSearchName = request.POST.get('UpdateSubjectName')
            self.subjectSearch = Subject.objects.get(subjectName=SubjectSearchName)
            return render(request, self.template_name,
                          {'clsRoom': self.clsRoom, 'subjectSearch': self.subjectSearch})
        if request.POST.get('AddSubject'):
            if Subject.objects.filter(subjectName=request.POST.get('SubjectName')).exists():
                messages.error(request, 'The Subject already exists!', extra_tags='add')
            else:
                subjectClassRoom = request.POST.get('SubjectClassRoom')
                subjectClassRoomObject = ClassRoom.objects.get(classRoomName=subjectClassRoom)
                subjectInfo = Subject.objects.create(subjectName=request.POST.get('SubjectName'),
                                                     classRoomName=subjectClassRoomObject)
                messages.success(request, 'The Subject was successfully added!', extra_tags='add')
        elif request.POST.get('UpdateSubject'):
            if Subject.objects.filter(subjectName=request.POST.get('UpdateSubjectName')).exists():
                SubjectName = request.POST.get('UpdateSubjectName')
                to_edit = Subject.objects.get(subjectName=SubjectName)
                updatedSubjectName = request.POST.get('NewSubjectName')
                updatedSubjectClass = request.POST.get('NewSubjectClassRoom')
                updatedSubjectClassObject = ClassRoom.objects.get(classRoomName=updatedSubjectClass)
                to_edit.subjectName = updatedSubjectName
                to_edit.classRoomName = updatedSubjectClassObject
                to_edit.save()
                messages.success(request, 'The Subject was successfully Updated!', extra_tags='add')
            else:
                messages.error(request, 'The Subject is not exists!', extra_tags='add')
        return redirect('subjectForm')


class classRoomForm(View):
    template_name = 'classRoomForm.html'
    ClassRoomSearch = 'Enter Room Name'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'ClassRoomSearch': self.ClassRoomSearch})

    def post(self, request, *args, **kwargs):
        if request.POST.get('search'):
            classRoomName = request.POST.get('UpdateRoomName')
            self.ClassRoomSearch = ClassRoom.objects.get(classRoomName=classRoomName)
            return render(request, self.template_name, {'ClassRoomSearch': self.ClassRoomSearch})
        if request.POST.get('AddClassRoom'):
            if ClassRoom.objects.filter(classRoomName=request.POST.get('RoomName')).exists():
                messages.error(request, 'The ClassRoom already exists!', extra_tags='add')
            else:
                roomName = ClassRoom.objects.create(classRoomName=request.POST.get('RoomName'))
                messages.success(request, 'The ClassRoom was successfully added!', extra_tags='add')
        elif request.POST.get('UpdateClassRoom'):
            if ClassRoom.objects.filter(classRoomName=request.POST.get('UpdateRoomName')).exists():
                className = request.POST.get('UpdateRoomName')
                to_edit = ClassRoom.objects.get(classRoomName=className)
                updatedClass = request.POST.get('NewRoomName')
                to_edit.classRoomName = updatedClass
                to_edit.save()
                messages.success(request, 'The ClassRoom was successfully Updated!', extra_tags='add')
            else:
                messages.error(request, 'The ClassRoom is not exists!', extra_tags='add')
        return redirect('classRoomForm')


class gradeForm(View):
    template_name = 'gradeForm.html'
    gradeSearch = 'Enter Grade Name'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'gradeSearch': self.gradeSearch})

    def post(self, request, *args, **kwargs):
        if request.POST.get('search'):
            gradeSearchName = request.POST.get('UpdateGradeName')
            self.gradeSearch = Grade.objects.get(gradeName=gradeSearchName)
            return render(request, self.template_name, {'gradeSearch': self.gradeSearch})

        if request.POST.get('AddGrade'):
            if Grade.objects.filter(gradeName=request.POST.get('GradeName')).exists():
                messages.error(request, 'The Grade already exists!', extra_tags='add')
            else:
                gradeName = Grade.objects.create(gradeName=request.POST.get('GradeName'))
                messages.success(request, 'The Grade was successfully added!', extra_tags='add')

        elif request.POST.get('UpdateGrade'):
            if Grade.objects.filter(gradeName=request.POST.get('UpdateGradeName')).exists():
                gradeName = request.POST.get('UpdateGradeName')
                to_edit = Grade.objects.get(gradeName=gradeName)
                updatedGrade = request.POST.get('NewGradeName')
                to_edit.gradeName = updatedGrade
                to_edit.save()
                messages.success(request, 'The Grade was successfully Updated !', extra_tags='update')
            else:
                messages.error(request, 'The Grade is not exists!', extra_tags='update')

        return redirect('gradeForm')

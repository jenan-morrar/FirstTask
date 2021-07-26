from django.conf.urls.static import static
from  django.conf import  settings
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact,name='contact'),
    path('news/',views.news,name='news'),
    path('student/',views.student, name='student'),
    path('teacher/',views.teacher, name='teacher'),
    path('subject/',views.subject, name='subject'),
    path('classRoom/',views.classRoom, name='classRoom'),
    path('grade/',views.grade, name='grade'),
    path('studentForm/',views.studentForm, name='studentForm'),
    path('teacherForm/',views.teacherForm, name='teacherForm'),
    path('subjectForm/',views.subjectForm, name='subjectForm'),
    path('classRoomForm/',views.classRoomForm, name='classRoomForm'),
    path('gradeForm/',views.gradeForm, name='gradeForm'),
]
urlpatterns = urlpatterns +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
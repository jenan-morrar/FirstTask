from django.conf.urls.static import static
from  django.conf import  settings
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index.as_view(),name='index'),
    path('about/',views.about.as_view(), name='about'),
    path('contact/',views.contact.as_view(),name='contact'),
    path('news/',views.news.as_view(),name='news'),
    path('student/',views.student.as_view(), name='student'),
    path('teacher/',views.teacher.as_view(), name='teacher'),
    path('subject/',views.subject.as_view(), name='subject'),
    path('classRoom/',views.classRoom.as_view(), name='classRoom'),
    path('grade/',views.grade.as_view(), name='grade'),
    path('studentForm/',views.studentForm.as_view(), name='studentForm'),
    path('teacherForm/',views.teacherForm.as_view(), name='teacherForm'),
    path('subjectForm/',views.subjectForm.as_view(), name='subjectForm'),
    path('classRoomForm/',views.classRoomForm.as_view(), name='classRoomForm'),
    path('gradeForm/',views.gradeForm.as_view(), name='gradeForm'),
]
urlpatterns = urlpatterns +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
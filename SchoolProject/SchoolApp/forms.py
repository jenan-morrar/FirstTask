from django import forms
from .models import Grade, Student, Subject,Teacher,ClassRoom

class gradeForms (forms.ModelForm):
    class Meta:
        model = Grade
        fields = "__all__"
class classRoomForms (forms.ModelForm):
    class Meta:
        model = Grade
        fields = "__all__"

class studentForms (forms.ModelForm):
    class Meta:
        model = Grade
        fields = "__all__"

class teacherForms (forms.ModelForm):
    class Meta:
        model = Grade
        fields = "__all__"

class subjectForms (forms.ModelForm):
    class Meta:
        model = Grade
        fields = "__all__"

from dataclasses import field, fields
from django import forms

from tutorial.models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"

class UpdateForm(forms.Form):
    student_name = forms.CharField(max_length=100)
    address = forms.CharField()


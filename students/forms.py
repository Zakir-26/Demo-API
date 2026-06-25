from django import forms
from .models import Student

class StudentCreationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"






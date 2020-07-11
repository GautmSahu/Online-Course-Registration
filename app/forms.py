from django import forms
from app.models import Course_Model,Student_Model
import re

class Schedule_New_Course_Form(forms.ModelForm):
    fees=forms.FloatField(min_value=1000)

    class Meta:
        model=Course_Model
        fields="__all__"

    def clean_faculty_name(self):
        name=self.cleaned_data['faculty_name']
        result=re.findall("^[a-zA-Z_ ]*$",name)
        if result:
            return result[0]
        else:
            raise forms.ValidationError("Invalid Faculty Name")

class Student_Registration_Form(forms.ModelForm):
    class Meta:
        model=Student_Model
        fields="__all__"





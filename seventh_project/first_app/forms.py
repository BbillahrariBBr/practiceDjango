from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class  Meta:
        model = StudentModel
        # fields = '__all__'
        exclude = ['roll']
        labels = {
            'name': 'Student Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'btn btn-primary'})
        }
        
        help_texts = {
            'name': 'write your full name'
        }
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
from django import forms
from .models import Trainee
from course_app.models import Course  

class TraineeForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )



class Traineeformmodel(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=False , widget=forms.Select(attrs={'class': 'form-control'}) ) 

    class Meta:
        model = Trainee
        fields = ['name', 'email', 'phone', 'course']  

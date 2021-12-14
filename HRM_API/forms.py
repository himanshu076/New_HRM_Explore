from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import Employee, Department, Attendance, Leave
from django.db.models import Q
from django.utils import timezone

class RegistrationForm (UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email is required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    thumb = forms.FileField(label='Attach a Passport Photograph',required=False,widget=forms.FileInput(attrs={'class':'form-control mt-2', 'type':'file', 'class':'form-control', 'id':'inputGroupFile02'}))
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'thumb')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':True, 'placeholder':'Username Here', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'}))

class EmployeeForm (forms.ModelForm):
    thumb = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    mobile = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email'}))
    emergency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    gender = forms.ChoiceField(choices=Employee.GENDER,widget=forms.Select(attrs={'class':'form-control'}))
    department = forms.ModelChoiceField(Department.objects.all(),required=True, empty_label='Select a department',widget=forms.Select(attrs={'class':'form-control'}))
    language = forms.ChoiceField(choices=Employee.LANGUAGE,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'position', 'mobile','email', 'current_address', 
        'permanent_address', 'emergency', 'gender', 'department', 'joined', 'language', 
        'document_status', 'bank', 'salary', 'thumb')
        widgets={
            'salary':forms.TextInput(attrs={'class':'form-control'}),
            'bank':forms.TextInput(attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'current_address':forms.TextInput(attrs={'class':'form-control'}),
            'permanent_address':forms.TextInput(attrs={'class':'form-control'}),
            'joined':forms.TextInput(attrs={'class':'form-control'}),
            'document_status':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class DepartmentForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department Name'}))
    history = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Brief Department History'}))
    
    class Meta:
        model = Department
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Attendance.STATUS,widget=forms.Select(attrs={'class':'form-control w-50'}))
    staff = forms.ModelChoiceField(Employee.objects.filter(Q(attendance__status=None) | ~Q(attendance__date = timezone.localdate())), widget=forms.Select(attrs={'class':'form-control w-50'}))
    class Meta:
        model = Attendance
        fields = ['status','staff']

class LeaveForm (forms.ModelForm):

    class Meta:
        model = Leave
        fields = '__all__'

        widgets={
            'start': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'end': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'employee':forms.Select(attrs={'class':'form-control'}),
        }
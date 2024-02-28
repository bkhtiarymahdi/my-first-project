from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class ProFileFields(forms.ModelForm):
    def __init__(self, *args, **kwrargs):
        super(ProFileFields, self).__init__(*args, **kwrargs)
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True
        self.fields['is_staff'].disabled = True

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','is_staff']

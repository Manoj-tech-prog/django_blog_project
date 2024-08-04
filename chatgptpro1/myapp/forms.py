# myapp/forms.py
from django import forms
from .models import Comment


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label='Enter A Username' ,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Enter A Password' ,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100,
                                label='Register Name',
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email = forms.EmailField(label='Enter valid Email',
                             widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    password1 = forms.CharField(label='Password1',
                                widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password 1'}))
    password2 = forms.CharField(label='Password2',
                                widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password2'}))
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment_body']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}),
            'comment_body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Your comment!!'})
        }
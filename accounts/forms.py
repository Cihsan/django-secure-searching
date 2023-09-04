from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'form-control'}),
    #         'first_name': forms.TextInput(attrs={'class': 'form-control'}),
    #         'last_name': forms.TextInput(attrs={'class': 'form-control'}),
    #         'email': forms.EmailInput(attrs={'class': 'form-control'}),
    #         'password': forms.PasswordInput(attrs={'class': 'form-control'}),
    #         'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
    #     }
    # def clean(self):
    #     cleaned_data = super(RegisterForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "password and confirm_password does not match"
    #         )

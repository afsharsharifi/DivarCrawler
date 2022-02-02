from attr import field, fields
from django import forms
from django.contrib.auth.models import User
from django.core import validators
from .models import ImageVerifaction
# Form Sign Up


class SignUpForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام کاربری', 'class': 'input100', 'id': 'signupUsernameInput'}),
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='تعداد کاراکترهای نام کاربری نباید بیشتر از 20 کاراکتر باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'ایمیل', 'class': 'input100'}),
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'گذرواژه', 'class': 'input100'}),
        label='گذروازه'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'تکرار گذرواژه', 'class': 'input100'}),
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        is_exist_email = User.objects.filter(email=email).exists()

        if is_exist_email:
            raise forms.ValidationError('کاربری با این ایمیل وجود دارد')
        return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        is_exist_user_by_username = User.objects.filter(
            username=username).exists()

        if is_exist_user_by_username:
            raise forms.ValidationError('کاربری با این نام کاربری وجود دارد')
        return username

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')
        return password


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام کاربری', 'class': 'input100'}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'گذرواژه', 'class': 'input100'}),
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        is_exists_user = User.objects.filter(username=username).exists()
        if not is_exists_user:
            raise forms.ValidationError('کاربری با این نام کاربری یافت نشد')
        return username


class NumberForm(forms.Form):
    number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'یک عدد وارد کنید', 'class': 'input100'}
        )
    )


class ImageForm(forms.Form):
    image = forms.FileField()

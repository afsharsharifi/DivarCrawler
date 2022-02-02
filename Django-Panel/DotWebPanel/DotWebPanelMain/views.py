from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm, NumberForm, ImageForm
from .models import UserNumber, ImageVerifaction
from .utilities import convert

# Create your views here.


def handle_uploaded_file(f):
    with open('images/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def index_page(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    number_form = NumberForm(request.POST or None)
    if number_form.is_valid():
        number = number_form.cleaned_data.get('number')
        number = f"{convert(number)}"

        UserNumber.objects.create(user=user, number=number)

    context = {
        'number_form': number_form
    }
    return render(request, 'Dashboard/panel.html', context)


def image_page(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    all_images = ImageVerifaction.objects.filter(user=user)

    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = request.FILES['image']
            image_path = f'/images/{image.name}'
            ImageVerifaction.objects.create(user=user, image=image_path)
            handle_uploaded_file(request.FILES['image'])
            return render(request, 'Dashboard/image-upload.html', {})
    else:
        image_form = ImageForm()

    context = {
        'image_form': image_form,
        'all_images': all_images,
    }
    return render(request, 'Dashboard/image-upload.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('username', 'کاربری با این مشخصات یافت نشد!')
    context = {
        'login_form': login_form,
    }
    return render(request, 'Accounting/login.html', context)


def user_signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    signup_form = SignUpForm(request.POST or None)
    if signup_form.is_valid():
        username = signup_form.cleaned_data.get('username')
        email = signup_form.cleaned_data.get('email')
        password = signup_form.cleaned_data.get('password')

        User.objects.create_user(
            username=username, email=email, password=password)
        return redirect('/login')
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'Accounting/register.html', context)

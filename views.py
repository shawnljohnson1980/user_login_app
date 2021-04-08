from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    return render(request, 'login.html')


def user_create(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
            return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
    User.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=pw_hash,
    )
    messages.info(request, "Account created Succesfully")
    return redirect(('/'))


def login(request):
    try:
        user = User.objects.get(email=request.POST['email'])
    except:
        messages.error(request, "Email not found.")
        return redirect('/')

    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, 'Incorrect Password used, Please try again')
        return redirect('/')
        
    request.session['first_name'] = user.first_name
    request.session['email'] = user.email
    messages.info(request, "login successful")
    return redirect('/')


def log_out(request):
    if 'email' in request.session:
        del request.session['email']
    elif 'first_name' in request.session:
        del request.session['first_name']
    return redirect('/')

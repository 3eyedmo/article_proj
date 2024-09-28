from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('articles:read_articles')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can log in now.')
            return redirect('accounts:login')  # Redirect to login page
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


# Calculator:

# Snake:
# What is Json Data
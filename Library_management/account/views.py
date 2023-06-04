from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import User
from account.forms import UserLoginForm, UserRegistrationForm


# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = User(cd[''])
#             user.save()
#             messages.success(
#                 request, 'user registered successfully', 'success')
#             return redirect('book:home')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = get_object_or_404(User, email=cd['email'])
            if user is not None:
                user.is_authenticated = True
                user.save()
                messages.success(request, 'logged in successfully', 'success')
                return redirect('book:home')
            else:
                messages.error(
                    request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    user = get_object_or_404(User, is_authenticated=True)
    user.is_authenticated = False
    user.save()
    messages.success(request, 'logged out successfully', 'success')
    return redirect('book:home')


# Create your views here.
def profile(request,id):
    return render(request, 'profile.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import MemberRegisterForm, LoginForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if password2 != password:
                messages.error(request, 'Password Mismatch')

            else: 
                login(request, user)
                
                # redirect users based on role            
                if user.is_staff:
                    messages.success(request, 'Login successful!')
                    return redirect('dashboard')
                 
                else:
                    messages.success(request, 'Login successful!')
                    return redirect('profile')
        
        else:
            messages.error(request, 'User Does Not Exist!')
            return redirect('login')

    else:
        form = LoginForm()
    context = {
        'form': form
    }
        
    return render(request, 'login.html', context)


def signout(request):
    logout(request)
    return redirect('index')


@login_required()
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Successfully updated profile!')
                return redirect('posts')
            except Exception as e:
                messages.error(request, 'There was an error updating your profile. Please try again later.')
        else:
            messages.error(request, 'There were issues with the form submission. Please correct the errors and try again.')
    
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'form': form,
    }

    return render(request, 'profile.html', context)
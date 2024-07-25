from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import MemberRegisterForm, LoginForm
from django.contrib import messages

# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if form.password2 != form.password:
                messages.error(request, 'Password Mismatch')

            else: 
                login(request, user)
                
                # redirect users based on role            
                if user.is_staff:
                    messages.success(request, 'Login successful!')
                    return redirect('dashboard')
                
                else:
                    messages.success(request, 'Login successful!')
                    return redirect('index')
        
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
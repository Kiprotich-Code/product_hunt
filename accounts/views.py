from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import MemberRegisterForm, LoginForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect

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
                return redirect('login')
            else: 

                login(request, user)                
                # redirect users based on role
                if user.user_type.lower() == 'admin':
                    messages.success(request, 'Login successful!')
                    return redirect('dashboard')
                elif user.user_type.lower() == 'member':
                    messages.success(request, 'Member login successful!')
                    return redirect('members_dashboard')
                else:
                    messages.error(request, 'Error! System can\'t determine your user type!')
                    return redirect('login')
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

def register_user(request):
    if request.method == 'POST':
        form = MemberRegisterForm(request.POST)
        
        if form.is_valid():
            # Access cleaned_data after form validation
            password1 = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')

            # Check for password mismatch
            if password1 is not password2:
                messages.error(request, 'Password Mismatch!')
                return redirect('signup')
            
            else:
                # Save the user and redirect to login
                form.save()
                messages.success(request, 'You\'ve successfully created an account!')
                return redirect('login')
            
        else:
            # Debugging form errors
            error_messages = form.errors.as_json()  # Get form errors as JSON
            print(error_messages)  # Print errors to console for debugging

            # Optionally show form errors to the user (in a real app, you might show a friendlier message)
            messages.error(request, f'Invalid form submission: {form.errors}')
            return redirect('signup')

    else:
        form = MemberRegisterForm()

    context = {'form': form}
    return render(request, "register.html", context)

from django.shortcuts import render
from accounts.models import CustomUser
from django.views.generic import ListView
from .forms import AddUserForm

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


# CRUD USERS 
# ADD USERS 
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect

# USER LIST 
class UsersListView(ListView):
    context_object_name = 'users'
    model = CustomUser
    template_name = 'users/users.html'
    paginate_by = 5 
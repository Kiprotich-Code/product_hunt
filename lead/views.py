from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from .forms import AddUserForm, UpdateUserForm, AddCategoryForm
from .models import Category, Product

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
            return redirect('dashboard')
        
    else:
        form = AddUserForm()

    context = {
        'form': form
    }

    return render(request, 'users/add_user.html', context)

# USER UPDATE 
def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UpdateUserForm(instance=user)
    return render(request, 'users/user_update.html', {'form': form})


# USER DELETE 
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    return render(request, 'users/user_confirm_delete.html', {'user': user})

# USER LIST 
class UsersListView(ListView):
    context_object_name = 'users'
    model = CustomUser
    template_name = 'users/users.html'
    paginate_by = 5 


# CRUD - CATEGORIES 
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/add_category.html'
    form_class = AddCategoryForm
    success_url = '/lead/categories/'

class CategoryListView(ListView):
    context_object_name = 'categories'
    model = Category
    template_name = 'categories/categories.html'
    paginate_by = 5


class CategoryDetailView(DetailView):
    context_object_name = 'category'
    model = Category
    template_name = 'categories/category_details.html'

class CategoryUpdateView(UpdateView):
    template_name = 'categories/category_update.html'
    model = Category
    fields = ('name', 'desc', )
    success_url = '/lead/categories/'


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/lead/categories/'
    template_name = 'categories/confirm_delete_category.html'
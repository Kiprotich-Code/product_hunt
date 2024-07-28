from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from .forms import AddUserForm, UpdateUserForm, AddCategoryForm, AddProductForm
from .models import Category, Product
from django.contrib.auth.decorators import login_required
from accounts.forms import ProfileUpdateForm
from django.contrib import messages

# Create your views here.
@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')


# CRUD USERS 
# ADD USERS 
@login_required()
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.user_type.lower() == 'admin':
                user.is_staff = True

            user.save()
            return redirect('dashboard')
        
    else:
        form = AddUserForm()

    context = {
        'form': form
    }

    return render(request, 'users/add_user.html', context)

# USER UPDATE 
@login_required()
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
@login_required()
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



# CRUD ON PRODUCTS 
class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/add_product.html'
    form_class = AddProductForm
    success_url = '/lead/products/'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the currently logged-in user
        return super().form_valid(form)

class ProductListView(ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'products/products.html'
    paginate_by = 5

class ProductUpdateView(UpdateView):
    template_name = 'products/product_update.html'
    model = Product
    fields = ('title', 'sub_title', 'desc', 'category', 'author', )
    success_url = '/lead/products/'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/lead/products/'
    template_name = 'products/confirm_delete_product.html'


# MY PROFILE 
@login_required()
def ld_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Successfully updated profile!')
                return redirect('ld_profile')
            except Exception as e:
                messages.error(request, 'There was an error updating your profile. Please try again later.')
                return redirect('ld_profile')
        else:
            messages.error(request, 'There were issues with the form submission. Please correct the errors and try again.')
            return redirect('ld_profile')
            
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'form': form,
    }

    return render(request, 'ld_profile.html', context)

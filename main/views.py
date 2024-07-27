from django.shortcuts import render, redirect, get_object_or_404
from lead.models import Product, Vote
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from accounts.models import Profile, CustomUser
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import AddProductForm
from accounts.forms import ProfileUpdateForm
from django.contrib import messages

# Create your views here.
def index(request):
    members = CustomUser.objects.all()

    context = {
        'members': members
    }
    return render(request, 'index.html', context)

def products(request):
    prods = Product.objects.annotate(
        upvotes=Count('vote', filter=Q(vote__vote_type='upvote')),
        downvotes=Count('vote', filter=Q(vote__vote_type='downvote'))
    )

    context = {
        'prods': prods
    }
    return render(request, 'products.html', context)

@login_required
def vote(request, product_id, vote_type):
    product = get_object_or_404(Product, pk=product_id)
    vote, created = Vote.objects.get_or_create(user=request.user, product=product)

    if not created and vote.vote_type == vote_type:
        # If user is revoting the same vote type, remove the vote
        vote.delete()
    else:
        # Else, update the vote
        vote.vote_type = vote_type
        vote.save()

    return redirect('products')


# MEMBERS VIEWS 
def members_dashboard(request):
    return render(request, 'members_dashboard.html')


# MEMBERS PERFORM CRUD ON PRODUCTS 
# CRUD ON PRODUCTS 
class MembersProductCreateView(CreateView):
    model = Product
    template_name = 'products/mb_add_product.html'
    form_class = AddProductForm
    success_url = '/mb_products/'

class MembersProductListView(ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'products/mb_products.html'
    paginate_by = 5

class MembersProductUpdateView(UpdateView):
    template_name = 'products/mb_product_update.html'
    model = Product
    fields = ('title', 'sub_title', 'desc', 'category', 'author', )
    success_url = '/mb_products/'


class MembersProductDeleteView(DeleteView):
    model = Product
    success_url = '/mb_products/'
    template_name = 'products/mb_confirm_delete_product.html'


# MY PRODUCTS 
def my_products(request):
    products = Product.objects.filter(author=request.user)

    context = {
        'products': products
    }
    return render(request, 'products/my_products.html', context)


# Members VIEW OTHER MEMBER PROFILES 
class ProfilesListView(ListView):
    context_object_name = 'members'
    model = CustomUser
    template_name = 'members/profiles.html'
    paginate_by = 5


# MEMBER UPDATES PROFILE 
@login_required()
def update_profile(request):
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

    return render(request, 'members/update_profile.html', context)
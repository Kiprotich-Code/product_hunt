from django.shortcuts import render, redirect, get_object_or_404
from lead.models import Product, Vote
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from accounts.models import Profile, CustomUser
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .forms import AddProductForm, ContactForm
from accounts.forms import ProfileUpdateForm
from django.contrib import messages

# Create your views here.
def index(request):
    members = CustomUser.objects.filter(profile__club_role__isnull=False).exclude(profile__club_role='')

    # contact us logic 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = ContactForm()

    context = {
        'members': members,
        'form': form
    }
    return render(request, 'index.html', context)

def products(request):
    prods = Product.objects.annotate(
        upvotes=Count('vote', filter=Q(vote__vote_type='upvote')),
        downvotes=Count('vote', filter=Q(vote__vote_type='downvote'))
    )
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = ContactForm()

    context = {
        'prods': prods,
        'form': form
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

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the currently logged-in user
        return super().form_valid(form)

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

    def get_queryset(self):
        # Filter out members with non-empty club_role
        return CustomUser.objects.filter(profile__club_role__isnull=False).exclude(profile__club_role='')


# MY PROFILE 
def my_profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'members/my_profile.html', context)


# MEMBER UPDATES PROFILE 
@login_required()
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Successfully updated profile!')
                return redirect('my_profile')
            except Exception as e:
                messages.error(request, 'There was an error updating your profile. Please try again later.')
                return redirect('my_profile')

        else:
            messages.error(request, 'There were issues with the form submission. Please correct the errors and try again.')
            return redirect('my_profile')

    
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'form': form,
    }

    return render(request, 'members/update_profile.html', context)


# MEMBER PROFILES 
class MemberDetailView(DetailView):
    context_object_name = 'member'
    model = CustomUser
    template_name = 'members/profile_details.html'

# INDEX PROFILE DETAILS 
class IndexProfileDetailView(DetailView):
    context_object_name = 'member'
    model = CustomUser
    template_name = 'index_profile_details.html'

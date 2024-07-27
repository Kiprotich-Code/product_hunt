from django.shortcuts import render, redirect, get_object_or_404
from lead.models import Product, Vote
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from accounts.models import CustomUser

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


def user_home(request):
    prods = Product.objects.annotate(
        upvotes=Count('vote', filter=Q(vote__vote_type='upvote')),
        downvotes=Count('vote', filter=Q(vote__vote_type='downvote'))
    )

    context = {
        'prods': prods
    }
    return render(request, 'members/user_home.html', context)

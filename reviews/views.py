from django.shortcuts import redirect, render
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        reviews_form = ReviewForm(request.POST)
        if reviews_form.is_valid():
            reviews = reviews_form.save(commit=False)
            reviews.user = request.user
            reviews.save()
            return redirect('reviews:index')
    else:
        reviews_form = ReviewForm()
    context = {
        'reviews_form' : reviews_form
    }
    return render(request, 'reviews/form.html', context=context)

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/index.html', context)

def detail(request, pk):
    reviews = Review.objects.get(pk=pk)
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/detail.html', context)

@login_required
def update(request, pk):
    reviews = Review.objects.get(pk=pk)
    if request.method == 'POST':
        reviews_form = ReviewForm(request.POST, instance=reviews)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect('reviews:detail', reviews.pk)
    else:
        reviews_form = ReviewForm(instance=reviews)
    context = {
        'reviews_form' : reviews_form
    }
    return render(request, 'reveiws/form.html', context)

def delete(request, reviews_pk):
    Review.objects.get(pk=reviews_pk).delete()
    return redirect('reviews:index')

def comment_create(request, pk):
    reviews = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form(commit=False)
        comment.reviews = reviews
        comment.user = request.user
        comment.save()
    return redirect('reviews:detail', reviews.pk)

def comment_delete(request, reviews_pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('reviews:detail', reviews_pk)
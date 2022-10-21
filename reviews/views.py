from django.shortcuts import redirect, render
from .forms import ReviewForm
from .models import Review

# Create your views here.
def create(request):
    if request.method == 'POST':
        reviews_form = ReviewForm(request.POST)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect('reciews:index')
    else:
        reviews_form = ReviewForm()
    context = {
        'reviews_form' : reviews_form
    }
    return render(request, 'reviews/form.html', context)

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
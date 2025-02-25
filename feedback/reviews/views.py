from django.shortcuts import render

from .forms import ReviewForm

# Create your views here.


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ReviewForm()
    
    context = {
        "form": form
    }
    return render(request, 'reviews/review.html', context)

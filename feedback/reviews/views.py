from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
# from .models import Review

# Create your views here.


def review(request):
    if request.method == 'POST':
        # Update instead of adding:
        # existing_data = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=existing_data)
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            # review = Review(
            #     user_name=form.cleaned_data['user_name'],
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating']
            #     )
            # review.save()
            form.save()
            
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    
    context = {
        "form": form
    }
    return render(request, 'reviews/review.html', context)


def thank_you(request):
    return render(request, 'reviews/thank-you.html')

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        
        return render(request, 'reviews/review.html', {
        "form": form
        })
    
    def post(self, request):
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, 'reviews/review.html', {
        "form": form
        })


# class ThanksView(View):
#     def get(self, request):
#         return render(request, 'reviews/thank-you.html')


class ThanksView(TemplateView):
    template_name = "reviews/thank-you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context


class ReviewsListView(TemplateView):
    template_name = "reviews/review-list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context


class ReviewDetailView(TemplateView):
    template_name = "reviews/review-detail.html"
    
    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.get(id=pk)
        context["review"] = review 
        return context


# def review(request):
#     if request.method == 'POST':
#         # Update instead of adding:
#         # existing_data = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST, instance=existing_data)
        
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating']
#             #     )
#             # review.save()
#             form.save()
            
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
    
#     context = {
#         "form": form
#     }
#     return render(request, 'reviews/review.html', context)


# def thank_you(request):
#     return render(request, 'reviews/thank-you.html')

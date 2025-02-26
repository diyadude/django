# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import FormView
# from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import ReviewForm
from .models import Review

# Create your views here.


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
        
#         return render(request, 'reviews/review.html', {
#         "form": form
#         })
    
#     def post(self, request):
#         form = ReviewForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
        
#         return render(request, 'reviews/review.html', {
#         "form": form
#         })


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class ThanksView(View):
#     def get(self, request):
#         return render(request, 'reviews/thank-you.html')


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


# class ThanksView(View):
#     def get(self, request):
#         return render(request, 'reviews/thank-you.html')


class ThanksView(TemplateView):
    template_name = "reviews/thank-you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review-list.html"
    model = Review
    context_object_name = "reviews"  # default: object_list
    
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=0)
        return data


class ReviewDetailView(DetailView):
    template_name = "reviews/review-detail.html"
    model = Review  # name in template: review, object
    # the key in url should be defined <int:pk> or slug
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context["is_favorite"] = favorite_id == str(loaded_review.id)

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


class AddFavorateView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        
        return HttpResponseRedirect(reverse('review-detail', args=[review_id]))

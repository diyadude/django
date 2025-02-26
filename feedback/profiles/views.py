from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        context = {
            "form": form
        }
        return render(request, "profiles/create-profile.html", context)

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()

            return HttpResponseRedirect('/profiles')            
        context = {
            "form": submitted_form
        }
        return render(request, "profiles/create-profile.html", context)

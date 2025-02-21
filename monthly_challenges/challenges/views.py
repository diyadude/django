from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month.",
    "february": "Walk for at least 20 minutes every day.",
    "march": "Learn Django for at least 20 minutes every day.",
    "april": "Read 10 pages of a book before bed.",
    "may": "Drink a full glass of water first thing in the morning.",
    "june": "Write down one thing you're grateful for each day.",
    "july": "Learn a new word and use it in conversation.",
    "august": "Spend 15 minutes decluttering a space in your home.",
    "september": "Reach out to a friend or family member just to say hi.",
    "october": None,
    "november": "Practice mindfulness or meditate for 10 minutes.",
    "december": "Try not to love her (impossible)."
}


def index(request):
    months = monthly_challenges.keys()

    context = {
        "months": months
    }
    return render(request, "challenges/index.html", context)


def monthly_challenge_numric(request, month: int):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid input!")

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])  # e.g. /challenges/january

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month: str):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/index.html", challenge_text)
        # return HttpResponse(response_data)
        context = {
            "text": challenge_text,
            # "month_name": month.capitalize()  # {{ month_name|title }}
            "month_name": month
        }
        return render (request, "challenges/challenge.html", context)
    except Exception:
        return HttpResponseNotFound("Invalid input!")

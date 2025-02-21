from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "october": "Try a new healthy recipe for dinner.",
    "november": "Practice mindfulness or meditate for 10 minutes.",
    "december": "Try not to love her (impossible)."
}


def index(request):
    list_items = ""
    for month in monthly_challenges.keys():
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f"<li> <a href='{month_path}'>{capitalized_month}</a> </li>"
    result = "<h2> Choose a challenge</h2>" + f"<ul>{list_items}</ul>"

    return HttpResponse(result)


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

        return HttpResponse(challenge_text)
    except Exception:
        return HttpResponseNotFound("Invalid input!")

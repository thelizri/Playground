from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

months = {
    "january": "It's cold outside. Wear a jacket.",
    "february": "Go to the gym. Work off that holiday weight.",
    "march": "Almost spring. Start preparing your beach body.",
    "april": "April showers bring May flowers. Don't forget your umbrella.",
    "may": "Spring is in full bloom. Enjoy the fresh air and nature.",
    "june": "Summer's here. Time for beach trips and BBQs.",
    "july": "Watch the fireworks. Happy Independence Day!",
    "august": "The hottest month. Stay hydrated and wear sunscreen.",
    "september": "Fall is approaching. Get your sweaters out.",
    "october": "Pumpkin spice everything. Prepare for Halloween.",
    "november": "Leaves are falling. Time to give thanks.",
    "december": "Holiday season. Spend time with loved ones and spread cheer.",
}


# Create your views here.
def index(request):
    list_items = ""
    keys = list(months.keys())
    for month in keys:
        redirect_path = reverse("monthly_challenge", args=[month])
        list_items += f"<li><a href='{redirect_path}'>{month.capitalize()}</a></li>"
    return HttpResponse(f"<h2><ul>{list_items}</ul></h2>")


def monthly_challenge(request, month):
    try:
        text = months[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Could not find that month.")


def monthly_challenge_redirect(request, month):
    try:
        keys_of_months = list(months.keys())
        redirect_month = keys_of_months[month - 1]
        redirect_path = reverse("monthly_challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Number needs to be between 1-12")

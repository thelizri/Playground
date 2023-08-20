from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    Http404,
)
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None,
}


# Create your views here.
def index(request):
    month_names = list(months.keys())
    return render(request, "challenges/index.html", {"months": month_names})


def monthly_challenge(request, month):
    try:
        challenge_text = months[month]
        return render(
            request,
            "challenges/challenge.html",
            {"month": month, "text": challenge_text},
        )
    except:
        raise Http404()


def monthly_challenge_redirect(request, month):
    try:
        keys_of_months = list(months.keys())
        redirect_month = keys_of_months[month - 1]
        redirect_path = reverse("monthly_challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()

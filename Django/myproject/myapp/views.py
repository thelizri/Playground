from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


# Create your views here.
def index(request):
    return render(
        request,
        "myapp/index.html",
        {
            "title": "Months",
            "months": months,
        },
    )


def month_by_number(request, month):
    month = months[(month - 1) % 12]
    redirect_path = reverse("month", args=[month])
    return HttpResponseRedirect(redirect_path)


def month(request, month):
    return render(
        request,
        "myapp/month.html",
        {
            "month": month,
        },
    )

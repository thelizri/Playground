from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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
    return HttpResponse("Hello World")


def month_by_number(request, month):
    month = months[(month - 1) % 12]
    return HttpResponseRedirect(month)


def month(request, month):
    return HttpResponse(month)

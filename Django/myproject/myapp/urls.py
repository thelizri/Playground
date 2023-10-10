from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.month_by_number, name="month_by_number"),
    path("<str:month>", views.month, name="month"),
]

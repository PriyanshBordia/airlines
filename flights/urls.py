from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("flight/<int:flight_id>", views.flight, name="flight"),
    path("flights", views.flights, name="flights"),
    path("book", views.book, name="book"),
]

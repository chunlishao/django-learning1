from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.indexByNum),
    path("<str:month>", views.index, name="month_challenge"),
    path("", views.GoHome)
]


from django.urls import path
from secapp import views

urlpatterns = [
    path("", views.home, name="hm"),
    path("abt/", views.about, name="ab"),
    path("cnt/", views.contact, name="ct"),
    path("reg/", views.register, name="rg"),
]

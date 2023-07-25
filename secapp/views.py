from django.shortcuts import render, redirect
from .form import UserForm


# Create your views here.
def home(self):
    return render(self, "ht/home.html")


def about(self):
    return render(self, "ht/about.html")


def contact(self):
    return render(self, "ht/contact.html")


def register(request):
    if request.method == "POST":
        r = UserForm(request.POST)
        if r.is_valid():
            r.save()
            return redirect("/")
    r = UserForm()
    return render(request, "ht/register.html", {"d": r})

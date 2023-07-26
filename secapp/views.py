from django.shortcuts import render, redirect
from .form import UserForm
from secproject import settings
from django.core.mail import send_mail
from django.contrib import messages


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


def mailsending(self):
    if self.method == "POST":
        sndr = self.POST["sn"]
        sbj = self.POST["sb"]
        m = self.POST["msg"]
        t = settings.EMAIL_HOST_USER
        # print(sndr, sbj, m, t)
        b = send_mail(sbj, m, t, [sndr])
        if b == 1:
            messages.success(self, "Mail has been sent Successfully")
            return redirect("/mail")

        else:
            messages.error(self, "Mail has not been sent")
            return redirect("/mail")

    return render(self, "ht/mail.html")

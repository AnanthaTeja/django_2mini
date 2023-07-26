from django.urls import path
from secapp import views
from django.contrib.auth import views as g

urlpatterns = [
    path("", views.home, name="hm"),
    path("abt/", views.about, name="ab"),
    path("cnt/", views.contact, name="ct"),
    path("reg/", views.register, name="rg"),
    path("login/", g.LoginView.as_view(template_name="ht/login.html"), name="lg"),
    path("logout/", g.LogoutView.as_view(template_name="ht/logout.html"), name="lgout"),
    path("mail/", views.mailsending, name="ml"),
]

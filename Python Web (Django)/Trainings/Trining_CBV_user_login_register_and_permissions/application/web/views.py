from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "templates/index.html"


class LoginView(generic.View):
    pass

class RegisterView():
    pass
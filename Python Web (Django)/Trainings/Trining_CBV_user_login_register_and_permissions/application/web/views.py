from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate
from .models import Ingredient

class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"
    login_url = "/login/"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        color = Ingredient.objects.get(id=1)
        context.update({
            'color': color
        })
        return context
    

class RegisterView(generic.CreateView):
    template_name = "register.html"
    form_class = CreationForm
    template_name_field = 'form'
    success_url = reverse_lazy("home page")
    
    
def login_view(request):
    message = ""
    
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy("home page"))
        else:
            message = "Wrong User or Passowrd"
        
    context = {
        'message': message,
    }
    return render(request, template_name="login.html", context=context)



class testView(generic.ListView):
    template_name = 'test.html'
    model = Ingredient
    
    def get_context_data(self, **kwargs):
        context = super(testView, self).get_context_data(**kwargs)
        
        color = Ingredient.objects.get(id=1)
        context.update({
            'color': color
        })
        return context
from django.shortcuts import render, redirect

from .models import Recepe
from .forms import RecepeForm

def home(request):
    
    recepes  = Recepe.objects.all()
    context = {
        "recepes": recepes
    }

    return render(request, "index.html", context)

def create(request):
    form = RecepeForm()

    context = {
        "form": form
    }

    return render(request, "create.html", context)


def edit_recipe(request, pk):
    recepes  = Recepe.objects.get(pk = pk)
    
    form = RecepeForm(request.POST, instance=recepes)
    
    if form.is_valid():
        form.save()
        return redirect("home page")
    
    else: 
        form = RecepeForm(instance=recepes)

    context = {
        "form": form,
        "recepes": recepes,
    }

    return render(request, "edit.html", context)
    

def delete_recipe(request, pk):
    return render(request, "delete.html")
    

def recipe_details(request, pk):
    return render(request, "details.html")
    

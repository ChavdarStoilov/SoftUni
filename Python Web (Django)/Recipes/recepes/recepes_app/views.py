from django.shortcuts import render, redirect
from .models import Recepe
from .forms import RecepeForm, DeletedRecepeForm

def home(request):
    
    recepes  = Recepe.objects.all()
    context = {
        "recepes": recepes
    }

    return render(request, "index.html", context)

def create(request):

    form = RecepeForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect("home page")
        
    else:
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
    the_recepes = Recepe.objects.get(pk = pk)

    form = DeletedRecepeForm(request.POST, instance=the_recepes)
    
    if form.is_valid():
        form.save()
        return redirect("home page")
    
    else:
        form = DeletedRecepeForm(instance=the_recepes)

    context = {
        "form": form,
        "recepes": the_recepes,
    }
    
    return render(request, "delete.html", context)
    

def recipe_details(request, pk):
    recepes = Recepe.objects.get(pk = pk)
    the_ingredients = recepes.ingredients.split(", ")
    context = {
        "recepes": recepes,
        "ingredoents": the_ingredients,
    }

    return render(request, "details.html", context)
    

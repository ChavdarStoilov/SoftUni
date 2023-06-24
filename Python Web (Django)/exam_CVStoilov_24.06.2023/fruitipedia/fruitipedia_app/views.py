from django.shortcuts import render, redirect
from .models import Profile, Fruit
from .forms import CreateProfiletForm, FruitForm,\
    DeleteFruitForm, EditProfileForm, EditFruitForm


def index(request):
    return render(request, "index.html")

def dashboard(request):
    fruits = Fruit.objects.all()
    
    context = {
        "fruits": fruits
    }
    return render(request, "dashboard.html", context=context)

def create_fruit(request):
    if request.method == 'POST':
        form = FruitForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("dashboard page")
    else:
        form = FruitForm()
        
    context = {
        'form': form,
    }
    return render(request, "create-fruit.html", context=context)

def details_fruit(request, pk):
    
    fruit = Fruit.objects.get(pk=pk)
    
    context = {
        "fruit": fruit
    }
    
    return render(request, "details-fruit.html", context=context)

def edit_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect("dashboard page")
        
        
    else:
        form = EditFruitForm(instance=fruit)
        
    context = {
        "form": form,
        "fruit": fruit
    }
    
    return render(request, "edit-fruit.html", context=context)

def delete_fruit(request, pk):
    
    fruit = Fruit.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = DeleteFruitForm(request.POST, instance=fruit)
        
        if form.is_valid():
            form.save()
            return redirect("dashboard page")
            
    else:
        form = DeleteFruitForm(instance=fruit)
        

    context= {
        "fruit": fruit,
        "form": form,
    }
    return render(request, "delete-fruit.html", context=context)

def create_profile(request):
    
    if request.method == 'POST':
        form = CreateProfiletForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("dashboard page")
    else:
        form = CreateProfiletForm()
        
    context = {
        'form': form,
    }

    return render(request, "create-profile.html", context=context)

def details_profile(request):
    user = Profile.objects.get()
    posts = Fruit.objects.all().count()
    context = {
        "user": user,
        "posts": posts,
    }
    return render(request, "details-profile.html", context=context)

def edit_profile(request):
    user = Profile.objects.first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            return redirect("details profile page")
    else:
        form = EditProfileForm(instance=user)
        
    context = {
        "form": form
    }
    return render(request, "edit-profile.html", context=context)

def delete_profile(request):
    user = Profile.objects.first()
    fruits = Fruit.objects.all()
    
    if request.method == "POST":
        user.delete()
        fruits.delete()
        return redirect("home page")
        
    
    return render(request, "delete-profile.html")


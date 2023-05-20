from django.shortcuts import redirect, render
from .forms import CreateProfileForm, CreateCarForm, CarForm, UserForm, UserDeleteForm
from .models import Car, Profiel



def index(request):
    user =  Profiel.objects.last()
    
    context = {
        'user': user,
    }
    return render(request, 'index.html', context=context)

def catalogue(request):
    user =  Profiel.objects.last()
    cars = Car.objects.all()
    context = {
        'cars': cars,
        'total_cars': len(cars),
        'user': user,
    }
    
    return render(request, 'catalogue.html', context=context)

def create_profile(request):
    
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('catalogue page')
    else:
        form = CreateProfileForm()
        
    context = {
        'form': form,
    }
    return render(request, 'profile-create.html', context = context)

def edit_profile(request):
    user = Profiel.objects.last()
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('detail profile')
    else:
        form = UserForm(instance=user)
        
    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context=context)

def delete_profile(request):
    if request.method == 'POST':
        Profiel.objects.all().delete()
        Car.objects.all().delete()
        return redirect('home page')
        
    return render(request, 'profile-delete.html')

def detail_profile(request):
    user =  Profiel.objects.last()
    total_car_price = [car.price for car in Car.objects.all()]
    context = {
        'user': user,
        'total_car_price': sum(total_car_price),
    }
    return render(request, 'profile-details.html', context=context)

def create_car(request):
    
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('catalogue page')
    else:
        form = CreateCarForm()
        
    context = {
        'form': form
    }
    return render(request, 'car-create.html', context =context)

def detail_car(request, pk):
    car = Car.objects.get(pk=pk)
    
    context = {
        'car': car,
    }
    return render(request, 'car-details.html', context=context)

def edit_car(request, pk):
    car = Car.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = CreateCarForm(request.POST, instance=car)
        
        if form.is_valid():
            form.save()
            return redirect('catalogue page')
    else:
        form=CreateCarForm(instance=car)
    
    context = {
        'form':form,
        'car': car,
    }
    return render(request, 'car-edit.html', context=context)

def delete_car(request, pk):
    
    car = Car.objects.get(pk=pk)
    
    
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')
    
    else:
        form = CarForm(instance=car)
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car-delete.html', context= context)

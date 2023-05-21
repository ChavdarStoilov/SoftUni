from django.shortcuts import render, redirect
from .models import Profile, Game
from .forms import CreateGameForm, CreateProfileForm, GameDeleteForm, ProfleForm

def index(request):
    user = Profile.objects.last()
    
    context = {
        "user": user
    }
    return render(request, 'home-page.html', context=context)

def dashboard(request):
    user = Profile.objects.last()
    games = Game.objects.all()
    
    context = {
        'user': user,
        'games': games
    }
    return render(request, 'dashboard.html', context=context)

def create_profile(request):
    
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home page")
    else:
        form = CreateProfileForm()
        
        
    context = {
        'form': form
    }
    
    return render(request, 'create-profile.html', context= context)

def details_profile(request):
    user = Profile.objects.last()
    total_games = [game for game in Game.objects.all()]
    avg_rating = sum([rating.rating for rating in Game.objects.all()])
    print(total_games)
    print(avg_rating)
    context = {
        "user": user,
        "total_games": len(total_games),
        "avg_rating": avg_rating / len(total_games) if total_games else 0.0
    }
    return render(request, 'details-profile.html', context)

def edit_profile(request):
    user = Profile.objects.last()
    
    if request.method == 'POST':
        form = ProfleForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("details profile page")
    else:
        form= ProfleForm(instance=user)
        
    context= {
        "form": form,
    }
    return render(request, 'edit-profile.html', context=context)

def delete_profile(request):
    user = Profile.objects.last()
    games = Game.objects.all()
    
    if request.method == 'POST':
        user.delete()
        games.delete()
        return redirect("home page")
    return render(request, 'delete-profile.html')

def create_game(request):
    
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("dashboard page")
        
    else:
        form = CreateGameForm()
        
    context = {
        'form': form,
    }
    return render(request, 'create-game.html', context=context)

def details_game(request, pk):
    game = Game.objects.get(pk=pk)
    
    context = {
        "game": game
    }
    return render(request, 'details-game.html', context=context)

def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = CreateGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("dashboard page")
    else:
        form = CreateGameForm(instance=game)
        
    context = {
        "game": game,
        "form": form,
    }
        
    return render(request, 'edit-game.html', context=context)

def delete_game(request, pk):
    
    game = Game.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("dashboard page")
    else:
        form = GameDeleteForm(instance=game)
    
    context = {
        'game': game,
        'form': form,
    }
    return render(request, 'delete-game.html', context=context)

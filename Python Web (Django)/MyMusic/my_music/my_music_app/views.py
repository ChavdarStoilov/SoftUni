from django.shortcuts import render
from .models import Profile, Album

def index(request):
    user = Profile.objects.last()
    albums =Album.objects.all()
    
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        
    else:
        form = CreateProfileForm()
        
    context = {
        'albums': albums,
        'form': form,
    }
    
    if user:
        return render(request, 'home-with-profile.html', context=context)
    else:
        return render(request, 'home-no-profile.html')

def profile_datails(request):
    pass

def profile_delete(request):
    pass

def album_add(request):
    pass

def album_details(request):
    pass

def album_edit(request):
    pass

def album_delete(request):
    pass

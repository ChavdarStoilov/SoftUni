from django.shortcuts import render, redirect
from .models import Profile, Note
from .forms import ProfileForm, CreateNote ,NoteFormn



# Create your views here.
def index(request):
    form = ProfileForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home page')
        
    
    profiles = Profile.objects.all()
    notes = Note.objects.all()

    context = {
        "form": form,
        "notes": notes
    }


    if profiles:
        return render(request, 'home-with-profile.html', context)
    
    return render(request, 'home-no-profile.html', context)

def add_note(request):

    form = CreateNote(request.POST)

    
    if form.is_valid():
        form.save()
        return redirect('home page')
    else:
        form = CreateNote()

    context = {
        "form": form,
    }
    

    return render(request, 'note-create.html', context)

def edit_note(request, pk):
    the_note = Note.objects.get(pk = pk)

    form = NoteFormn(request.POST, instance=the_note)

    if form.is_valid():
        form.save()
        return redirect('home page')
    
    else:
        form = NoteFormn(instance=the_note)

    context = {
        "form": form,
        "the_note": the_note
    }

    return render(request, 'note-edit.html', context)

def delete_note(request, pk):
    return render(request, 'note-delete.html')

def details_note(request, pk):
    the_note = Note.objects.get(pk = pk)

    context = {
        "the_note": the_note
    }


    return render(request, 'note-details.html', context)

def show_prfile(request):
    return render(request, 'profile.html')
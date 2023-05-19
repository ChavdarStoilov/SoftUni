from django.shortcuts import render

def detail_photo(request, username, pet_name):
    return render(request, 'photo-detail-page.html')

def add_photo(request):
    return render(request, 'photo-add-page.html')

def edit_photo(request):
    return render(request, 'photo-edit-page.html')
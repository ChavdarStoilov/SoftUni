from django.shortcuts import render


def details_pet(request):
    return render(request, 'pet-details-page.html')

def add_pet(request):
    return render(request, 'pet-add-page.html')

def edit_pet(request):
    return render(request, 'pet-edit-page.html')

def delete_pet(request):
    return render(request, 'pet-delete-page.html')


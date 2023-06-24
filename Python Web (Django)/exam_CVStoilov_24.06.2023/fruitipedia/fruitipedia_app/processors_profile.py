from .models import Profile

def get_profile(request):
    user = Profile.objects.first()
    context = {
        "user": user
    }
    
    return context

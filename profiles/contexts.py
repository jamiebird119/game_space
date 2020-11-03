from django.shortcuts import get_object_or_404
from .models import UserProfile


def profile_from_user(request):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        context = {
            'user_profile': user_profile
        }
        return context
    else:
        context = {

        }
        return context

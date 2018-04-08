from django.shortcuts import render
from django.http import Http404
from .models import User, Video

def index(request):
    all_users = User.objects.all()
    context = {
        'all_users' : all_users,
    }
    return render(request, 'videos/index.html', context)

def user_videos(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist.")
    return render(request, 'videos/user_videos.html', {'user' : user})

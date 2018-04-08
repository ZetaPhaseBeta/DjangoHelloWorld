from django.shortcuts import render
from django.http import Http404
from .models import User, Video

def index(request):
    all_users = User.objects.all()
    context = {
        'all_users' : all_users,
    }
    return render(request, 'videos/index.html', context)

def user_videos(request):
    pass

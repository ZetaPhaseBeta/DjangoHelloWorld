from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.user_videos, name='user_videos'),
]

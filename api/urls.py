from django.urls import path
from . import views

urlpatterns = [
	path('servers/', views.ServerView.as_view()),
    path('create/', views.CreateView.as_view())
]
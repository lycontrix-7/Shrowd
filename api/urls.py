from django.urls import path
from . import views

urlpatterns = [
	path('s/servers/', views.PublicServerView.as_view()),
    path('s/create/', views.PublicCreateView.as_view()),
    path('s/join/', views.PublicJoinView.as_view()),
    path('p/servers/', views.PrivateServerView.as_view()),
    path('p/create/', views.PrivateCreateView.as_view()),
    path('p/join/', views.PrivateJoinView.as_view()),
]
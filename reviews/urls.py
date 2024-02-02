from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.ReviewPostDisplay, name='ReviewPostDisplay'),
    path('profile/', views.Profile, name='profile' )
]
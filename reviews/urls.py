from django.urls import path
from . import views



app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.ReviewPostDisplay, name='ReviewPostDisplay'),
    path('reviews/<slug:slug>/', views.ReviewDetail, name='reviews-detail'),
    path('create/', views.CreateReview, name='create'),
    path('<slug>/update/', views.UpdateReview, name='update-review'),
    path('<slug>/delete/', views.DeleteReview, name='delete-review')
]
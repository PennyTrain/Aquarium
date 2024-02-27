from django.urls import path
from . import views



app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.review_display, name='review-display'),
    path('reviews/<slug:slug>/', views.review_detail, name='reviews-detail'),
    path('create/', views.review_create, name='create'),
    path('<slug>/update/', views.review_update, name='update-review'),
    path('<slug>/delete/', views.review_delete, name='delete-review')
]
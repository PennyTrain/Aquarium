from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='main'),
    path('gallery/', views.gallery, name='gallery'),
    path('visit/', views.visit, name='visit'),
]

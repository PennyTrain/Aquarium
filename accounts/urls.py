from . import views
from django.urls import path


app_name = 'accounts'


urlpatterns = [
    path('signups/', views.profile_register, name="signup"),
    path('login/', views.profile_login, name="login"),
    path('logout/', views.profile_logout, name="account_logout"),
    path('profile/', views.profile_view, name="user-profile"),
    path('profile/delete-account', views.profile_delete, name="delete"),
]
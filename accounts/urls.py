from . import views
from django.urls import path


app_name = 'accounts'


urlpatterns = [
    path('signups/', views.account_signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="account_logout"),
    path('profile/', views.profile_view, name="user-profile"),
    path('profile/delete-account', views.delete_profile, name="delete"),
]
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (UserRegisterForm,
                    AccountUpdateForm,
                    ProfileFormUpdate,
                    DeleteUserForm
                    )


def profile_register(request):
    """
    This enables people to create an account if they do not already have one
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Account created!')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})


# Creates the login_view


def profile_login(request):
    """
    This enables people to log in to their account
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                messages.add_message(request, messages.SUCCESS,
                                     'You have been logged in!')
                return redirect('main:main')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login-form.html',
                  {'form': form})


# Creates the log out view

@login_required(login_url="/accounts/login/")
def profile_logout(request):
    """
    profile_logout enables the user to logout
    """
    if request.method == 'POST':
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                             'You have been logged out!')
        return redirect('main:main')
    form = AuthenticationForm()
    return render(request, 'accounts/log-out.html', {'form': form})


@login_required(login_url="/accounts/login/")
def profile_view(request):
    """
    This shows the users their own profile
    if they have one and they are logged into it
    """
    profile_form = ProfileFormUpdate(instance=request.user.profile)
    account_form = AccountUpdateForm(instance=request.user)
    if request.method == 'POST':
        account_form = AccountUpdateForm(request.POST,
                                         instance=request.user)
        profile_form = ProfileFormUpdate(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if account_form.is_valid() and profile_form.is_valid():
            try:
                profile_form.save()
                account_form.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Your profile has been updated')
                return redirect('accounts:profile')
            except Exception:
                account_form = AccountUpdateForm(request.POST,
                                                 instance=request.user)
                profile_form = ProfileFormUpdate(request.POST,
                                                 request.FILES,
                                                 instance=request.user.profile)
                context = {
                    'profile_form': profile_form,
                    'account_form': account_form,
                }
                return render(request, 'accounts/user-profile.html', context)
    context = {
        'account_form': account_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/user-profile.html', context)


@login_required(login_url="/accounts/login/")
def profile_delete(request):
    """
    This enables users to delete their profile
    """
    if request.method == 'POST':
        delete_form = DeleteUserForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Your profile has been deleted!')
        return redirect('accounts:signup')
    else:
        delete_form = DeleteUserForm(instance=request.user)
    context = {
        'delete_form': delete_form
    }
    return render(request, 'accounts/delete.html', context)

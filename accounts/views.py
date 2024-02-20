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


def account_signup(request):
    """
    Is what is run when the signup url is called upon
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            mess = f"Account had been created for {username}!"
            messages.success(request, mess)
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})


# Creates the login_view


def login_view(request):
    """
    Is what is run when the login in url is called upon
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                messages.info(request, 'You are successfully logged in!')
                return redirect('main:main')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login-form.html', {'form': form})


# Creates the log out view


def logout_view(request):
    """
    Logsout the user to the site
    """
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Your have been Logged Out.')
        return redirect('main:main')
    form = AuthenticationForm()
    return render(request, 'accounts/log-out.html', {'form': form})


@login_required(login_url="/accounts/login/")
def profile_view(request):
    """
    Shows the Users profile only if logged in
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
                messages.info(request, 'Profile Updated Successfully.')
                return redirect('accounts:profile')
            except:
                messages.warning(request, 'Please Use an Image')
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


def delete_profile(request):
    """
    deletes the profile view
    """
    if request.method == 'POST':
        delete_form = DeleteUserForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.warning(request, 'Your profile has been deleted.')
        return redirect('accounts:signup')
    else:
        delete_form = DeleteUserForm(instance=request.user)
    context = {
        'delete_form': delete_form
    }
    return render(request, 'accounts/delete.html')
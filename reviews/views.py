from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import ReviewPost
from django.views.generic import DeleteView
from .forms import EditPost, CreatePost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from accounts.models import Profile


def review_display(request):
    template_name = "reviews/reviews.html"
    reviews_all = ReviewPost.objects.all()
    context = {
        'reviews_all': reviews_all
    }
    return render(request, template_name, context)


def review_detail(request, slug):
    review = get_object_or_404(ReviewPost, slug=slug)
    template_name = "reviews/reviews_details.html"
    context = {
        'review': review
    }
    return render(request, template_name, context)


@login_required(login_url="/accounts/login/")
def review_create(request):
    """
    A view to create the reviews
    """
    form = CreatePost()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            new_review = form.save(commit=False)
            print(request.user)
            # print(new_review)
            # print(new_review.author)
            new_review.author = request.user
            print(new_review)
            new_review.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your review has been uploaded!')
            return redirect(reverse('reviews:review-display'))
        else:
            messages.add_message(request, messages.WARNING,
                                 'Somethings gone wrong please try again!')
            return
    template_name = "reviews/create_review.html"
    return render(request, template_name, context)


@login_required(login_url="/accounts/login/")
def review_update(request, slug):
    """
    update
    """
    review = get_object_or_404(ReviewPost, slug=slug)
    if not request.user == review.author:
        messages.warning(request, 'Sorry not Owner of the post!')
        return redirect('reviews:review-display')
    review_form = EditPost(instance=review)
    if request.method == 'POST':
        review_form = EditPost(request.POST,
                               request.FILES,
                               instance=review)
        if review_form.is_valid():
            try:
                review_form.save()
                messages.add_message(request, messages.SUCCESS,
                                     'The review has been successfully')
                return redirect('reviews:review-display')
            except Exception:
                messages.add_message(request, messages.WARNING,
                                     'is it all filled out correctly?')
                context = {
                    'form': review_form
                }
                return render(request,
                              'reviews/update_review.html', context)
    context = {
        'form': review_form
    }
    return render(request, 'reviews/update_review.html', context)


@login_required(login_url="/accounts/login/")
def review_delete(request, slug):
    review = get_object_or_404(ReviewPost, slug=slug)
    if not (request.user == review.author or request.user.is_superuser):
        messages.add_message(request, messages.WARNING,
                             'Somethings gone wrong please try again!')
        return redirect('reviews:review-display')
    review.delete()
    messages.add_message(request, messages.SUCCESS, 'Review Deleted!')
    return redirect('reviews:review-display')

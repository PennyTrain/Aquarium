from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import ReviewPost


# View for running reviews
def ReviewPostDisplay(request):
    template_name = "reviews/reviews.html"
    reviews_all = ReviewPost.objects.all()
    context = {
        'reviews_all': reviews_all
    }
    return render(request, template_name, context)


@login_required
def Profile(request):
    """
    View that returns profile page
    """
    template_name = 'reviews/profile.html'
    return render(request, template_name)
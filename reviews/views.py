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

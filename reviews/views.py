from django.http import HttpResponse
from django.shortcuts import render


# View for running reviews
def reviews(request):
    return HttpResponse("This isnt a review")

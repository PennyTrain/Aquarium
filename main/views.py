from django.shortcuts import render

# Create your views here.

def index(request):
    """
    View that returns homepage
    """
    template_name = 'main/index.html'
    return render(request, template_name)


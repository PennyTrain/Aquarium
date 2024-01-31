from django.shortcuts import render

# Create your views here.

def index(request):
    """
    View that returns homepage
    """
    template_name = 'main/index.html'
    return render(request, template_name)


def gallery(request):
    """
    View that returns the gallery page
    """
    template_name = 'main/gallery.html'
    return render(request, template_name)


def visit(request):
    """
    View that returns the visit page
    """
    template_name = 'main/visit.html'
    return render (request, template_name)

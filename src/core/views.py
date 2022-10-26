from django.shortcuts import render

# Create your views here.
from core.models import Image

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    images = Image.objects.all().count()

    context = {
        'num_images': images,
    }

    # Render the HTML template index.htm with the data in the context variable
    return render(request, 'index.htm', context=context)
from django.shortcuts import render

from core.choices import COMMON, PRIME
# Create your views here.
from core.models import Image, Warframe


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    images = Image.objects.all().count()

    context = {
        'num_images': images,
    }

    # Render the HTML template index.htm with the data in the context variable
    return render(request, 'index.htm', context=context)


def about(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    images = Image.objects.all().count()

    context = {
        'num_images': images,
    }

    # Render the HTML template index.htm with the data in the context variable
    return render(request, 'about.htm', context=context)


def news(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    images = Image.objects.all().count()

    context = {
        'num_images': images,
    }

    # Render the HTML template index.htm with the data in the context variable
    return render(request, 'news.htm', context=context)


def warframes(request):
    """View function for home page of site."""

    c_warframes = Warframe.objects.select_related("image").filter(warframe_type=COMMON)
    p_warframes = Warframe.objects.select_related("image").filter(warframe_type=PRIME)

    context = {
        "c_warframes": c_warframes,
        "p_warframes": p_warframes,
    }

    return render(request, "warframes.htm", context=context)


def downloads(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    images = Image.objects.all().count()

    context = {
        'num_images': images,
    }

    # Render the HTML template index.htm with the data in the context variable
    return render(request, 'downloads.htm', context=context)
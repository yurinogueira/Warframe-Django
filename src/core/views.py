from django.shortcuts import render

from core.choices import COMMON, PRIME, HOME_ITEM, HOME_IMAGE, HOME_SUB_IMAGE, ABOUT_ITEM, DOWNLOAD_ITEM
from core.models import Image, ListItem, Report, Warframe


def index(request):
    home_items = ListItem.objects.filter(item_type=HOME_ITEM)
    home_images = ListItem.objects.select_related("image").filter(item_type=HOME_IMAGE)
    home_sub_images = ListItem.objects.select_related("image").filter(item_type=HOME_SUB_IMAGE)

    context = {
        "home_items": home_items,
        "home_images": home_images,
        "home_sub_images": home_sub_images
    }

    return render(request, "index.htm", context=context)


def about(request):
    about_items = ListItem.objects.filter(item_type=ABOUT_ITEM)

    context = {
        "about_items": about_items,
    }

    return render(request, "about.htm", context=context)


def news(request):
    reports = Report.objects.select_related("image").prefetch_related("badges")

    context = {
        "reports": reports,
    }

    return render(request, 'news.htm', context=context)


def warframes(request):
    c_warframes = Warframe.objects.select_related("image").filter(warframe_type=COMMON)
    p_warframes = Warframe.objects.select_related("image").filter(warframe_type=PRIME)

    context = {
        "c_warframes": c_warframes,
        "p_warframes": p_warframes,
    }

    return render(request, "warframes.htm", context=context)


def downloads(request):
    download_items = ListItem.objects.filter(item_type=DOWNLOAD_ITEM)

    context = {
        "download_items": download_items,
    }

    return render(request, "downloads.htm", context=context)

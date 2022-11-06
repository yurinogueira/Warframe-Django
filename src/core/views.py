from django.contrib import messages
from django.shortcuts import render, redirect

from core.choices import COMMON, PRIME, HOME_ITEM, HOME_IMAGE, HOME_SUB_IMAGE, ABOUT_ITEM, DOWNLOAD_ITEM
from core.models import ListItem, Report, Warframe
from user.forms import UserRegisterForm


def register(request):
    form = UserRegisterForm(request.POST)
    context = {
        "register_form": form,
    }

    if form.is_valid():
        user = form.save()
        messages.success(
            request,
            f"Conta criada com sucesso, usuário: {user.email}"
        )
        return redirect("core:index")
    else:
        context["registering"] = True

    return render(request, "index.htm", context=context)


def index(request):
    home_items = ListItem.objects.filter(item_type=HOME_ITEM)
    home_images = ListItem.objects.select_related("image").filter(item_type=HOME_IMAGE)
    home_sub_images = ListItem.objects.select_related("image").filter(item_type=HOME_SUB_IMAGE)

    register_form = UserRegisterForm()

    context = {
        "home_items": home_items,
        "home_images": home_images,
        "home_sub_images": home_sub_images,
        "register_form": register_form,
    }

    return render(request, "index.htm", context=context)


def about(request):
    about_items = ListItem.objects.filter(item_type=ABOUT_ITEM)

    register_form = UserRegisterForm()

    context = {
        "about_items": about_items,
        "register_form": register_form,
    }

    return render(request, "about.htm", context=context)


def news(request):
    reports = Report.objects.select_related("image").prefetch_related("badges")

    register_form = UserRegisterForm()

    context = {
        "reports": reports,
        "register_form": register_form,
    }

    return render(request, 'news.htm', context=context)


def warframes(request):
    c_warframes = Warframe.objects.select_related("image").filter(warframe_type=COMMON)
    p_warframes = Warframe.objects.select_related("image").filter(warframe_type=PRIME)

    register_form = UserRegisterForm()

    context = {
        "c_warframes": c_warframes,
        "p_warframes": p_warframes,
        "register_form": register_form,
    }

    return render(request, "warframes.htm", context=context)


def downloads(request):
    download_items = ListItem.objects.filter(item_type=DOWNLOAD_ITEM)

    register_form = UserRegisterForm()

    context = {
        "download_items": download_items,
        "register_form": register_form,
    }

    return render(request, "downloads.htm", context=context)

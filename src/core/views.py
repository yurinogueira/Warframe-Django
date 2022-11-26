from django.contrib import messages
from django.shortcuts import render

from core.choices import COMMON, PRIME, HOME_ITEM, HOME_IMAGE, HOME_SUB_IMAGE, ABOUT_ITEM, DOWNLOAD_ITEM
from core.models import ListItem, Report, Warframe
from user.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login, logout, authenticate


def login_view(request):
    home_items = ListItem.objects.filter(item_type=HOME_ITEM)
    home_images = ListItem.objects.select_related("image").filter(item_type=HOME_IMAGE)
    home_sub_images = ListItem.objects.select_related("image").filter(item_type=HOME_SUB_IMAGE)

    form = UserLoginForm(request, data=request.POST)
    register_form = UserRegisterForm()

    context = {
        "home_items": home_items,
        "home_images": home_images,
        "home_sub_images": home_sub_images,
        "login_form": form,
        "register_form": register_form,
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request,
                f"Logado com sucesso: {user.email}"
            )
    else:
        context["logining"] = True

    context["user_password"] = "Usuário ou senha inválida"

    return render(request, "index.htm", context=context)


def logout_view(request):
    form = UserLoginForm()
    register_form = UserRegisterForm()

    context = {
        "login_form": form,
        "register_form": register_form,
    }
    logout(request)

    return render(request, "index.htm", context=context)


def register(request):
    home_items = ListItem.objects.filter(item_type=HOME_ITEM)
    home_images = ListItem.objects.select_related("image").filter(item_type=HOME_IMAGE)
    home_sub_images = ListItem.objects.select_related("image").filter(item_type=HOME_SUB_IMAGE)

    login_form = UserLoginForm()
    form = UserRegisterForm(request.POST)

    context = {
        "home_items": home_items,
        "home_images": home_images,
        "home_sub_images": home_sub_images,
        "login_form": login_form,
        "register_form": form,
    }

    if form.is_valid():
        user = form.save()

        login(request, user)

        messages.success(
            request,
            f"Conta criada com sucesso, usuário: {user.email}"
        )
    else:
        context["registering"] = True

    return render(request, "index.htm", context=context)


def index(request):
    home_items = ListItem.objects.filter(item_type=HOME_ITEM)
    home_images = ListItem.objects.select_related("image").filter(item_type=HOME_IMAGE)
    home_sub_images = ListItem.objects.select_related("image").filter(item_type=HOME_SUB_IMAGE)

    login_form = UserLoginForm()
    register_form = UserRegisterForm()

    context = {
        "home_items": home_items,
        "home_images": home_images,
        "home_sub_images": home_sub_images,
        "login_form": login_form,
        "register_form": register_form,
    }

    return render(request, "index.htm", context=context)


def about(request):
    about_items = ListItem.objects.filter(item_type=ABOUT_ITEM)

    login_form = UserLoginForm()
    register_form = UserRegisterForm()

    context = {
        "about_items": about_items,
        "login_form": login_form,
        "register_form": register_form,
    }

    return render(request, "about.htm", context=context)


def news(request):
    reports = Report.objects.select_related("image").prefetch_related("badges")

    login_form = UserLoginForm()
    register_form = UserRegisterForm()

    context = {
        "reports": reports,
        "login_form": login_form,
        "register_form": register_form,
    }

    return render(request, 'news.htm', context=context)


def warframes(request):
    c_warframes = Warframe.objects.select_related("image").filter(warframe_type=COMMON)
    p_warframes = Warframe.objects.select_related("image").filter(warframe_type=PRIME)

    login_form = UserLoginForm()
    register_form = UserRegisterForm()

    context = {
        "c_warframes": c_warframes,
        "p_warframes": p_warframes,
        "login_form": login_form,
        "register_form": register_form,
    }

    return render(request, "warframes.htm", context=context)


def downloads(request):
    download_items = ListItem.objects.filter(item_type=DOWNLOAD_ITEM)

    login_form = UserLoginForm()
    register_form = UserRegisterForm()

    context = {
        "download_items": download_items,
        "login_form": login_form,
        "register_form": register_form,
    }

    return render(request, "downloads.htm", context=context)

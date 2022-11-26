from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/")
def index(request):
    context = {
        "request": request
    }

    return render(request, "market_index.htm", context=context)


@login_required(login_url="/")
def list_item(request):
    context = {
        "request": request
    }

    return render(request, "list_item.htm", context=context)


@login_required(login_url="/")
def create_item(request):
    context = {
        "request": request
    }

    return render(request, "create_item.htm", context=context)

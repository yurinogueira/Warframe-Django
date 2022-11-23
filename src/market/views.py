from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/")
def index(request):
    context = {
    }

    return render(request, "catalog.htm", context=context)


@login_required(login_url="/")
def create_item(request):
    context = {
    }

    return render(request, "create_item.htm", context=context)

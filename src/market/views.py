from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from market.models import SellItem


@login_required(login_url="/")
def index(request):
    context = {
    }

    return render(request, "market_index.htm", context=context)


@login_required(login_url="/")
def list_item(request):
    items = SellItem.objects.select_related("image", "item_type").all()

    context = {
        "items": items
    }

    return render(request, "list_item.htm", context=context)


@login_required(login_url="/")
def create_item(request):
    context = {
    }

    return render(request, "create_item.htm", context=context)

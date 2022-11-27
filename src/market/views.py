from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from market.forms import SearchSellItemForm, SellItemForm
from market.models import SellItem


@login_required(login_url="/")
def index(request):
    context = {
    }

    return render(request, "market_index.htm", context=context)


@login_required(login_url="/")
def list_item(request):
    search_form = SearchSellItemForm(request.GET)
    if not search_form.is_valid():
        raise ValueError("Formulário inválido")

    name = search_form.cleaned_data["name"]
    items = SellItem.objects.select_related("image", "item_type").filter(name__icontains=name)
    paginator = Paginator(items, 3)

    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    context = {
        "items": page_obj,
        "form": search_form,
        "name": name,
    }

    return render(request, "list_item.htm", context=context)


@login_required(login_url="/")
def get_item(request, slug):
    item = get_object_or_404(SellItem, slug=slug)
    return render(request, "see_item.htm", {"item": item})


@login_required(login_url="/")
def create_item(request):
    if request.POST:
        item_form = SellItemForm(request.POST)
        if item_form.is_valid():
            item = item_form.save()
            messages.add_message(request, messages.INFO, "Item cadastrado com sucesso!")

            return redirect("market:get_item", slug=item.slug)
    else:
        item_form = SellItemForm()

    context = {
        "form": item_form,
    }

    return render(request, "create_item.htm", context=context)

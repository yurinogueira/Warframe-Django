from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from product.forms import ProductForm, EditProductForm
from product.models import Product


@login_required(login_url="/")
def index(request):
    return render(request, "product_index.htm")


@login_required(login_url="/")
def list_product(request):
    products = Product.objects.all()
    total_price = sum([(product.price * product.stock) for product in products])
    forms = [EditProductForm(initial={
        "id": product.id,
        "stock": product.stock
    }) for product in products]

    context = {
        "results": zip(products, forms),
        "total_price": int(total_price),
    }

    return render(request, "list_product.htm", context=context)


@login_required(login_url="/")
def create_product(request):
    if request.POST:
        form = ProductForm(request.POST)
        if not form.is_valid():
            raise ValueError("Formulário Inválido")

        product = form.save(commit=False)
        product.partial_price = product.price * product.stock
        product.save()

        products = Product.objects.all()
        total_price = sum([(product.price * product.stock) for product in products])

        return JsonResponse({
            "product": model_to_dict(product),
            "category": model_to_dict(product.item_type),
            "total_price": int(total_price)
        }, safe=False)
    else:
        form = ProductForm()

    context = {
        "form": form,
    }

    return render(request, "create_product.htm", context=context)


@login_required(login_url="/")
def edit_product(request):
    form = EditProductForm(request.POST)
    if not form.is_valid():
        raise ValueError("Formulário Inválido")

    pk = form.cleaned_data["id"]
    stock = form.cleaned_data["stock"]

    product = get_object_or_404(Product, id=pk)

    product.stock = stock
    product.partial_price = (product.price * stock)
    product.save(update_fields=["stock", "partial_price"])
    product_price = int(product.partial_price)

    products = Product.objects.all()
    total_price = sum([(product.price * product.stock) for product in products])

    return JsonResponse({
        "amount": products.count(),
        "product_price": product_price,
        "total_price": int(total_price),
    })


@login_required(login_url="/")
def delete_product(request):
    form = EditProductForm(request.POST)
    pk = form.data["id"]

    product = get_object_or_404(Product, id=pk)
    product.delete()

    products = Product.objects.all()
    total_price = sum([(product.price * product.stock) for product in products])

    return JsonResponse({"total_price": int(total_price)})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/")
def index(request):
    context = {
    }

    return render(request, "catalog.htm", context=context)

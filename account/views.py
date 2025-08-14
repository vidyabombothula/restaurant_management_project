from django.shortcuts import render

from django.conf import settings

def homepage(request):
    return render(request, "index.html",{
        "restaurant_phone":settings.RESTAURANT_PHONE
    })
